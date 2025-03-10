import os
import cv2
import numpy as np
from flask import Flask, request, render_template, send_file

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

SECRET_PASSWORD = "123"  # Change this password as needed

def encrypt_image(image_path, key=42):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Image not found or could not be loaded.")
    
    np.random.seed(key)
    height, width, _ = image.shape
    encrypted_image = image.copy()
    
    for i in range(height):
        for j in range(width):
            encrypted_image[i, j] = encrypted_image[i, j] ^ np.random.randint(0, 256, 3, dtype=np.uint8)
    
    encrypted_path = os.path.join(app.config['UPLOAD_FOLDER'], "encrypted_image.png")
    cv2.imwrite(encrypted_path, encrypted_image)
    return encrypted_path

def decrypt_image(encrypted_path, key=42):
    image = cv2.imread(encrypted_path, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Encrypted image not found or could not be loaded.")
    
    np.random.seed(key)
    height, width, _ = image.shape
    decrypted_image = image.copy()
    
    for i in range(height):
        for j in range(width):
            decrypted_image[i, j] = decrypted_image[i, j] ^ np.random.randint(0, 256, 3, dtype=np.uint8)
    
    decrypted_path = os.path.join(app.config['UPLOAD_FOLDER'], "decrypted_image.png")
    cv2.imwrite(decrypted_path, decrypted_image)
    return decrypted_path

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)
            encrypted_path = encrypt_image(image_path)
            return send_file(encrypted_path, as_attachment=True)
    return render_template("upload.html")

@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    password = request.form.get('password')
    if password != SECRET_PASSWORD:
        return "Authentication Failed! Incorrect Password.", 403
    
    file = request.files['file']
    if file:
        encrypted_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(encrypted_path)
        decrypted_path = decrypt_image(encrypted_path)
        return send_file(decrypted_path, as_attachment=True)
    return "No file uploaded.", 400

if __name__ == "__main__":
    app.run(debug=True)