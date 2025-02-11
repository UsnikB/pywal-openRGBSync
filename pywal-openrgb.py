import json
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor

# Path to Pywal's colors.json
colors_file = '~/.cache/wal/colors.json'

# Load Pywal colors
with open(colors_file, 'r') as f:
    colors = json.load(f)

# Extract the first color from Pywal's palette
primary_color_hex = colors['colors']['color0']

# Convert hex to RGB
primary_color_rgb = RGBColor(
    int(primary_color_hex[1:3], 16),
    int(primary_color_hex[3:5], 16),
    int(primary_color_hex[5:7], 16)
)

# Connect to OpenRGB
client = OpenRGBClient()

# Apply the color to all devices
for device in client.devices:
    device.set_color(primary_color_rgb)

