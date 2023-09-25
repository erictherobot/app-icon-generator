import argparse
from PIL import Image
import os


def generate_macos_app_icons(source_image_path, output_directory):
    app_icon_sizes = [
        (16, 16),
        (32, 32),
        (64, 64),
        (128, 128),
        (256, 256),
        (512, 512),
        (1024, 1024),
    ]

    os.makedirs(output_directory, exist_ok=True)

    source_image = Image.open(source_image_path)

    for size in app_icon_sizes:
        icon = source_image.resize(size, Image.ANTIALIAS)

        # Standard icon
        icon_name = f"AppIcon-{size[0]}x{size[1]}.png"
        icon_path = os.path.join(output_directory, icon_name)
        icon.save(icon_path, "PNG")

        # 2x Retina icon
        retina_icon = source_image.resize((size[0] * 2, size[1] * 2), Image.ANTIALIAS)
        retina_icon_name = f"AppIcon-{size[0]}x{size[1]}@2x.png"
        retina_icon_path = os.path.join(output_directory, retina_icon_name)
        retina_icon.save(retina_icon_path, "PNG")

    print("macOS AppIcons generated successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate macOS AppIcons from a source image."
    )
    parser.add_argument(
        "source_image", help="Path to the source image file (1024x1024 px)."
    )
    parser.add_argument(
        "output_directory", help="Path to the output directory for AppIcons."
    )
    args = parser.parse_args()
    generate_macos_app_icons(args.source_image, args.output_directory)
