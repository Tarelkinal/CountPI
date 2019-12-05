from modules import *
import os

dx = 0.003
output_dir = 'square_movie'
img = 0
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


body1 = Body(0.6, -0.3, 100, 0.35)
body2 = Body(0.3, 0, 1, 0.1)
bodies = [body1, body2]

for i in range(200):
    snapshot(bodies, output_dir, img)
    move(bodies, dx)
    img += 1
    print(img)


