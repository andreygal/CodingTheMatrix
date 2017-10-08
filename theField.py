from image import file2image
from plotting import plot
from myProcs import center_pts


data = file2image('img01.png')

S = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

pts = {(x + (len(data) - y) * 1j) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] < (120, 120, 120)}

plot(center_pts(S), 10)