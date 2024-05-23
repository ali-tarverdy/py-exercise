#!/usr/bin/bash

word="rabbit"
python_script="/home/ali/w/PycharmProject/relax/bit_byte_meme.py"

# Run the Python script with the word as an argument
/usr/bin/python3 "$python_script" "$word"

# wget command to download the image
wget -O temp.png "$(cat temp.png)"

# Image conversion command
convert temp.png -resize x200 temp.png