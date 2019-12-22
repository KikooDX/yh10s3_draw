from PIL import Image

# program by KikooDX (kiko.ovh)
# file is expected to be a 14x14 monochrome bitmap

def image_read(path):
    image = Image.open(image_path)
    content = image.tobytes()
    width, height = image.size
    if width != height:
        raise ValueError("Image should be a square.")
    return content, width

def conf_read(project_path):
    content = ""
    objects_ids = []
    with open(project_path + "/conf.txt", "r") as file:
        content = file.read()
    content = content.split("\n")
    del content[0]
    for line in content:
        if line and line[0] != '#':
            objects_ids += [int(line)]
    return len(objects_ids), objects_ids

# constants
BASE_X = 128
MAX_X = 368
WIDTH = MAX_X - BASE_X + 16

output = "[save]\n"
id = 0
project_path = input("Project to open\n> ")
max_img, objects_ids = conf_read(project_path)
img = 1

while img <= max_img:
    image_path = f"{project_path}/{img}.bmp"

    # starting positions
    x = BASE_X
    y = 16

    content, step = image_read(image_path) # step is image width
    step = WIDTH / step
    if step == int(step):
        step = int(step)

    object_to_draw = objects_ids[img - 1]

    # draw
    for c in content:
        c = int(c)
        if (c):
            output += "{0}0={3}\n{0}1={1}\n{0}2={2}\n".format(id, x, y, object_to_draw)
            id += 1
        x += step
        if step < 16:
            if x > MAX_X + 15.9:
                y += step
                x = BASE_X
        elif x > MAX_X:
            y += step
            x = BASE_X

    img += 1

# write
output_path = project_path + ".yh10s3"
with open(output_path, "w") as file:
    file.write(output)

input("Done.")
