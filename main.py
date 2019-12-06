from modules import *
import os

dt = 0.0003
output_dir = 'square_movie'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


body1 = Body(0.6, -0.3, 100, 0.35)
body2 = Body(0.3, 0, 1, 0.1)
bodies = [body1, body2]

for i in range(10):
    snapshot(bodies, output_dir, 2)
    move(bodies, dt)
    print(i)



