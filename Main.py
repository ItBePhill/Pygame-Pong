import pygame as pg

pg.init()
#list of lists of surface and coordinate
obj = []
delta = 1
class player(object):
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = pg.Surface([width, height])
        self.colour = colour
    @staticmethod
    def draw(self):
        pg.draw.rect(window, self.colour, pg.Rect(self.x, self.y, self.width, self.height), 20)

p1: player = None
p2: player = None
window = pg.display.set_mode([800, 600])

def drawScreen(obj):
    # print(obj)
    window.fill([0,0,0])
    for i in obj:
        i.draw(i)
    pg.display.update()




def start():
    global obj, p1, p2
    p1 = player(100,400,20,50, pg.Color(255, 255, 255))
    p2 = player(700,400,20,50, pg.Color(255, 255, 255))
    obj.append(p1)
    obj.append(p2)
    return obj, p1, p2

start()

clock = pg.time.Clock()
running = True
while running:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            running = False
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        p1.y -= 300 * delta
    if keys[pg.K_s]:
        p1.y += 300 * delta
    if keys[pg.K_UP]:
        p2.y -= 300 * delta
    if keys[pg.K_DOWN]:
        p2.y += 300 * delta


    drawScreen(obj)
    delta = clock.tick(500)/1000
    print(clock.get_fps())

pg.quit()
