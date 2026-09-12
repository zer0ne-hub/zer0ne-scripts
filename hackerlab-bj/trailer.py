#!/usr/bin/python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "numpy>=2.5.3",
#     "pillow>=12.3.0",
# ]
# ///
"""XOR all images in a folder and save the result as a new image."""

import os

import numpy as np
from PIL import Image


def xor_images(image_paths):
    """XOR all images in the given paths and return the result as a PIL Image."""
    result = np.array(Image.open(image_paths[0]).convert("L"))
    for path in image_paths[1:]:
        img = np.array(Image.open(path).convert("L"))
        result = np.bitwise_xor(result, img)
        return Image.fromarray(result, mode="L")


def main():
    """ entry point of the script."""
    frames_folder = "."
    output_folder = "."
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    image_paths = [os.path.join(frames_folder, f) for f in os.listdir(
        frames_folder) if os.path.isfile(os.path.join(frames_folder, f))]
    try:
        result_image = xor_images(image_paths)
        output_path = os.path.join(output_folder, "result.png")
        result_image.save(output_path)
        print("Output image saved to: ", output_path)
    except ValueError as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
