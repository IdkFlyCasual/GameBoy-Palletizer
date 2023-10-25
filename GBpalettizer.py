from PIL import Image

# Define the Game Boy palette
gameboy_palette = [(155, 188, 15), (139, 172, 15), (48, 98, 48), (15, 56, 15)]

# Define the Game Boy resolution
gameboy_width = 160
gameboy_height = 144

def convert_to_gameboy_resolution(input_image_path, output_image_path):
    # Open the input image
    image = Image.open(input_image_path)

    # Convert the image to grayscale
    grayscale_image = image.convert("L")

    # Resize the image to Game Boy resolution
    resized_image = grayscale_image.resize((gameboy_width, gameboy_height))

    # Create a new image with the Game Boy palette
    gameboy_image = Image.new("P", (gameboy_width, gameboy_height))
    gameboy_image.putpalette([color for rgb in gameboy_palette for color in rgb])

    # Convert the resized grayscale image to an indexed image with the Game Boy palette
    gameboy_image.paste(resized_image, (0, 0))

    # Save the converted and resized image
    gameboy_image.save(output_image_path)

if __name__ == "__main__":
    input_image_path = "/home/ted/Downloads/Saitama.jpeg"  # Replace with your input image file path
    output_image_path = "./gameboy_image.png"  # Replace with your desired output image file path

    convert_to_gameboy_resolution(input_image_path, output_image_path)
    print(f"Image converted and resized to Game Boy resolution, and saved as {output_image_path}")
