from PIL import Image
from PIL.ExifTags import TAGS
import os
import string
import re
from pprint import pprint
import sys

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    global info
    info = i._getexif()


def FileCleanup(fn):

    f = open(fn, 'r')
    filedata = f.read()
    f.close()

    filedata = filedata.replace("{", "")
    filedata = filedata.replace("}", "")
    filedata = filedata.replace("x00", "")
    filedata = filedata.replace("'", "")
    filedata = filedata.replace("\\", "")
    filedata = filedata.replace("::", "")
    filedata = filedata.replace("), ", "),\n")
    filedata = filedata.replace("', ", ",\n")
    filedata = filedata.replace("x01", "")
    filedata = filedata.replace("x00", "")
    filedata = filedata.replace("x02", "")
    filedata = filedata.replace("x03", "")
    filedata = filedata.replace("x04", "")
    filedata = filedata.replace("x05", "")
    filedata = filedata.replace("x06", "")
    filedata = filedata.replace("x07", "")
    filedata = filedata.replace("  ", "")


    f = open(fn, 'w')
    f.write(filedata)
    f.close()


def ConvertIDs(fn):
    f = open(fn, 'r')
    filedata = f.read()
    f.close()

    filedata = filedata.replace("256:", "Image Width:")
    filedata = filedata.replace("257:", "Image Length:")
    filedata = filedata.replace("271:", "Make:")
    filedata = filedata.replace("272:", "Model:")
    filedata = filedata.replace("274:", "Orientation:")
    filedata = filedata.replace("282:", "XResolution Px:")
    filedata = filedata.replace("283:", "YResolution Px:")
    filedata = filedata.replace("296:", "Resolution Unit:")  #if unknown 2(inches) is used
    filedata = filedata.replace("305:", "Software/Firmware:")
    filedata = filedata.replace("306:", "DateTime:")
    filedata = filedata.replace("531:", "YCbCr Positioning:")  #Position of chrominance data
    filedata = filedata.replace("33434:", "Exposure Time:")
    filedata = filedata.replace("33437:", "F Number:")  #Focal ratio
    filedata = filedata.replace("34665:", "Exif IFD:")
    filedata = filedata.replace("34850:", "Exposure Program:")
    filedata = filedata.replace("34855:", "ISO Speed:")
    filedata = filedata.replace("34864:", "Sensitivity:")
    filedata = filedata.replace("34867:", "ISO Speed:")
    filedata = filedata.replace("36864:", "Exif Version:")
    filedata = filedata.replace("36867:", "DateTime Original:")
    filedata = filedata.replace("36868:", "DateTime Digitized:")
    filedata = filedata.replace("37121:", "Components Configuration:")
    filedata = filedata.replace("37122:", "Compressed Bits Per Pixel:")
    filedata = filedata.replace("37377:", "Shutter Speed:")
    filedata = filedata.replace("37378:", "Lens Aperture:")
    filedata = filedata.replace("37379:", "Brightness:")
    filedata = filedata.replace("37380:", "Exposure Bias:")
    filedata = filedata.replace("37381:", "Max Aperture:")
    filedata = filedata.replace("37382:", "Subject Distance")  #Given in meters
    filedata = filedata.replace("37383:", "Metering Mode:")
    filedata = filedata.replace("37384:", "Light Source:")
    filedata = filedata.replace("37385:", "Flash:")
    filedata = filedata.replace("37386:", "Focal Length:")
    filedata = filedata.replace("37389:", "Noise")
    filedata = filedata.replace("37500:", "Manufacturer note:")
    filedata = filedata.replace("37510:", "User Comment:")
    filedata = filedata.replace("40960:", "Flash Pix Version:")
    filedata = filedata.replace("40961:", "Colour Space:")  #color space
    filedata = filedata.replace("40962:", "Pixel X Dimension:")  # Not present in not compressed
    filedata = filedata.replace("40963:", "Pixel Y Dimension:")
    filedata = filedata.replace("40965:", "Interoperability Tag:")
    filedata = filedata.replace("41493:", "Exposure Index:")
    filedata = filedata.replace("41495:", "Sending Method:")
    filedata = filedata.replace("41728:", "File Source:")
    filedata = filedata.replace("41729:", "Scene Type:")
    filedata = filedata.replace("41985:", "Custom Rendered:")
    filedata = filedata.replace("41986:", "Exposure Mode:")
    filedata = filedata.replace("41987:", "White Balance:")
    filedata = filedata.replace("41988:", "Digital Zoom Ratio:")
    filedata = filedata.replace("41989:", "FocalLengthIn35mmFilm:")
    filedata = filedata.replace("41990:", "Scene Capture Type:")
    filedata = filedata.replace("41991:", "Gain Control:")
    filedata = filedata.replace("41992:", "Contrast:")
    filedata = filedata.replace("41993:", "Saturation:")
    filedata = filedata.replace("41994:", "Sharpness:")
    filedata = filedata.replace("41995:", "Device Settings Description:")
    filedata = filedata.replace("41996:", "Subject Distance:")
    filedata = filedata.replace("42016:", "Unique ID:")
    filedata = filedata.replace("50341:", "Print Image Matching:")

    f = open(fn, 'w')
    f.write(filedata)
    f.close()


def PrintDict(Dict):
    with open(TextFileName, "a") as out:
        pprint(info, stream=out)

TextFileName = "DataOutput.txt"
f = open(TextFileName, "a")
ImagePath = "TestImage.JPG"
FileName = os.path.basename(ImagePath)
get_exif(ImagePath)
f.close()
PrintDict(info)
ConvertIDs(TextFileName)
FileCleanup(TextFileName)
pprint(filedata)
os.system('pause')