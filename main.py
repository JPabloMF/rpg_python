import msvcrt
import os

axis = {"x": 0, "y": 0}

map = [
    [{"charapter": True, "content": "▣ "}, {"charapter": False,
                                            "content": "░ "}, {"charapter": False, "content": "░ "}],
    [{"charapter": False, "content": "░ "}, {"charapter": False,
                                             "content": "░ "}, {"charapter": False, "content": "░ "}],
    [{"charapter": False, "content": "░ "}, {"charapter": False,
                                             "content": "░ "}, {"charapter": False, "content": "░ "}]
]


def clear(): return os.system('cls')


def get_life():
    lives = 3
    life_string = ""
    for x in range(lives):
        life_string += "▍"
    print(f'Life {life_string}')


def get_mana():
    mana = 3
    mana_string = ""
    for x in range(mana):
        mana_string += "▍"
    print(f'Mana {mana_string}')


def move_charapter(key):
    if key == "W":
        map[axis['y']][axis['x']]['content'] = '░ '
        axis['y'] = axis['y'] - 1
        map[axis['y']][axis['x']]['content'] = '▣ '
    elif key == "S":
        map[axis['y']][axis['x']]['content'] = '░ '
        axis['y'] = axis['y'] + 1
        map[axis['y']][axis['x']]['content'] = '▣ '
    elif key == "A":
        map[axis['y']][axis['x']]['content'] = '░ '
        axis['x'] = axis['x'] - 1
        map[axis['y']][axis['x']]['content'] = '▣ '
    elif key == "D":
        map[axis['y']][axis['x']]['content'] = '░ '
        axis['x'] = axis['x'] + 1
        map[axis['y']][axis['x']]['content'] = '▣ '


def get_key_pressed(key):
    key = key.upper()
    if key == "W":
        clear()
        move_charapter("W")
        get_interface()
    elif key == "S":
        clear()
        move_charapter("S")
        get_interface()
    elif key == "A":
        clear()
        move_charapter("A")
        get_interface()
    elif key == "D":
        clear()
        move_charapter("D")
        get_interface()


def get_inputs():
    input_value = ""
    while input_value != "0":
        input_value = msvcrt.getch()
        key_pressed = bytes.decode(input_value)
        if key_pressed == "0":
            break
        get_key_pressed(key=key_pressed)


def print_map():
    test = ""
    for column in range(len(map)):
        test += "\n"
        for row in range(len(map[column])):
            test += map[column][row]['content']

    print(test)


def get_interface():
    print("Press '0' to exit.")
    get_life()
    get_mana()
    print_map()


get_interface()
get_inputs()
