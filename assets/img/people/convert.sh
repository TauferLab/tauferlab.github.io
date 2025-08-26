#!/bin/bash

# Loop through all PNG, JPG, and JPEG files in the current directory
for file in *.png *.jpg *.jpeg; do
    # Check if the file exists (in case no matches are found)
    [ -e "$file" ] || continue

    # Get the base filename without extension
    filename="${file%.*}"

    # Run ffmpeg to convert and resize to 400x400
    ffmpeg -i "$file" -vf scale=400:400 "${filename}.webp"
done
