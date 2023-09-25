import sys
from PIL import Image, ImageDraw, ImageFont


def add_to_canvas(canvas, image, x_offset, y_offset):
    canvas.paste(image, (x_offset, y_offset))


def resize_and_maintain_aspect(image, max_width, max_height):
    aspect_ratio = image.width / image.height
    new_width = min(max_width, int(max_height * aspect_ratio))
    new_height = min(max_height, int(max_width / aspect_ratio))
    return image.resize((new_width, new_height), Image.LANCZOS)


# Define the dimensions for each device
device_dimensions = {
    "iPhone_6_7": (1284, 2778),
    "iPhone_6_5": (1242, 2688),
    "iPhone_5_5": (1242, 2208),
    "iPad_Pro_6th_Gen": (2048, 2732),
    "iPad_Pro_2nd_Gen": (2048, 2732),
}

if len(sys.argv) < 4:
    print(
        "Usage: python script.py <path_to_original_image> <marketing_title> <marketing_tagline>"
    )
    sys.exit(1)

original_file, marketing_title, marketing_tagline = (
    sys.argv[1],
    sys.argv[2],
    sys.argv[3],
)

# Loop through each device and generate the marketing image
for device, dimensions in device_dimensions.items():
    width, height = dimensions

    # Create a new canvas with the background color
    canvas = Image.new("RGB", (width, height), "#1f1f1f")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()

    # Add marketing text
    draw.text((20, 20), marketing_title, font=font, fill=(255, 255, 255))
    draw.text((20, 70), marketing_tagline, font=font, fill=(255, 255, 255))

    # Open the original image and resize it while maintaining aspect ratio
    with Image.open(original_file) as img:
        max_height = height - 400
        img_resized = resize_and_maintain_aspect(img, width - 40, max_height - 40)

        x_offset = (width - img_resized.width) // 2
        y_offset = ((max_height - img_resized.height) // 2) + 400

        add_to_canvas(canvas, img_resized, x_offset, y_offset)

    output_file = f"marketing_{device}.png"
    canvas.save(output_file)

print("Images generated with marketing headers and saved.")
