
from PIL import Image

# Function to encrypt or decrypt the image
def process_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")  # Ensure RGBA format
        pixels = img.load()

        for i in range(img.size[0]):  # Width
            for j in range(img.size[1]):  # Height
                r, g, b, a = pixels[i, j]
                r = r ^ key
                g = g ^ key
                b = b ^ key
                pixels[i, j] = (r, g, b, a)  # Keep alpha unchanged

        img.save(output_path)
        print(f"Image saved to {output_path}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Pixel Manipulation Image Encryption Tool")
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

    input_file = input("Enter the path of the image file: ").strip().replace('"', '')
    output_file = input("Enter the path to save output image (with filename): ").strip().replace('"', '')
    key = int(input("Enter encryption/decryption key (0-255): "))

    process_image(input_file, output_file, key)


