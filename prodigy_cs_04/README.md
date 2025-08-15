# 🖼 Pixel Manipulation for Image Encryption 🔐

This project was created as part of my **Cybersecurity Internship at Prodigy Infotech**.  
It encrypts and decrypts images at the pixel level using an XOR-based encryption key.

---

## 📌 Features
- Encrypts any image by changing each pixel’s RGB values.
- Decrypts back to the original image using the same key.
- Works with different image formats (PNG, JPG, GIF, etc.).
- Supports transparency (RGBA images).
- Simple, lightweight, and easy to run.

---

## ⚙ How It Works
1. The program reads the image pixel-by-pixel.
2. Each pixel’s RGB values are XORed with a key (0–255).
3. The encrypted image is save


## 🛠 Requirements
- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) library

Install Pillow:
```bash
pip install pillow
```

##How To Run
```bash
python pixel_encryption.py
```
