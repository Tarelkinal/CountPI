from modules import *
import os

dt = 0.0000003  # 0.0003 - 1/100, 0.00003 - 1/10000, 0.000007 - 1/1000000 и далее
output_dir = 'square_movie'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


body1 = Body(0.6, -0.3, 100000000, 0.35) # (pos0 - х-координата, vel0, mass, size)
body2 = Body(0.3, 0, 1, 0.1)  # body1 - Большой куб, body2 - маленький куб
bodies = [body1, body2]

for i in range(12000001):
    snapshot(bodies, output_dir, 7200)
    move(bodies, dt)
    print(i)



