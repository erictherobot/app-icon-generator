import sys
from PIL import Image


def overlay_on_template(template_path, image_path, coordinates, output_path):
    with Image.open(template_path) as template, Image.open(image_path) as img:
        template.paste(img, coordinates)
        template.save(output_path)


def resize_image(original_file, output_file, dimensions):
    with Image.open(original_file) as img:
        img_resized = img.resize(dimensions)
        img_resized.save(output_file)


# Define the dimensions and template coordinates for each device
device_specs = {
    "iPhone_6_7": {
        "dimensions": (1284, 2778),
        "template": "template_6_7.png",
        "coordinates": (100, 100),
    },
    "iPhone_6_5": {
        "dimensions": (1242, 2688),
        "template": "template_6_5.png",
        "coordinates": (100, 100),
    },
    # Add other devices here...
}

if len(sys.argv) < 2:
    print("Usage: python script.py <path_to_original_image>")
    sys.exit(1)

original_file = sys.argv[1]

# Loop through each device and resize the image
for device, specs in device_specs.items():
    resized_file = f"resized_{device}.png"
    template_path = specs["template"]
    coordinates = specs["coordinates"]

    # Resize the image to the required dimensions
    resize_image(original_file, resized_file, specs["dimensions"])

    # Overlay the resized image onto the template
    output_file = f"final_{device}.png"
    overlay_on_template(template_path, resized_file, coordinates, output_file)

print("Images resized, overlaid on templates, and saved.")
