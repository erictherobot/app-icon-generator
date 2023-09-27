# iOS App Store Screenshot Icon Generator in Python

If you build native iOS, iPad mobile or desktop applications you know that you need to create screenshots for the App Store. This can be a tedious process, especially if you have a lot of screenshots to create. Here's an open source python script I made that has been working great for me. It's easy to use and can save you a lot of time.

Follow the tutorial here: https://ericdavidsmith.com/blog/software/ios-app-store-screenshot-icon-generator-python

## Prerequisites and Dependencies

To run this Python script, you need:

Clone this repo first

```bash
git clone https://github.com/erictherobot/app-icon-generator.git
```

1. Python 3.x installed
2. PIL (Pillow) for image manipulation
3. A TrueType font (in this example, Baloo-Regular.ttf)

Install Pillow with pip:

```bash
pip install pillow
```

## How It Works

The script takes an original image and layers it with marketing text to create device-specific screenshots. It performs several operations:

1. **Rounding Corners**: `round_corners()` function rounds the corners of an image.
2. **Text Addition**: Marketing titles and taglines are added to the canvas.
3. **Image Placement**: The original image is resized and placed on the canvas.
4. **Saving**: The final canvas is saved as a PNG file.

## Customization

1. **Canvas Color**: Change the `"#1f1f1f"` in `Image.new()` to your desired background color.
2. **Font**: Replace "Baloo-Regular.ttf" with another TrueType font.
3. **Device Dimensions**: Edit `device_dimensions` dictionary to add/remove devices.
4. **Text Position**: Modify `title_y`, `subtitle1_y`, and `subtitle2_y` to adjust text positioning.

## How to Use

1. Save the script as `generate_screenshots.py`.
2. Download or create a `.ttf` font file and place it in the same directory as the script.
3. Place the original image in the same directory.

Run the script:

```bash
python generate_screenshots.py original.png "My App" "Best App Ever" "Download Now"
```

## Benefits

1. **Automated**: Generate multiple screenshots with a single command.
2. **Consistent**: Ensures uniformity across all device-specific screenshots.
3. **Efficient**: Reduces manual effort and human error.

## Results

Once the script is run, it will generate PNG files in the format `marketing_{device}_{timestamp}.png`.

## License

MIT

## Author

Eric David Smith

https://ericdavidsmith.com

Follow the tutorial here: https://ericdavidsmith.com/blog/software/ios-app-store-screenshot-icon-generator-python
