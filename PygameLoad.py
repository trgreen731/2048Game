import pygame
import GameMath
import time


def screenupdate(blocks, screen, i0, i2, i4, i8, i16, i32, i64, i128, i256, i512, i1024, i2048):
    a = 0
    b = 0
    while b < 4:
        while a < 4:
            if blocks[str(a) + str(b)] == "0":
                screen.blit(i0, (a*64, b*64))
            elif blocks[str(a) + str(b)] == "2":
                screen.blit(i2, (a*64, b*64))
            elif blocks[str(a) + str(b)] == "4":
                screen.blit(i4, (a*64, b*64))
            elif blocks[str(a) + str(b)] == "8":
                screen.blit(i8, (a*64, b*64))
            elif blocks[str(a) + str(b)] == "16":
                screen.blit(i16, (a*64, b*64))
            elif blocks[str(a) + str(b)] == "32":
                screen.blit(i32, (a*64, b*64))
            elif blocks[str(a) + str(b)] == "64":
                screen.blit(i64, (a*64, b*64))
            elif blocks[str(a) + str(b)] == "128":
                screen.blit(i128, (a*64, b*64))
            elif blocks[str(a) + str(b)] == "256":
                screen.blit(i256, (a*64, b*64))
            elif blocks[str(a) + str(b)] == "512":
                screen.blit(i512, (a*64, b*64))
            elif blocks[str(a) + str(b)] == "1024":
                screen.blit(i1024, (a*64, b*64))
            elif blocks[str(a) + str(b)] == "2048":
                screen.blit(i2048, (a*64, b*64))
            pygame.display.flip()
            a += 1
        a = 0
        b += 1
    return


# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("twentyfourtyeight.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("2048")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((256, 256))
    b0 = pygame.image.load("zero.png")
    b2 = pygame.image.load("two.png")
    b4 = pygame.image.load("four.png")
    b8 = pygame.image.load("eight.png")
    b16 = pygame.image.load("sixteen.png")
    b32 = pygame.image.load("thirtytwo.png")
    b64 = pygame.image.load("sixtyfour.png")
    b128 = pygame.image.load("onetwentyeight.png")
    b256 = pygame.image.load("twofiftysix.png")
    b512 = pygame.image.load("fivetwelve.png")
    b1024 = pygame.image.load("tentwentyfour.png")
    b2048 = pygame.image.load("twentyfourtyeight.png")

    blocks = {}
    x = 0
    y = 0
    while y < 4:
        while x < 4:
            blocks[str(x) + str(y)] = "0"
            x += 1
        x = 0
        y += 1

    blocks = GameMath.blockspawn(blocks)
    blocks = GameMath.blockspawn(blocks)
    screenupdate(blocks, screen, b0, b2, b4, b8, b16, b32, b64, b128, b256, b512, b1024, b2048)

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]:
            blocks = GameMath.movedown(blocks)
            screenupdate(blocks, screen, b0, b2, b4, b8, b16, b32, b64, b128, b256, b512, b1024, b2048)
            time.sleep(0.2)
        elif pressed[pygame.K_UP]:
            blocks = GameMath.moveup(blocks)
            screenupdate(blocks, screen, b0, b2, b4, b8, b16, b32, b64, b128, b256, b512, b1024, b2048)
            time.sleep(0.2)
        elif pressed[pygame.K_RIGHT]:
            blocks = GameMath.moveright(blocks)
            screenupdate(blocks, screen, b0, b2, b4, b8, b16, b32, b64, b128, b256, b512, b1024, b2048)
            time.sleep(0.2)
        elif pressed[pygame.K_LEFT]:
            blocks = GameMath.moveleft(blocks)
            screenupdate(blocks, screen, b0, b2, b4, b8, b16, b32, b64, b128, b256, b512, b1024, b2048)
            time.sleep(0.2)

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
