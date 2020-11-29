import pygame
import random
pygame.init()

framew, frameh = 500, 250
frame = pygame.display.set_mode((framew, frameh))
pygame.display.set_caption('GAYME')
fps = pygame.time.Clock()
bulletpos, bulletpos2, score = 0, 0, 0

walkleft = [pygame.image.load('skl1_lf1.png'), pygame.image.load('skl1_lf2.png')]
walkright = [pygame.image.load('skl1_rt1.png'), pygame.image.load('skl1_rt2.png')]
walkup = [pygame.image.load('skl1_bk1.png'), pygame.image.load('skl1_bk2.png')]
walkdown = [pygame.image.load('skl1_fr1.png'), pygame.image.load('skl1_fr2.png')]
bg = pygame.image.load('back2.jpg')
neutral = pygame.image.load('skl1_fr1.png')
eleft = [pygame.image.load('bmg1_lf1.png'), pygame.image.load('bmg1_lf2.png')]
eright = [pygame.image.load('bmg1_rt1.png'), pygame.image.load('bmg1_rt2.png')]
eneutral = pygame.image.load('bmg1_fr1.png')
dead = pygame.image.load('dead.png')
font = pygame.font.Font('freesansbold.ttf', 32)


def walkcheck(x):
    if x + 1 >= 3:
        x = 0
    return x


class Player(object):

    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 5
        self.jump = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkcount = 0
        self.jstate = False
        self.standing = True
        self.health = 10

    def framer(self):
        if self.health > 0 and boi.dead is False:
            self.walkcount = walkcheck(self.walkcount)
            if not self.standing:
                if self.left and self.jstate is False:
                    frame.blit(walkleft[self.walkcount], (self.x, self.y))
                    self.walkcount += 1
                    self.walkcount = walkcheck(self.walkcount)
                elif self.right and self.jstate is False:
                    frame.blit(walkright[self.walkcount], (self.x, self.y))
                    self.walkcount += 1
                    self.walkcount = walkcheck(self.walkcount)

                elif self.right and self.jstate:
                    frame.blit(walkright[1], (self.x, self.y))
                elif self.left and self.jstate:
                    frame.blit(walkleft[1], (self.x, self.y))
            else:
                if self.left:
                    frame.blit(walkleft[0], (self.x, self.y))
                elif self.right:
                    frame.blit(walkright[0], (self.x, self.y))
                else:
                    frame.blit(walkdown[0], (self.x, self.y))
            if self.up:
                frame.blit(walkup[self.walkcount], (self.x, self.y))
                self.walkcount += 1
                self.right = False
                self.left = False
                self.walkcount = walkcheck(self.walkcount)
            elif self.down:
                frame.blit(walkdown[self.walkcount], (self.x, self.y))
                self.walkcount += 1
                self.right = False
                self.left = False
                self.walkcount = walkcheck(self.walkcount)
            if updown and not self.right and not self.left:
                if self.up:
                    frame.blit(walkup[self.walkcount], (self.x, self.y))
                else:
                    frame.blit(walkdown[self.walkcount], (self.x, self.y))
        else:
            frame.blit(dead, (self.x, self.y))
            # self.health = 10

def mainframe():
    global bulletpos, bulletpos2
    frame.blit(bg, (0, 0))
    nig.framer()
    boi.draw()
    boi.rev()
    for i in bullets:
        bulletpos = i.x
        bulletpos2 = i.y
        boi.die()
        i.delete()
        i.draw()
    pygame.display.update()


class Ak(object):

    def __init__(self, x, y, colour, radius, win, state, tybe):
        self.x = x
        self.y = y
        self.colour = colour
        self.radius = radius
        self.vel = 20 * state
        self.win = win
        self.type = tybe

    def delete(self):
        if bulletpos in range(boi.x, boi.x + boi.width) and bulletpos2 in range(boi.y, boi.y + boi.height):
            self.type = 2

    def draw(self):
        if self.type == 0:
            pygame.draw.rect(self.win, self.colour, (self.x, self.y, 5, 2))
        elif self.type == 1:
            pygame.draw.circle(self.win, self.colour, (self.x, self.y), self.radius, circal)
        elif self.type == 2:
            pass


class Enemy(object):

    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 4
        self.el = False
        self.er = False
        self.reset = False
        self.dead = False
        self.revivewait = 0
        self.walkcount = 0
        self.health = 20

    def die(self):
        global score
        if bulletpos in range(self.x, self.x + self.width) and bulletpos2 in range(self.y, self.y + self.height):
            self.health -= 1
            if not self.dead:
                score += 1
            if self.health <= 0:
                self.health = 0
                self.dead = True

    def rev(self):
        if self.revivewait == 100:
            self.dead = False
            self.health = 20
            self.el = True
            self.x = 460
            self.y = 63

    def draw(self):
        if nig.x in range(self.x, self.x + self.width) and nig.y in range(self.y, self.y + self.height) and self.dead is False:
            nig.health -= 1
        elif nig.x + nig.width in range(self.x, self.x + self.width) and nig.y + nig.height in range(self.y, self.y + self.height) and self.dead is False:
            nig.health -= 1
        self.walkcount = walkcheck(self.walkcount)
        if self.dead:
            frame.blit(walkdown[0], (self.x, self.y))
            self.el = False
            self.er = False
        else:
            if self.el:
                frame.blit(eleft[self.walkcount], (self.x, self.y))
                self.walkcount += 1
            elif self.er:
                frame.blit(eright[self.walkcount], (self.x, self.y))
                self.walkcount += 1
            elif self.reset:
                frame.blit(eright[self.walkcount], (self.x, self.y))
                self.walkcount += 1
        pygame.draw.rect(frame, (255, 0, 0), (self.x + 5, self.y - 5, 20, 5))
        pygame.draw.rect(frame, (0, 255, 0), (self.x + 5, self.y - 5, self.health, 5))
        frame.blit(font.render(str(score), True, (0, 0, 255)), (0, 225))
# x = 20
# y = 63
# height = 32
# width = 32
# vel = 3
# jump = 10


why = 0

# left = False
# right = False
# up = False
# down = False
# walkcount = 0
# jstate = False
run = True
updown = False
hwchanger = False
drop = False

nig = Player(20, 63, 32, 32)
bullets = []
boi = Enemy(460, 63, 32, 32)
nig.right = True
while run:
    circal = random.randint(0, 1)
    lg, bt, q = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    pygame.time.delay(30)
    fps.tick(100)
    if nig.jstate is False:
        why = nig.y
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                updown = not updown
                print(f'up down restriction: {updown}')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                hwchanger = not hwchanger
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and nig.jstate is True:
                drop = True
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if 500 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.remove(bullet)
    if boi.x == 460 and boi.y == 63:
        boi.el = True
        boi.er = False
        boi.reset = False
    elif boi.x == 460:
        boi.el = True
        boi.er = False
    if boi.el:
        boi.x -= boi.vel
    if boi.x == 400 and boi.y == 63:
        boi.er = True
        boi.el = False
    if boi.er:
        boi.x += boi.vel
        boi.y -= boi.vel
    if boi.x == 400 and boi.y == 3:
        boi.reset = True
        boi.er = False
        boi.el = False
    if boi.reset:
        boi.x += boi.vel
        boi.y += boi.vel

    keys = pygame.key.get_pressed()
    if nig.left:
        nig.state = -1
        bulletx = nig.x
    else:
        nig.state = 1
        bulletx = nig.x + nig.width

    if keys[pygame.K_f]:
        if len(bullets) < 5:
            bullets.append(Ak(bulletx, nig.y + nig.height // 2, (lg, bt, q), 4, frame, nig.state, 0))
    if keys[pygame.K_g]:
        if len(bullets) < 5:
            bullets.append(Ak(bulletx, nig.y + nig.height // 2, (lg, bt, q), 4, frame, nig.state, 1))

    if updown:
        if keys[pygame.K_w] and nig.jstate is False:
            nig.y -= nig.vel
            nig.up = True
            nig.down = False
            nig.standing = False
        elif keys[pygame.K_s] and nig.jstate is False:
            nig.y += nig.vel
            nig.up = False
            nig.down = True
            nig.standing = False
        else:
            nig.up = False
            nig.down = False
            nig.standing = True
    elif updown is False and nig.jstate is True:
        if drop is True:
            nig.y = why
            nig.jstate = False
            drop = False
            nig.jump = 10
            nig.standing = True

    if keys[pygame.K_a]:
        nig.x -= nig.vel
        nig.left = True
        nig.right = False
        nig.standing = False
    elif keys[pygame.K_d]:
        nig.x += nig.vel
        nig.left = False
        nig.right = True
        nig.standing = False
    else:
        nig.standing = True
    if hwchanger:
        if keys[pygame.K_UP]:
            nig.height += 10
        if keys[pygame.K_RIGHT]:
            nig.width += 10
        if keys[pygame.K_DOWN]:
            nig.height -= 10
        if keys[pygame.K_LEFT]:
            nig.width -= 10
    if keys[pygame.K_q]:
        nig.vel += 10
    if keys[pygame.K_e]:
        nig.vel -= 10

    # jump

    if keys[pygame.K_SPACE]:
        nig.jstate = True
        nig.standing = False
    if nig.jstate is True and 2 < nig.jump <= 10:
        nig.y -= round(abs(nig.jump))
        nig.jump -= 1
    if nig.jump == 2:
        nig.jump = -3
    if nig.jstate is True and -10 <= nig.jump < -2:
        nig.y += round(abs(nig.jump))
        nig.jump -= 1
    if nig.jump == -11:
        nig.jump = 10
        nig.jstate = False
        nig.standing = True
    print(nig.health)
    # borderlimiter
    nig.x = min(max(nig.x, 0), framew - nig.width)
    nig.y = min(max(nig.y, 0), frameh - nig.height)
    if boi.dead:
        boi.revivewait += 1
    else:
        boi.revivewait = 0
    mainframe()

pygame.quit()
