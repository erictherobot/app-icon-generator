import sys
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


def round_corners(image, radius):
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)

    draw.rectangle([(0, 0), (image.width, image.height)], fill=0)
    draw.ellipse([0, 0, radius * 2, radius * 2], fill=255)
    draw.ellipse([image.width - radius * 2, 0, image.width, radius * 2], fill=255)
    draw.ellipse([0, image.height - radius * 2, radius * 2, image.height], fill=255)
    draw.ellipse(
        [
            image.width - radius * 2,
            image.height - radius * 2,
            image.width,
            image.height,
        ],
        fill=255,
    )
    draw.rectangle([0, radius, image.width, image.height - radius], fill=255)
    draw.rectangle([radius, 0, image.width - radius, image.height], fill=255)

    image.putalpha(mask)
    return image


def add_to_canvas(canvas, image, x_offset, y_offset):
    canvas.paste(image, (x_offset, y_offset), image)


def resize_and_maintain_aspect(image, max_width, max_height):
    aspect_ratio = image.width / image.height
    new_width = min(max_width, int(max_height * aspect_ratio))
    new_height = min(max_height, int(max_width / aspect_ratio))
    return image.resize((new_width, new_height), Image.LANCZOS)


if len(sys.argv) < 4:
    print(
        "Usage: python script.py <path_to_original_image> <marketing_title> <marketing_tagline1> <marketing_tagline2>"
    )
    sys.exit(1)

original_file, marketing_title, marketing_tagline1, marketing_tagline2 = (
    sys.argv[1],
    sys.argv[2],
    sys.argv[3],
    sys.argv[4],
)

# Define the dimensions for each device
device_dimensions = {
    "iPhone_6_7": (1290, 2796),
    "iPhone_6_5": (1242, 2688),
    "iPhone_5_5": (1242, 2208),
    "iPad_Pro_6th_Gen": (2048, 2732),
    "iPad_Pro_2nd_Gen": (2048, 2732),
}

# Current time in YYYYMMDDHHMMSS format
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

# Loop through each device and generate the marketing image
for device, dimensions in device_dimensions.items():
    width, height = dimensions

    # Create a new canvas with the background color
    canvas = Image.new("RGBA", (width, height), "#1f1f1f")
    canvas = round_corners(canvas.convert("RGBA"), 100)
    draw = ImageDraw.Draw(canvas)

    # Load the Baloo font
    title_font = ImageFont.truetype("Baloo-Regular.ttf", 100)
    subtitle_font = ImageFont.truetype("Baloo-Regular.ttf", 60)

    # Center the marketing text
    title_w, title_h = draw.textsize(marketing_title, font=title_font)
    title_x = (width - title_w) // 2
    title_y = (200 - title_h) // 2  # Assuming the header area is 200px high

    subtitle1_w, subtitle1_h = draw.textsize(marketing_tagline1, font=subtitle_font)
    subtitle1_x = (width - subtitle1_w) // 2
    subtitle1_y = title_y + title_h + 15  # 15px below the title

    subtitle2_w, subtitle2_h = draw.textsize(marketing_tagline2, font=subtitle_font)
    subtitle2_x = (width - subtitle2_w) // 2
    subtitle2_y = subtitle1_y + subtitle1_h + 10  # 10px below the first tagline

    draw.text(
        (title_x, title_y), marketing_title, font=title_font, fill=(255, 255, 255)
    )
    draw.text(
        (subtitle1_x, subtitle1_y),
        marketing_tagline1,
        font=subtitle_font,
        fill=(255, 255, 255),
    )
    draw.text(
        (subtitle2_x, subtitle2_y),
        marketing_tagline2,
        font=subtitle_font,
        fill=(255, 255, 255),
    )

    # Open the original image and resize it while maintaining aspect ratio
    with Image.open(original_file) as img:
        max_height = height - 400
        img_resized = resize_and_maintain_aspect(img, width - 40, max_height - 40)

        # Round corners of the screenshot
        img_resized = round_corners(img_resized.convert("RGBA"), 100)

        x_offset = (width - img_resized.width) // 2
        y_offset = ((max_height - img_resized.height) // 2) + 400

        add_to_canvas(canvas, img_resized, x_offset, y_offset)

    # Remove alpha channel before saving
    canvas = canvas.convert("RGB")

    output_file = f"marketing_{device}_{timestamp}.png"
    canvas.save(output_file)

print("Images generated with marketing headers and saved.")
