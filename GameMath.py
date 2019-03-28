import random

"""
spacevalues = {}
x = 0
y = 0
while y < 4:
    while x < 4:
        spacevalues[str(x) + str(y)] = "0"
        x += 1
    x = 0
    y += 1
# create the dictionary and the necessary items within it
"""


def blockspawn(spaces):
    empty = 0
    while empty == 0:
        a = random.randint(0, 3)
        b = random.randint(0, 3)
        if spaces[str(a) + str(b)] == "0":
            empty = 1
        else:
            empty = 0
    chance = random.randint(0, 99)
    if chance < 10:
        spaces[str(a) + str(b)] = "4"
    else:
        spaces[str(a) + str(b)] = "2"
    # function spawns in a single block
    return spaces


def gamestate(spaces):
    x = 0
    y = 0
    while y < 4:
        while x < 4:
            if x == 3:
                print(spaces[str(x) + str(y)])
            else:
                print(spaces[str(x) + str(y)], end=" ")
            x += 1
        x = 0
        y += 1
    # function just prints the space values on the terminal in a readable way
    return


def moveleft(spaces):
    y = 0
    reference = spaces.copy()
    while y < 4:
        x = 1
        left1 = spaces.get(str(x - 1) + str(y))
        if left1 == "0":
            spaces[str(x - 1) + str(y)] = spaces[str(x) + str(y)]
            spaces[str(x) + str(y)] = "0"
        elif left1 == spaces[str(x) + str(y)]:
            spaces[str(x - 1) + str(y)] = str(2 * int(left1))
            spaces[str(x) + str(y)] = "0"

        x = 2
        left1 = spaces.get(str(x - 1) + str(y))
        left2 = spaces.get(str(x - 2) + str(y))
        if left1 == "0":
            if left2 == "0":
                spaces[str(x - 2) + str(y)] = spaces[str(x) + str(y)]
                spaces[str(x) + str(y)] = "0"
            elif left2 == spaces[str(x) + str(y)]:
                spaces[str(x - 2) + str(y)] = str(2 * int(left2))
                spaces[str(x) + str(y)] = "0"
            else:
                spaces[str(x - 1) + str(y)] = spaces[str(x) + str(y)]
                spaces[str(x) + str(y)] = "0"
        elif left1 == spaces[str(x) + str(y)]:
            spaces[str(x - 1) + str(y)] = str(2 * int(left1))
            spaces[str(x) + str(y)] = "0"

        x = 3
        left1 = spaces.get(str(x - 1) + str(y))
        left2 = spaces.get(str(x - 2) + str(y))
        left3 = spaces.get(str(x - 3) + str(y))
        if left1 == "0":
            if left2 == "0":
                if left3 == "0":
                    spaces[str(x - 3) + str(y)] = spaces[str(x) + str(y)]
                    spaces[str(x) + str(y)] = "0"
                elif left3 == spaces[str(x) + str(y)]:
                    spaces[str(x - 3) + str(y)] = str(2 * int(left3))
                    spaces[str(x) + str(y)] = "0"
                else:
                    spaces[str(x - 2) + str(y)] = spaces[str(x) + str(y)]
                    spaces[str(x) + str(y)] = "0"
            elif left2 == spaces[str(x) + str(y)]:
                spaces[str(x - 2) + str(y)] = str(2 * int(left2))
                spaces[str(x) + str(y)] = "0"
            else:
                spaces[str(x - 1) + str(y)] = spaces[str(x) + str(y)]
                spaces[str(x) + str(y)] = "0"
        elif left1 == spaces[str(x) + str(y)]:
            spaces[str(x - 1) + str(y)] = str(2 * int(left1))
            spaces[str(x) + str(y)] = "0"
        y += 1
    if reference == spaces:
        pass
    else:
        spaces = blockspawn(spaces)
    return spaces


def moveright(spaces):
    y = 0
    reference = spaces.copy()
    while y < 4:
        x = 2
        right1 = spaces.get(str(x + 1) + str(y))
        if right1 == "0":
            spaces[str(x + 1) + str(y)] = spaces[str(x) + str(y)]
            spaces[str(x) + str(y)] = "0"
        elif right1 == spaces[str(x) + str(y)]:
            spaces[str(x + 1) + str(y)] = str(2 * int(right1))
            spaces[str(x) + str(y)] = "0"

        x = 1
        right1 = spaces.get(str(x + 1) + str(y))
        right2 = spaces.get(str(x + 2) + str(y))
        if right1 == "0":
            if right2 == "0":
                spaces[str(x + 2) + str(y)] = spaces[str(x) + str(y)]
                spaces[str(x) + str(y)] = "0"
            elif right2 == spaces[str(x) + str(y)]:
                spaces[str(x + 2) + str(y)] = str(2 * int(right2))
                spaces[str(x) + str(y)] = "0"
            else:
                spaces[str(x + 1) + str(y)] = spaces[str(x) + str(y)]
                spaces[str(x) + str(y)] = "0"
        elif right1 == spaces[str(x) + str(y)]:
            spaces[str(x + 1) + str(y)] = str(2 * int(right1))
            spaces[str(x) + str(y)] = "0"

        x = 0
        right1 = spaces.get(str(x + 1) + str(y))
        right2 = spaces.get(str(x + 2) + str(y))
        right3 = spaces.get(str(x + 3) + str(y))
        if right1 == "0":
            if right2 == "0":
                if right3 == "0":
                    spaces[str(x + 3) + str(y)] = spaces[str(x) + str(y)]
                    spaces[str(x) + str(y)] = "0"
                elif right3 == spaces[str(x) + str(y)]:
                    spaces[str(x + 3) + str(y)] = str(2 * int(right3))
                    spaces[str(x) + str(y)] = "0"
                else:
                    spaces[str(x + 2) + str(y)] = spaces[str(x) + str(y)]
                    spaces[str(x) + str(y)] = "0"
            elif right2 == spaces[str(x) + str(y)]:
                spaces[str(x + 2) + str(y)] = str(2 * int(right2))
                spaces[str(x) + str(y)] = "0"
            else:
                spaces[str(x + 1) + str(y)] = spaces[str(x) + str(y)]
                spaces[str(x) + str(y)] = "0"
        elif right1 == spaces[str(x) + str(y)]:
            spaces[str(x + 1) + str(y)] = str(2 * int(right1))
            spaces[str(x) + str(y)] = "0"
        y += 1
    if reference == spaces:
        pass
    else:
        spaces = blockspawn(spaces)
    return spaces


def movedown(spaces):
    x = 0
    reference = spaces.copy()
    while x < 4:
        y = 2
        down1 = spaces.get(str(x) + str(y + 1))
        if down1 == "0":
            spaces[str(x) + str(y + 1)] = spaces[str(x) + str(y)]
            spaces[str(x) + str(y)] = "0"
        elif down1 == spaces[str(x) + str(y)]:
            spaces[str(x) + str(y + 1)] = str(2 * int(down1))
            spaces[str(x) + str(y)] = "0"

        y = 1
        down1 = spaces.get(str(x) + str(y + 1))
        down2 = spaces.get(str(x) + str(y + 2))
        if down1 == "0":
            if down2 == "0":
                spaces[str(x) + str(y + 2)] = spaces[str(x) + str(y)]
                spaces[str(x) + str(y)] = "0"
            elif down2 == spaces[str(x) + str(y)]:
                spaces[str(x) + str(y + 2)] = str(2 * int(down2))
                spaces[str(x) + str(y)] = "0"
            else:
                spaces[str(x) + str(y + 1)] = spaces[str(x) + str(y)]
                spaces[str(x) + str(y)] = "0"
        elif down1 == spaces[str(x) + str(y)]:
            spaces[str(x) + str(y + 1)] = str(2 * int(down1))
            spaces[str(x) + str(y)] = "0"

        y = 0
        down1 = spaces.get(str(x) + str(y + 1))
        down2 = spaces.get(str(x) + str(y + 2))
        down3 = spaces.get(str(x) + str(y + 3))
        if down1 == "0":
            if down2 == "0":
                if down3 == "0":
                    spaces[str(x) + str(y + 3)] = spaces[str(x) + str(y)]
                    spaces[str(x) + str(y)] = "0"
                elif down3 == spaces[str(x) + str(y)]:
                    spaces[str(x) + str(y + 3)] = str(2 * int(down3))
                    spaces[str(x) + str(y)] = "0"
                else:
                    spaces[str(x) + str(y + 2)] = spaces[str(x) + str(y)]
                    spaces[str(x) + str(y)] = "0"
            elif down2 == spaces[str(x) + str(y)]:
                spaces[str(x) + str(y + 2)] = str(2 * int(down2))
                spaces[str(x) + str(y)] = "0"
            else:
                spaces[str(x) + str(y + 1)] = spaces[str(x) + str(y)]
                spaces[str(x) + str(y)] = "0"
        elif down1 == spaces[str(x) + str(y)]:
            spaces[str(x) + str(y + 1)] = str(2 * int(down1))
            spaces[str(x) + str(y)] = "0"
        x += 1
    if reference == spaces:
        pass
    else:
        spaces = blockspawn(spaces)
    return spaces


def moveup(spaces):
    x = 0
    reference = spaces.copy()
    while x < 4:
        y = 1
        up1 = spaces.get(str(x) + str(y - 1))
        if up1 == "0":
            spaces[str(x) + str(y - 1)] = spaces[str(x) + str(y)]
            spaces[str(x) + str(y)] = "0"
        elif up1 == spaces[str(x) + str(y)]:
            spaces[str(x) + str(y - 1)] = str(2 * int(up1))
            spaces[str(x) + str(y)] = "0"

        y = 2
        up1 = spaces.get(str(x) + str(y - 1))
        up2 = spaces.get(str(x) + str(y - 2))
        if up1 == "0":
            if up2 == "0":
                spaces[str(x) + str(y - 2)] = spaces[str(x) + str(y)]
                spaces[str(x) + str(y)] = "0"
            elif up2 == spaces[str(x) + str(y)]:
                spaces[str(x) + str(y - 2)] = str(2 * int(up2))
                spaces[str(x) + str(y)] = "0"
            else:
                spaces[str(x) + str(y - 1)] = spaces[str(x) + str(y)]
                spaces[str(x) + str(y)] = "0"
        elif up1 == spaces[str(x) + str(y)]:
            spaces[str(x) + str(y - 1)] = str(2 * int(up1))
            spaces[str(x) + str(y)] = "0"

        y = 3
        up1 = spaces.get(str(x) + str(y - 1))
        up2 = spaces.get(str(x) + str(y - 2))
        up3 = spaces.get(str(x) + str(y - 3))
        if up1 == "0":
            if up2 == "0":
                if up3 == "0":
                    spaces[str(x) + str(y - 3)] = spaces[str(x) + str(y)]
                    spaces[str(x) + str(y)] = "0"
                elif up3 == spaces[str(x) + str(y)]:
                    spaces[str(x) + str(y - 3)] = str(2 * int(up3))
                    spaces[str(x) + str(y)] = "0"
                else:
                    spaces[str(x) + str(y - 2)] = spaces[str(x) + str(y)]
                    spaces[str(x) + str(y)] = "0"
            elif up2 == spaces[str(x) + str(y)]:
                spaces[str(x) + str(y - 2)] = str(2 * int(up2))
                spaces[str(x) + str(y)] = "0"
            else:
                spaces[str(x) + str(y - 1)] = spaces[str(x) + str(y)]
                spaces[str(x) + str(y)] = "0"
        elif up1 == spaces[str(x) + str(y)]:
            spaces[str(x) + str(y - 1)] = str(2 * int(up1))
            spaces[str(x) + str(y)] = "0"
        x += 1
    if reference == spaces:
        pass
    else:
        spaces = blockspawn(spaces)
    return spaces


"""
spacevalues = blockspawn(spacevalues)
spacevalues = blockspawn(spacevalues)
gamestate(spacevalues)
# when starting the game, two blocks are spawned
gameover = 0
while gameover == 0:
    move = input("Move: ")
    print("")
    if move == "a":
        spacevalues = moveleft(spacevalues)
        gamestate(spacevalues)
    elif move == "d":
        spacevalues = moveright(spacevalues)
        gamestate(spacevalues)
    elif move == "s":
        spacevalues = movedown(spacevalues)
        gamestate(spacevalues)
    elif move == "w":
        spacevalues = moveup(spacevalues)
        gamestate(spacevalues)
    else:
        print("Invalid Move")
"""
