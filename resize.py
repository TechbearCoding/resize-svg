import svgutils.transform as sg
import sys
import os

# width and height you want to resize to
width='40'
height='40'

# assign directory
directory = './'

def resizeSvg(fname):
    fig = sg.fromfile(fname)
    fig.set_size((width, height))
    fig.save(fname)
    print(fname)

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file and if contains .svg in the file name
    if os.path.isfile(f) and '.svg' in f:
        resizeSvg(f)



