from image import file2image
from plotting import plot

data = file2image('img01.png')

pts = {(x + (len(data) - y) * 1j) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] < (120, 120, 120)}

