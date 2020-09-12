from PIL import Image
from os import listdir
from os.path import isfile, join

files_path = "//home//marcin//Pulpit//puzzle//puzzle_easy_variant//"
onlyfiles = [files_path+f for f in listdir(files_path) if isfile(join(files_path, f))]

def get_section(i):
    files = sorted(onlyfiles)[:i*49]
    images = [Image.open(x) for x in files]
    return images

def stitch_section(sect, i):
    widths, heights = zip(*(i.size for i in sect))

    y = 0

    new_im = Image.new('RGB', (sum(widths), sum(heights)))
    
    for im in sect:
        new_im.paste(im, (0, y))
        y += im.size[1]
    
    new_im.save('test' + str(i) + '.jpg')

#stitch sections
x = 0
for i in range(52):
    stitch_section(get_section(2), i)

onlyfiles = [files_path+f for f in listdir(files_path) if isfile(join(files_path, f))]


