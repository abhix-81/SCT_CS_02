from PIL import Image

def swap_pixels(image_path, output_path, x1, y1, x2, y2):
    """
    Swaps the pixel values at coordinates (x1, y1) and (x2, y2) in the image.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the modified image.
        x1, y1, x2, y2 (int): Coordinates of the pixels to swap.
    """
    image = Image.open(image_path)
    pixels = image.load()

    # Swap pixel values
    pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]

    # Save the modified image
    image.save(output_path)
    print(f"Swapped pixels at ({x1}, {y1}) and ({x2}, {y2}). Saved to {output_path}")

def apply_math_operation(image_path, output_path, operation=lambda x: x + 50):
    """
    Applies a mathematical operation to each pixel value in the image.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the modified image.
        operation (function): Custom mathematical operation (default: add 50).
    """
    image = Image.open(image_path)
    pixels = image.load()

    # Apply operation to each pixel
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (operation(r), operation(g), operation(b))

    # Save the modified image
    image.save(output_path)
    print(f"Applied math operation to each pixel. Saved to {output_path}")

# Example usage
if __name__ == "__main__":
    input_image_path = "input_image.jpg"
    output_image_path = "output_image.jpg"

    # Swap pixels at coordinates (100, 200) and (300, 400)
    swap_pixels(input_image_path, output_image_path, 100, 200, 300, 400)

    # Apply a custom mathematical operation (subtract 30) to each pixel
    apply_math_operation(input_image_path, output_image_path, operation=lambda x: x - 30)
