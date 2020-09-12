from PIL import Image
from os import listdir
from os.path import isfile, join

files_path = "//home//marcin//Pulpit//puzzle//puzzle_easy_variant//"
onlyfiles = [files_path+f for f in listdir(files_path) if isfile(join(files_path, f))]

def get_section(i):
    files = sorted(onlyfiles)[:i*49]
    images = [Image.open(x) for x in files]
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
    files = get_section(j)
    print(f'Stitching section #{j}')
    stitch_section(get_section(files), j)
print('Done')

sections_path = 'stitched//'
section_files = [sections_path+f for f in listdir(sections_path) if isfile(join(sections_path, f))]
section_files = sorted(section_files)

def stitch_sections(sections):
    widths, heights = zip(*(i.size for i in sections))
    print(f"Final image sizes: {sum(widths), heights[0]}")
    x = 0
    new_im = Image.new('RGB', (sum(widths), heights[0]))
    for im in sections:
        new_im.paste(im, (x, 0))
        x += im.size[0]

    new_im.save('test.jpg')

def get_sections(files):
    images = [Image.open(x) for x in files]
    print(images)
    return images

imgs = get_sections(section_files)
print(imgs)

for section in imgs:
    #print(section)
    #print(f'Stitching {section}')
    stitch_sections(get_sections(section))
print('Done')

im = Image.open('test.jpg')
im.show()
