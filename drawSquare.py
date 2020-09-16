#! python3
# drawSquare.py - Draws square for into svg file

import svgwrite
from cairosvg import svg2png

def create_square():
    dwg = svgwrite.Drawing('square.svg', size=(5, 5))
    dwg.add(dwg.rect(insert=(0, 0), size=(5, 5), fill=svgwrite.utils.rgb(255, 255, 255)))      #outer square
    dwg.add(dwg.rect(insert=(0.5, 0.5), size=(4, 4), fill=svgwrite.utils.rgb(0, 0, 0)))        #mid square
    dwg.add(dwg.rect(insert=(1.0, 1.0), size=(3, 3), fill=svgwrite.utils.rgb(128, 128, 128)))  #inner square
    dwg.save()

    #convert .svg format to .png
    pngFile = svg2png('square.svg',write_to='square.png')

create_square()