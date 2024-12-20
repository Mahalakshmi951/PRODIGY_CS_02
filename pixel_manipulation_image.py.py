from PIL import Image

def encrypt_image(input_path, output_path, key=None):
    """
    Encrypts an image by swapping RGB values.
    """
    try:
        image = Image.open(input_path).convert("RGB")
        pixels = image.load()
        width, height = image.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                encrypted_pixel = (b, r, g)  # Encryption logic: reversible
                pixels[i, j] = encrypted_pixel

        image.save(output_path)
        print("Image encrypted successfully!")
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(input_path, output_path, key=None):
    """
    Decrypts an image by reversing the RGB swapping.
    """
    try:
        image = Image.open(input_path).convert("RGB")
        pixels = image.load()
        width, height = image.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                decrypted_pixel = (g, b, r)  # Reverse encryption logic
                pixels[i, j] = decrypted_pixel

        image.save(output_path)
        print("Image decrypted successfully!")
    except Exception as e:
        print(f"Error during decryption: {e}")

# File paths (modify as needed)
input_image=r"c:\Users\mahal\OneDrive\Desktop\pip\Input.jpg.jpg"
decrypted_image=r"c:\Users\mahal\OneDrive\Desktop\pip\decrypted_image.jpg"
encrypted_image=r"c:\Users\mahal\OneDrive\Desktop\pip\encrypted_image.jpg"

# Encrypt and Decrypt the image
encrypt_image(input_image, encrypted_image)
decrypt_image(encrypted_image, decrypted_image)
