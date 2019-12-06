from modules import *
import os

dx = 0.001
output_dir = 'square_movie'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


body1 = Body(0.6, -0.3, 100, 0.35)
body2 = Body(0.3, 0, 1, 0.1)
bodies = [body1, body2]

for i in range(10000):
    snapshot(bodies, output_dir)
    move(bodies, dx)
    print(i)

dt_array[0] = 0.01
print(min(dt_array))

