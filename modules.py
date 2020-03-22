import pylab, os, math

count = 0
img = 0


class Body:
    def __init__(self, pos0, vel0, mass, size):
        self.pos = pos0
        self.vel = vel0
        self.mass = mass
        self.size = size


def snapshot(bodies, output_dir, n):  # n - задает частоту кадров
    global img
    if img % n == 0:
        colors = ["r", "g"]
        pylab.subplots_adjust(left=0.10, right=0.90, top=0.90, bottom=0.10)
        pylab.gcf().set_size_inches(12, 6)
        x = 2 if bodies[0].pos < 2 else math.ceil(bodies[0].pos)  # масштабирование
        y = 1 if bodies[0].pos < 2 else math.ceil(bodies[0].pos)/2
        pylab.setp(pylab.gca(), xticks=[0, x], yticks=[0, y])
        for b, c in zip(bodies, colors):
            Rect = pylab.Rectangle((b.pos, 0), b.size, b.size, color=c)
            pylab.gca().add_patch(Rect)
        pylab.text(0.7, 0.8, f'счётчик столкновений: {count}')
        pylab.savefig(os.path.join(output_dir, f'{img}.png'), transparent=False)
        pylab.close()
    img += 1


def move(bodies, dt):
    global count
    if bodies[1].pos <= 0:
        bodies[1].vel = -bodies[1].vel
        count += 1
    elif bodies[0].pos <= bodies[1].pos + bodies[1].size:
        v0x = bodies[0].vel
        v0y = bodies[1].vel
        bodies[0].vel = (bodies[0].mass*v0x + 2*bodies[1].mass*v0y - bodies[1].mass*v0x) / (bodies[1].mass + bodies[0].mass)
        bodies[1].vel = (bodies[1].mass*v0y + 2*bodies[0].mass*v0x - bodies[0].mass*v0y) / (bodies[1].mass + bodies[0].mass)
        count += 1
    for body in bodies:
        body.pos = body.pos + body.vel*dt


