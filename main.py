from PIL import Image

# program by KikooDX (kiko.ovh)
# file is expected to be a 14x14 monochrome bitmap

def image_read(path):
    image = Image.open(image_path)
    content = image.tobytes()
    return content

output = "[save]\n"
id = 0
image_path = input("Image to open (q to stop)\n> ") + ".bmp"

while image_path != "q.bmp":
    # starting positions
    BASE_X = 144
    MAX_X = 352
    x = BASE_X
    y = 32

    content = image_read(image_path)
    object_to_draw = int(input("Object to draw (75 is block)\n> "))

    # draw
    for c in content:
        c = int(c)
        if (c):
            output += "{0}0={3}\n{0}1={1}\n{0}2={2}\n".format(id, x, y, object_to_draw)
            id += 1
        x += 16
        if x > MAX_X:
            y += 16
            x = BASE_X
    image_path = input("Image to open (q to stop)\n> ") + ".bmp"

# write
output_path = input("Save as\n> ") + ".yh10s3"
with open(output_path, "w") as file:
    file.write(output)

input("Done.")
