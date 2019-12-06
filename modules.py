import pylab, os

count = 0
img = 0


class Body:
    def __init__(self, pos0, vel0, mass, size):
        self.pos = pos0
        self.vel = vel0
        self.mass = mass
        self.size = size

    # def face_the_wall(self):
    #     return self.pos[0] <= 0


def snapshot(bodies, output_dir, n):
    global img
    if img % n == 0:
        colors = ["r", "g"]
        pylab.subplots_adjust(left=0.10, right=0.90, top=0.90, bottom=0.10)
        pylab.gcf().set_size_inches(12, 6)
        pylab.setp(pylab.gca(), xticks=[0, 2], yticks=[0, 1])
        for b, c in zip(bodies, colors):
            circle = pylab.Rectangle((b.pos, 0), b.size, b.size, color=c)
            pylab.gca().add_patch(circle)
        pylab.text(0.7, 0.8, f'счётчик столкновений: {count}')
        pylab.savefig(os.path.join(output_dir, f'{img}.png'), transparent=False)
        pylab.close()
    img += 1


def move(bodies, dt):
    global count
    # dt = min(dx / max(abs(bodies[1].vel), abs(bodies[0].vel)), 0.01)
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


