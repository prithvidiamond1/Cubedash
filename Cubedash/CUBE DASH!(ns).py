
from __future__ import division
import pygame
import random
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

finalscore = 0

ch = True
gamespeed = 4
cubecount = 15
resetval = 4

pygame.init()

#clicksnd = pygame.mixer.Sound('pingclick.ogg')

displayWidth = 800
displayHeight = 600
#displayWidth and DisplayHeight should be in the ratio 4:3 for better graphics

buttonWidth=150
buttonHeight=75
#buttonWidth and buttonHeight should be in the ratio 2:1 for better graphics

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
lime=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
aqua=(0,255,255)
fuchsia=(255,0,255)
silver=(192,192,192)
gray=(128,128,128)
Maroon=(128,0,0)
olive=(128,128,0)
green=(0,128,0)
purple=(128,0,128)
teal=(0,128,128)
navy=(0,0,128)
orange=(255,165,0)
gold=(255,215,0)
sandy_brown=(244,164,96)
dark_blue=(0,0,139)
hot_pink=(255,105,180)
deep_pink=(255,20,147)
deep_sky_blue=(0,191,255)
dullblue = (0, 0, 200)
dullred = (200, 0, 0)
dullgreen = (0, 200, 0)
firebrick=(178,34,34)
dim_gray=(105,105,105)
burly_wood=(222,184,135)

gamedisplay = pygame.display.set_mode((displayWidth, displayHeight))
icon = pygame.image.load('cubedashicon.png')
g1 = pygame.image.load('gear1.png')
g2 = pygame.image.load('gear2.png')

pygame.display.set_icon(icon)

pygame.display.set_caption('CUBE_DASH!')

clock = pygame.time.Clock()

colorlines = (
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0)
        )

colorquads = (
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 0, 1)
            )

vertices = (
        (2, -2, -2),
        (2, 2, -2),
        (-2, 2, -2),
        (-2, -2, -2),
        (2, -2, 2),
        (2, 2, 2),
        (-2, -2, 2),
        (-2, 2, 2)
            )

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
        )

surfaces = (
    (0, 1, 2, 3),
    (6, 7, 5, 4),
    (3, 2, 7, 6),
    (4, 5, 1, 0),
    (0, 3, 6, 4),
    (1, 2, 7, 5)
            )

ground_vertices = (
    (-75, -0.3, -200),
    (-75, -0.3, 40),
    (75, -0.3, 40),
    (75, -0.3, -200)
)

wall1_vertices = (
    (75, -0.3, -200),
    (75, 100, -200),
    (95, 100, -200),
    (95, -0.3, -200),
    (75, -0.3, 40),
    (75, 100, 40),
    (95, -0.3, 40),
    (95, 100, 40),
)

wall2_vertices = (
    (-75, -0.3, -200),
    (-75, 100, -200),
    (-95, 100, -200),
    (-95, -0.3, -200),
    (-75, -0.3, 40),
    (-75, 100, 40),
    (-95, -0.3, 40),
    (-95, 100, 40),
)

wallcolorlines = (
    (1, 0, 0),
    (1, 0, 0),
    (1, 0, 0),
    (1, 0, 0),
    (1, 0, 0),
    (1, 0, 0)
        )

wallcolorquads = (
    (1, 0, 0),
    (1, 0.6, 0.6),
    (1, 0, 0),
    (1, 0.6, 0.6),
    (1, 0, 0),
    (1, 0.6, 0.6)
            )

def ground(ground_vertices):
    glBegin(GL_QUADS)
    for vertex in ground_vertices:
        glColor3fv((0.2, 0.3, 0.4))
        glVertex3fv(vertex)
    glEnd()

    glBegin(GL_LINES)
    for vertex in ground_vertices:
        glColor3fv((1, 0, 0))
        # glColor3fv((1, 1, 1))
        glVertex3fv(vertex)
    glEnd()


def wall(wall_vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(wallcolorquads[x])
            glVertex3fv(wall_vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        x = 0
        for vertex in edge:
            x += 1
            glColor3fv(wallcolorlines[x])
            glVertex3fv(wall_vertices[vertex])
    glEnd()


def set_g_vertices(camera_z, camera_x=0, camera_y=0):
    x_val_change = 0
    y_val_change = 0
    z_val_change = camera_z

    new_vertices = []

    for vert in ground_vertices:
        new_vert = []

        new_x = vert[0] + x_val_change
        new_y = vert[1] + y_val_change
        new_z = vert[2] + z_val_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices


def Cube(vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colorquads[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        x = 0
        for vertex in edge:
            x += 1
            glColor3fv(colorlines[x])
            glVertex3fv(vertices[vertex])
    glEnd()


def windowquit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


def set_vertices(max_distance, min_distance=-20, camera_x=0, camera_y=0):
    x_val_change = random.randrange(-75, 75)
    y_val_change = 1.7
    z_val_change = random.randrange(-1*max_distance, -1*min_distance)

    val_changes = []

    val_changes.append(x_val_change)
    val_changes.append(y_val_change)
    val_changes.append(z_val_change)

    return val_changes


def main():
    global gamespeed
    global cubecount
    global resetval

    gamespeed = resetval

    pygame.init()
    displayWidth = 800
    displayHeight = 600
    gamedisplay = pygame.display.set_mode((displayWidth, displayHeight), DOUBLEBUF | OPENGL)

    pygame.display.set_caption('CUBE DASH!')

    x_move = 0
    y_move = 0

    cur_x = 0
    cur_y = 0

    # gamespeed = 4 #2 #3
    initialspeed = gamespeed
    resetval = initialspeed
    direction_speed = 1

    max_distance = 200 #100 #200 #300
    min_distance = 100

    # cubecount = 15 #15

    cube_pos_dict = {}
    for x in range(cubecount):
        cube_pos_dict[x] = set_vertices(max_distance, min_distance)

    g_surf_dict = {}
    for x in range(1):
        g_surf_dict[x] = set_g_vertices(max_distance)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45, displayWidth/displayHeight, 0.1, max_distance)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -40)

    clock = pygame.time.Clock()
    FPS = int(clock.get_fps())
    displayFPS = str(FPS)

    dt = 0
    timer = 1

    #pygame.mixer.music.load('TokyoMachine_ROCK_IT.ogg')

    #pygame.mixer.music.play(-1)

    global finalscore

    crashed = False

    displaylist = glGenLists(1)
    glNewList(displaylist, GL_COMPILE)
    Cube(vertices)
    glEndList()

    while not crashed:
        x = glGetDoublev(GL_MODELVIEW_MATRIX)  # Numpy is a dependent module for this function of opengl to work.
        # print(x)
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        cur_x += x_move
        cur_y += y_move

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = direction_speed
                if event.key == pygame.K_RIGHT:
                    x_move = -1*direction_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0

        FPS = int(clock.get_fps())
        displayFPS = str(FPS)

        img2 = pygame.font.Font(None, 20).render(displayFPS, True, (40, 180, 255))
        w, h = img2.get_size()
        texture2 = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glBindTexture(GL_TEXTURE_2D, texture2)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        data = pygame.image.tostring(img2, "RGBA", 1)
        glTexImage2D(GL_TEXTURE_2D, 0, 4, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)

        timer -= dt
        stimer = int(round(timer, 2))
        if stimer == 0:
            gamespeed += 0.0005

            timer = 1

        dt = clock.tick(60)/1000

        score = (gamespeed-initialspeed)*(10**4)*(cubecount/5)

        # Generating shader for text
        img = pygame.font.Font(None, 60).render('Score: '+str(int(score)), True, (255, 255, 255))
        w, h = img.get_size()
        texture = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        data = pygame.image.tostring(img, "RGBA", 1)
        glTexImage2D(GL_TEXTURE_2D, 0, 4, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, data)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        ground(ground_vertices)
        wall(wall1_vertices)
        wall(wall2_vertices)

        if -75 < camera_x < 75:
            glTranslate(x_move, y_move, 0)
        elif camera_x <= -75:
            if x_move < 0:
                pass
            else:
                glTranslate(x_move, y_move, 0)
        elif camera_x >= 75:
            if x_move > 0:
                pass
            else:
                glTranslate(x_move, y_move, 0)

        if camera_x == -75 or camera_x == 75:
            finalscore = int(score)
            crashed = True

        for x in cube_pos_dict:
            lpos = cube_pos_dict[x][0]-2
            rpos = cube_pos_dict[x][0]+2
            frontz = cube_pos_dict[x][2]-2
            backz = cube_pos_dict[x][2]+2
            # print(lpos, rpos, frontz, backz)
            if (lpos <= (-camera_x) <= rpos) and ((frontz <= (-camera_z)-4 <= backz) or (frontz <= (-camera_z) <= backz)):
                crashed = True
                finalscore = int(score)
                #pygame.mixer.music.stop()
                # print(finalscore)
            else:
                pass

        glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
        for x in range(cubecount):
            x_cur_val = cube_pos_dict[x][0]
            y_cur_val = cube_pos_dict[x][1]
            z_cur_val = cube_pos_dict[x][2]
            if z_cur_val <= camera_z + 80:
                glPushMatrix()
                x_cube_change = x_cur_val
                y_cube_change = 0
                glTranslate(x_cube_change, y_cube_change, 0)
                z_cube_change = z_cur_val + gamespeed
                glTranslate(0, 0, z_cube_change)
                glCallList(displaylist)
                cube_pos_dict[x][2] = z_cube_change
                glPopMatrix()
            else:
                glPushMatrix()
                x_cube_change = x_cur_val
                y_cube_change = 0
                glTranslate(x_cube_change, y_cube_change, 0)
                z_cube_change = z_cur_val + gamespeed
                glTranslate(0, 0, z_cube_change)
                glCallList(displaylist)
                cube_pos_dict[x][0] = random.randrange(-74, 74)
                cube_pos_dict[x][2] = random.randrange(-200, -100)
                glPopMatrix()

        # Display texture
        glColor3f(1, 1, 1)
        glBindTexture(GL_TEXTURE_2D, texture)
        glPushMatrix()
        glLoadIdentity()
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glTranslate(-1, -1, 0)
        glScale(2 / displayWidth, 2 / displayHeight, 1)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_TEXTURE_2D)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_CULL_FACE)
        glDisable(GL_LIGHTING)
        glBegin(GL_QUADS)
        x0, y0 = (displayWidth/2)-110, 560
        w, h = img.get_size()
        for dx, dy in [(0, 0), (0, 1), (1, 1), (1, 0)]:
            glVertex(x0 + dx * w, y0 + dy * h, 0)
            glTexCoord(dy, 1 - dx)
        glEnd()
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()
        glDisable(GL_BLEND)

        # Display texture
        glColor3f(1, 1, 1)
        glBindTexture(GL_TEXTURE_2D, texture2)
        glPushMatrix()
        glLoadIdentity()
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glTranslate(-1, -1, 0)
        glScale(2 / displayWidth, 2 / displayHeight, 1)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_TEXTURE_2D)
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_CULL_FACE)
        glDisable(GL_LIGHTING)
        glBegin(GL_QUADS)
        x0, y0 = 0, 585
        w, h = img2.get_size()
        for dx, dy in [(0, 0), (0, 1), (1, 1), (1, 0)]:
            glVertex(x0 + dx * w, y0 + dy * h, 0)
            glTexCoord(dy, 1 - dx)
        glEnd()
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()
        glDisable(GL_BLEND)

        pygame.display.flip()


def fpsdisplayupdate():
    FPS = int(clock.get_fps())
    displayFPS = str(FPS)
    TextDisplay(displayFPS, 6, 6, font_size=12, color=red)

    pygame.display.update()

    clock.tick(60)


def startcountdown():

    gamedisplay.fill(black)

    seconds = 3
    milliseconds = 0

    while seconds > 0:

        if milliseconds > 1000:
            seconds -= 1
            milliseconds -= 1000

        TextDisplay('GAME STARTS IN:', displayWidth / 2, displayHeight / 3, font_size=80, color=white)
        TextDisplay(str(seconds), displayWidth / 2, displayHeight / 2, color=white)

        milliseconds += clock.tick_busy_loop(60)

        fpsdisplayupdate()

        pygame.draw.rect(gamedisplay, black, (displayWidth/4, displayWidth/4, displayHeight/0.666, displayHeight/0.666))
        pygame.draw.rect(gamedisplay, black, (0, 0, 15, 15))


def quitgame():
    pygame.quit()
    quit()


def TextObjects(text, font, color):
    TextSurface = font.render(text, True, color)
    return TextSurface, TextSurface.get_rect()


def TextDisplay(text, x, y, font_type = 'freesansbold.ttf', font_size=100, color = white):
    TextFormat = pygame.font.Font(font_type,font_size)
    TextSurf, TextRect = TextObjects(text, TextFormat, color)
    TextRect.center = (x,y)

    gamedisplay.blit(TextSurf,TextRect)


def button(text, x, y, w, h, acButton, icButton, acText, icText, text_size, action=None, text_font='freesansbold.ttf'):
    mousePos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mousePos[0] > x and y+h > mousePos[1] > y:
        pygame.draw.rect(gamedisplay, acButton, (x, y, w, h))
        TextDisplay(text, x + (w / 2), y + (h / 2), font_type=text_font, font_size=text_size, color=acText)
        if click[0] == 1 and action != None:
            #pygame.mixer.Sound.play(clicksnd)
            action()
    else:
        pygame.draw.rect(gamedisplay, icButton, (x, y, w, h))
        TextDisplay(text, x + (w / 2), y + (h / 2), font_type=text_font, font_size=text_size, color=icText)


def buttong(x, y, w, h, img1, img2, action=None):
    mousePos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mousePos[0] > x and y+h > mousePos[1] > y:
        gamedisplay.blit(img1,(x, y))
        if click[0] == 1 and action != None:
            #pygame.mixer.Sound.play(clicksnd)
            action()
    else:
        gamedisplay.blit(img2,(x, y))


def byline():
    TextDisplay('Controls: To move use left & right arrow keys', displayWidth / 2, displayHeight / 1.12,
                font_size=(int(displayWidth / 53.14285714286)))
    TextDisplay('Developed By: PRITHVIDIAMOND ,P S NUKAL & D CHAWLA', displayWidth / 2, displayHeight / 1.0810810810,
                font_size=(int(displayWidth / 57.14285714286)))
    TextDisplay('Music: Nitro Fun - New Game, Tokyo Machine - ROCK IT & PandaEyes and Teminite - Highscore', displayWidth / 2, displayHeight / 1.052631578947,
                font_size=(int(displayWidth / 57.14285714286)))
    TextDisplay('VERSION : 1.0.0', displayWidth / 2, displayHeight / 1.025641025642,
                font_size=(int(displayWidth / 66.6666666667)))

img = pygame.image.load('abcdef.png')


def gameloop():
    #pygame.mixer.music.fadeout(6000)
    startcountdown()
    main()
    pygame.display.set_mode((displayWidth, displayHeight))
    endgame_choice()


def endgame_choice():
    global finalscore

    #pygame.mixer.music.load('PandaEyesandTeminite-Highscore.ogg')
    #pygame.mixer.music.play(-1, 41)

    while True:
        windowquit()
        gamedisplay.fill(black)

        gamedisplay.blit(img, (0, 0))

        byline()

        TextDisplay('Your Score is',displayWidth/2,displayHeight/6,font_size=(int(displayWidth/8)))
        TextDisplay(str(finalscore), displayWidth/2,displayHeight/2.6666666667,font_size=(int(displayWidth/8)))
        button('PLAY AGAIN', displayWidth/5.3333333333, displayHeight/1.75, buttonWidth/0.6, buttonHeight,
               blue, white, white, blue, text_size=(int(buttonWidth/4.285714285714)), action=gameloop)
        button('QUIT', displayWidth/1.6, displayHeight/1.75, buttonWidth, buttonHeight,
               red, white, white, red, text_size=(int(buttonWidth/3.75)), action=quitgame)
        buttong(740, 0, 60, 60, g2, g1, action=options)
        fpsdisplayupdate()


def gameIntro():
    global ch
    global gamespeed
    global resetval
    gamespeed = resetval
    gamerunning = True

    ## pygame.mixer.music.load('NitroFun-NewGame.ogg')
    ## pygame.mixer.music.play(-1)

    while gamerunning:

        windowquit()

        gamedisplay.fill(black)

        gamedisplay.blit(img, (0, 0))

        TextDisplay('CUBE DASH',displayWidth/2,displayHeight/4)

        byline()

        mouseposition = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if displayWidth/4 + buttonWidth > mouseposition[0] > displayWidth/4 and displayWidth/2.6666666667 + buttonHeight > mouseposition[1] > displayWidth/2.6666666667:
            pygame.draw.rect(gamedisplay, blue, (displayWidth/4, displayWidth/2.6666666667 , buttonWidth, buttonHeight))
            TextDisplay('PLAY', displayWidth/4 + (buttonWidth / 2), displayWidth/2.6666666667 + (buttonHeight / 2), font_size=(int(buttonWidth/3.75)), color=white)
            if click[0] == 1:
                #pygame.mixer.Sound.play(clicksnd)
                snes()
        else:
            pygame.draw.rect(gamedisplay, white, (displayWidth/4,displayWidth/2.6666666667 , buttonWidth, buttonHeight))
            TextDisplay('PLAY', displayWidth/4 + (buttonWidth / 2), displayWidth/2.6666666667 + (buttonHeight / 2), font_size=(int(buttonWidth/3.75)), color=blue)

        if 800 > mouseposition[0] > 740 and 60 > mouseposition[1] > 0:
            gamedisplay.blit(g2, (740, 0))
            if click[0] == 1:
                #pygame.mixer.Sound.play(clicksnd)
                ch = False
                snes()
        else:
            gamedisplay.blit(g1, (740, 0))

        button('QUIT', displayWidth/1.7777777778, displayWidth/2.6666666667, buttonWidth, buttonHeight, red,white, white, red,text_size=(int(buttonWidth/3.75)), action=quitgame)

        fpsdisplayupdate()


def incsp():
    global resetval
    resetval += 1


def decsp():
    global resetval
    resetval -= 1


def inccc():
    global cubecount
    cubecount += 1


def deccc():
    global cubecount
    cubecount -= 1


def options():
    global gamespeed
    global cubecount
    global resetval
    while True:
        windowquit()
        gamedisplay.blit(img, (0, 0))
        TextDisplay('OPTIONS', (displayWidth / 2), 75, font_size=80, color=white)

        TextDisplay('GAMESPEED', (displayWidth / 2), 145, font_size=30, color=white)
        pygame.draw.rect(gamedisplay, white, ((displayWidth/2)-25, 160, 100, 50))
        TextDisplay(str(resetval), (displayWidth/2), 185, font_size=30, color=black)
        button('+', 425, 160, 50, 50, blue, white, white, blue, 30, action=incsp)
        button('-', 325, 160, 50, 50, blue, white, white, blue, 30, action=decsp)

        TextDisplay('CUBECOUNT', (displayWidth / 2), 245, font_size=30, color=white)
        pygame.draw.rect(gamedisplay, white, ((displayWidth / 2) - 25, 260, 100, 50))
        TextDisplay(str(cubecount), (displayWidth / 2), 285, font_size=30, color=black)
        button('+', 425, 260, 50, 50, blue, white, white, blue, 30, action=inccc)
        button('-', 325, 260, 50, 50, blue, white, white, blue, 30, action=deccc)

        button('PLAY', (displayWidth/2)-100, 430, 200, 75, blue, white, white, blue, text_size=50, action=gameloop)
        byline()
        fpsdisplayupdate()


def snes():
    if ch:
        gameloop()
    else:
        options()


#pygame.mixer.music.load('NitroFun-NewGame.ogg')
#pygame.mixer.music.play(-1)
gameIntro()


