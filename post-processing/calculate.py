

import sys
import os
from fontTools import ttLib



def find_upm(directory):
    upm = 0
    for filename in os.listdir(directory):
        if filename.endswith(".otf") or filename.endswith(".ttf"):
            font = ttLib.TTFont(os.path.join(directory, filename))
            if font['head'].unitsPerEm > upm:
                upm = font['head'].unitsPerEm
    return upm

def find_yMax(directory):
    yMax = 0
    for filename in os.listdir(directory):
        if filename.endswith(".otf") or filename.endswith(".ttf"):
            font = ttLib.TTFont(os.path.join(directory, filename))
            if font['head'].yMax > yMax:
                yMax = font['head'].yMax
    return yMax

def find_yMin(directory):
    yMin = 0
    for filename in os.listdir(directory):
        if filename.endswith(".otf") or filename.endswith(".ttf"):
            font = ttLib.TTFont(os.path.join(directory, filename))
            if font['head'].yMin < yMin:
                yMin = font['head'].yMin
    return yMin

def find_capHeight(directory):
    capHeight = 0
    for filename in os.listdir(directory):
        if filename.endswith(".otf") or filename.endswith(".ttf"):
            font = ttLib.TTFont(os.path.join(directory, filename))
            if font['OS/2'].sCapHeight > capHeight:
                capHeight = font['OS/2'].sCapHeight
    return capHeight

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python countFontsInDirectory.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    find_yMax(directory)