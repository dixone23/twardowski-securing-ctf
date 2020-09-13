from PIL import Image
from os import listdir
from os.path import isfile, join
import os

files_path = "//home//marcin//Pulpit//puzzle//puzzle_easy_variant//"
onlyfiles = [files_path+f for f in listdir(files_path) if isfile(join(files_path, f))]

def get_section(i):
    files = sorted(onlyfiles)[i:i+49]
    images = [Image.open(x) for x in files]
#    print(i, len(images))
    return images

def stitch_section(sect, j):
    widths, heights = zip(*(i.size for i in sect))

    y = 0

    new_im = Image.new('RGB', (widths[0], sum(heights)))
    
    for im in sect:
        new_im.paste(im, (0, y))
        y += im.size[1]
    
    new_im.save('stitched//test' + str(j) + '.jpg')

#stitch sections
x = 0
for j in range(1, 52):
    os.system('clear')
    files = get_section(j)
    print(f'Stitching section #{j}')
    stitch_section(get_section(j), j)
os.system('clear')
print('Done')


#list master image files
sections_path = 'stitched//'
section_files = [sections_path+f for f in listdir(sections_path) if isfile(join(sections_path, f))]
section_files = sorted(section_files)

#function to load all the master image files with PIL
def get_sections(files):
    images = [Image.open(x) for x in files]
    return images

#again, get the size of the final image
imgs = get_sections(section_files)
widths, heights = zip(*(i.size for i in imgs))
print(f"Master image size: {sum(widths), heights[0]}")

#create temp image
new_im = Image.new('RGB', (sum(widths), heights[0]))

#stitch master image chunks
x = 0
for im in imgs:
    new_im.paste(im, (x, 0))
    x += im.size[0]

#save and show
new_im.save('master.jpg')
new_im.show()
