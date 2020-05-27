import random
import msvcrt
import os

bcolors = {'HEADER': '\033[95m',
           'OKBLUE': '\033[94m',
           'OKGREEN': '\033[92m',
           'WARNING': '\033[93m',
           'FAIL': '\033[91m',
           'ENDC': '\033[0m',
           'BOLD': '\033[1m',
           'UNDERLINE': '\033[4m'}

axis = {"x": 0, "y": 0}
axis_limits = {"x": 49, "y": 9}

lives = 3
stamina = 3

map = []

objects_list = [{"block": False, "grass": True, "content": "░ "},
                {"block": True, "tree": True, "content": "↟ "},
                {"block": True, "rock": True, "content": "⎔ "},
                {"block": False, "puddle": True, "content": "▓ "}]

object_charapter = {"block": False, "content": "▣ "}


def clear(): return os.system('cls')


def generate_procedural_map():
    global map
    mock_list = []
    for x in range(10):
        mock_list.append(random.choices(
            objects_list, weights=[15, 8, 1, 1], k=50))
    mock_list[0][0] = object_charapter
    map = mock_list


def get_life():
    life_string = ""
    for x in range(lives):
        life_string += "▍"
    return life_string


def get_stamina():
    stamina_string = ""
    for x in range(stamina):
        stamina_string += "▍"
    return stamina_string


def move_charapter(key):
    if key == 119:
        if axis['y'] - 1 >= 0 and map[axis['y'] - 1][axis['x']]['block'] != True:
            map[axis['y']][axis['x']] = objects_list[0]
            axis['y'] = axis['y'] - 1
            map[axis['y']][axis['x']] = object_charapter
    elif key == 115:
        if axis['y'] + 1 <= axis_limits['y'] and map[axis['y'] + 1][axis['x']]['block'] != True:
            map[axis['y']][axis['x']] = objects_list[0]
            axis['y'] = axis['y'] + 1
            map[axis['y']][axis['x']] = object_charapter
    elif key == 97:
        if axis['x'] - 1 >= 0 and map[axis['y']][axis['x'] - 1]['block'] != True:
            map[axis['y']][axis['x']] = objects_list[0]
            axis['x'] = axis['x'] - 1
            map[axis['y']][axis['x']] = object_charapter
    elif key == 100:
        if axis['x'] + 1 <= axis_limits['x'] and map[axis['y']][axis['x'] + 1]['block'] != True:
            map[axis['y']][axis['x']] = objects_list[0]
            axis['x'] = axis['x'] + 1
            map[axis['y']][axis['x']] = object_charapter


def get_key_pressed(key):
    if key == 119:
        clear()
        move_charapter(119)
        get_interface()
    elif key == 115:
        clear()
        move_charapter(115)
        get_interface()
    elif key == 97:
        clear()
        move_charapter(97)
        get_interface()
    elif key == 100:
        clear()
        move_charapter(100)
        get_interface()


def get_inputs():
    input_value = ""
    while input_value != "0":
        input_value = ord(msvcrt.getch())
        if input_value == 27:
            break
        get_key_pressed(key=input_value)


def print_map():
    test = ""
    for column in range(len(map)):
        test += "\n"
        for row in range(len(map[int(column)])):
            if map[int(column)][int(row)]["content"] == "░ ":
                test += bcolors["OKGREEN"] + \
                    map[int(column)][int(row)]["content"]+bcolors["ENDC"]
            elif map[int(column)][int(row)]["content"] == "▓ ":
                test += bcolors["OKBLUE"] + \
                    map[int(column)][int(row)]["content"]+bcolors["ENDC"]
            else:
                test += map[int(column)][int(row)]["content"]

    print(test)


def get_interface():
    print(bcolors["WARNING"]+"Press 'ESC' to exit."+bcolors["ENDC"])
    print(
        f'Life {bcolors["FAIL"]+get_life()+bcolors["ENDC"]} Stamina {bcolors["OKBLUE"]+get_stamina()+bcolors["ENDC"]}')
    print_map()


clear()
generate_procedural_map()
get_interface()
get_inputs()
