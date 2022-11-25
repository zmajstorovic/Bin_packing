import random

from rectpacker.rectpack import newPacker
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle



def plotter(abin, height, width):
    fig, ax = plt.subplots()
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    for rect in abin:

        # add rectangle to plot
        # print(rect.corner_bot_l.x, rect.corner_bot_l.y, rect.corner_top_r.x, rect.corner_top_r.y)
        ax.add_patch(Rectangle((rect.corner_bot_l.x, rect.corner_bot_l.y),
                               rect.width, rect.height, edgecolor='white', lw=1))
    plt.show()





coords = [(random.randint(0,70), random.randint(10,70)) for _ in range(50)]
rectangles = [(14, 23), (63, 18), (33, 36), (23, 23), (4, 40), (64, 42), (64, 64), (32, 10), (25, 57), (19, 17), (62, 51), (62, 47), (15, 68), (27, 67), (11, 55), (68, 20), (41, 51), (17, 56), (4, 17), (59, 40), (53, 33), (51, 14), (20, 49), (69, 25), (23, 54), (27, 63), (65, 63), (65, 40), (69, 51), (34, 16), (26, 47), (70, 49), (28, 51), (37, 39), (9, 24), (55, 34), (44, 37), (9, 43), (57, 50), (58, 47), (25, 68), (41, 38), (26, 34), (31, 61), (37, 21), (39, 25), (4, 34), (13, 68), (58, 56), (29, 64)]
rectangles1 = [(100, 30), (40, 60), (30, 30), (70, 70), (100, 50), (30, 30), (30, 30), (70, 70), (100, 50), (30, 30)]
bins = [(100, 80), (80, 40), (200, 150)]

packer = newPacker()

# Add the rectangles to packing queue
for r in rectangles:
    packer.add_rect(*r)

# Add the bins where the rectangles will be placed
for b in bins:
    packer.add_bin(*b)

# Start packing
packer.pack()

# Obtain number of bins used for packing
nbins = len(packer)

# Index first bin
abin = packer[0]

# Bin dimmensions (bins can be reordered during packing)
width, height = abin.width, abin.height

# Number of rectangles packed into first bin
nrect = len(packer[0])

# Second bin first rectangle
rect = packer[1][0]

# rect is a Rectangle object
x = rect.x  # rectangle bottom-left x coordinate
y = rect.y  # rectangle bottom-left y coordinate
w = rect.width
h = rect.height


for abin in packer:
    print(abin.bid)  # Bin id if it has one
    plotter(abin, abin.height, abin.width)


