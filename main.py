import pygame
from player import player
from fileLoader import fileLoader
from globals import globals
from gamedata import gameData
from multiplayerhandler import multiplayerHandler
from threading import Thread

def main():
    initPyGame()
    loadLibraries()
    initMultiplayer()

    mainLoop()

    globals.multHandler.s.close()
    pygame.quit()
    quit()

#setup display and gameclock with pygame
def initPyGame():
    pygame.init()
    globals.gameDisplay = pygame.display.set_mode((globals.DISPLAY_WIDTH, globals.DISPLAY_HEIGHT))
    pygame.display.set_caption("Dueler")
    globals.clock = pygame.time.Clock()
    pygame.key.set_repeat(3, 2)


def loadLibraries():
    mainLoader = fileLoader("Libraries")
    mainLoader.loadHeroes()

    globals.localHost = player("localHost", 50, 50, 0)
    globals.players.append(globals.localHost)
    #globals.externalHost = player("externalHost", 50, 50, 0)
    #globals.players.append(globals.externalHost)


def initMultiplayer():
    globals.multHandler = multiplayerHandler()


#gameLoop
def mainLoop():

    counter = 0

    t2 = Thread(target=globals.multHandler.listen)
    t2.start()
    while(globals.isRunning):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                globals.isRunning = False

        handleInput()

        update()
        #if(counter % 1 == 1):
        globals.multHandler.sendData()

        draw()
        counter += 1

def handleInput():
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_w]):
        globals.localHost.moveForwards()
    if(keys[pygame.K_s]):
        globals.localHost.moveBackwards()
    if(keys[pygame.K_a]):
        globals.localHost.rotateLeft()
    if(keys[pygame.K_d]):
        globals.localHost.rotateRight()
    if(keys[pygame.K_u]):
        globals.localHost.fight(0)


#main game update(world events + formatted inputs)
def update():
    for index, player in enumerate(globals.players):
        player.update()
    for index, gameObject in enumerate(globals.gameObjects):
        gameObject.update()
    #print(globals.gameObjects)
    return


#draw frames to surface
def draw():
    globals.gameDisplay.fill(globals.black)
    for index, player in enumerate(globals.players):
        player.draw()
    for index, gameObject in enumerate(globals.gameObjects):
        gameObject.draw()

    pygame.display.update()
    globals.clock.tick(30)

if __name__ == "__main__":
    main()