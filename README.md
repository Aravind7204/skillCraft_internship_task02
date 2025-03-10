# 🖼️ Image Encryption and Decryption Tool (Python + Flask)

A simple **web-based application** built with **Python**, **OpenCV**, and **Flask**, that allows users to **encrypt** and **decrypt** images using basic **pixel-level encryption**.  
This project demonstrates how image data can be manipulated for confidentiality and how to restore the original image when authorized.

---

## 📝 About the Project

This project encrypts an image by applying **bitwise XOR encryption** to each pixel with a pseudo-random key. The same process can decrypt the encrypted image by applying the XOR operation again using the same key.

The project provides a **web interface** where users can:
- Upload an image to encrypt and download the encrypted version.
- Upload an encrypted image, enter a password, and download the decrypted original.

---

## 💡 Features
✅ Encrypt any uploaded image (PNG, JPG, etc.).  
✅ Decrypt previously encrypted images (password-protected access).  
✅ Simple and intuitive web interface built with Flask.  
✅ Randomized encryption using **NumPy** and **OpenCV** libraries.  
✅ XOR-based encryption ensures reversibility (same operation to decrypt).  
✅ Password-protected decryption route for basic authentication.

---

## 📂 Project Structure
```
/uploads/                  # Folder to store uploaded, encrypted, and decrypted images
/templates/
    upload.html            # HTML page for uploading files
app.py                     # Main Flask application
```

---

## ▶️ How It Works

### Encryption Process
- Reads the input image.
- Generates a pseudo-random sequence (based on a key/seed).
- Performs a **bitwise XOR** operation between each pixel's RGB values and the random values.
- Saves and returns the encrypted image.

### Decryption Process
- Reads the encrypted image.
- Uses the same pseudo-random sequence (same key/seed) to reverse the XOR operation.
- Returns the decrypted image (original).

⚠️ **Note:**  
The encryption/decryption process is **symmetric**. If the key is lost, the original image cannot be recovered.

---

## 🛠️ Technologies Used
- **Python 3.x**
- **Flask**
- **OpenCV (cv2)**
- **NumPy**
- **HTML (basic upload form)**

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed  
- Install required packages:
  ```bash
  pip install flask opencv-python numpy
  ```

### Running the App
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CyberSecurity-Projects.git
   cd CyberSecurity-Projects
   git checkout image-encryption
   ```

2. Run the Flask app:
   ```bash
   python app.py
   ```

3. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🖼️ Usage Guide

### Encrypt an Image
- Open the web page `/`
- Upload an image.
- The encrypted image will automatically download after processing.

### Decrypt an Image
- Send a POST request to `/decrypt` (or build a front-end form for decryption).
- Upload the encrypted image.
- Enter the **password** (default is `123` in the code—change for better security!).
- The decrypted image will download automatically.

---

## 🔐 Password Protection (Decryption)
- `SECRET_PASSWORD` in the code is currently set to `"123"`.
- You can modify it in the `app.py` file:
  ```python
  SECRET_PASSWORD = "your_strong_password"
  ```

---

## 📄 Example Flow

### Encryption  
➡️ Upload: `flower.jpg`  
⬇️ Downloaded encrypted file: `encrypted_image.png`

### Decryption  
➡️ Upload: `encrypted_image.png`  
🔑 Password: `123`  
⬇️ Downloaded decrypted file: `decrypted_image.png` (restored original)

---

## 📌 Improvements You Can Make
✅ Use a **better encryption algorithm** (AES, RSA, etc.).  
✅ Add **user authentication** for upload/decrypt routes.  
✅ Store **encryption keys** per user session.  
✅ Improve **UI/UX** with CSS/JavaScript (Bootstrap, etc.).  
✅ Add **logging and error handling** for production use.

---

## ⚠️ Disclaimer
This project is for **educational purposes** and should **not** be used for serious security applications. The encryption method is simple and not secure against advanced attacks.

---

## 📄 License
Free for personal and educational use!

---

Let me know if you want a **`upload.html` template** for the front end or if you want to upgrade this project with **advanced encryption**! 🚀
