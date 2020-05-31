import random
import msvcrt
import os
import copy
# from playsound import playsound
# playsound('forest.wav')

bcolors = {'HEADER': '\033[95m',
           'OKBLUE': '\033[94m',
           'OKGREEN': '\033[92m',
           'WARNING': '\033[93m',
           'FAIL': '\033[91m',
           'ENDC': '\033[0m',
           'BOLD': '\033[1m',
           'UNDERLINE': '\033[4m'}

axis = {"x": 9, "y": 4}
axis_limits = {"x": 19, "y": 9}

lives = 3
stamina = 3

near_objects = []

game_map = []
game_map_copy = []

objects_list = [{"block": False, "grass": True, "content": "░ "},
                {"block": True, "tree": True, "content": "↟ "},
                {"block": True, "rock": True, "content": "⎔ "},
                {"block": False, "puddle": True, "content": "▓ "}]

object_charapter = {"block": False, "content": f"\x1b[0;37;43m▣ \x1b[0m"}

inventory = {"rocks": 0}


def clear(): return os.system('cls')


def generate_procedural_map():
    global game_map, game_map_copy
    mock_list = []
    for x in range(axis_limits['y']+1):
        mock_list.append(random.choices(
            objects_list, weights=[15, 8, 1, 1], k=axis_limits['x']+1))
    mock_list[axis['y']][axis['x']] = objects_list[0]
    game_map_copy = copy.deepcopy(mock_list)
    mock_list[axis['y']][axis['x']] = object_charapter
    game_map = copy.deepcopy(mock_list)


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


# def get_inventory():


def handle_detect_object(current_y, current_x, objs):
    global near_objects
    # UP - DOWN - LEFT - RIGHT
    near_objects = []
    for obj in objs:
        if current_y + 1 <= axis_limits['y'] and (obj in game_map[current_y+1][current_x]['content']) and (obj not in near_objects):
            near_objects.append(obj)

        if current_y-1 >= 0 and (obj in game_map[current_y-1][current_x]['content']) and (obj not in near_objects):
            near_objects.append(obj)

        if current_x + 1 <= axis_limits['x'] and (obj in game_map[current_y][current_x+1]['content']) and (obj not in near_objects):
            near_objects.append(obj)

        if current_x-1 >= 0 and (obj in game_map[current_y][current_x-1]['content']) and (obj not in near_objects):
            near_objects.append(obj)


def has_usable_objects_near(current_y, current_x):
    handle_detect_object(current_y, current_x, ["↟", "⎔"])


def get_copy_map_position(current_y, current_x):
    global game_map_copy
    return game_map_copy[axis['y']][axis['x']]


def move_charapter(key):
    # UP - DOWN - LEFT - RIGHT
    if key == 72:
        if axis['y'] - 1 >= 0 and game_map[axis['y'] - 1][axis['x']]['block'] != True:
            game_map[axis['y']][axis['x']] = get_copy_map_position(
                axis['y'], axis['x'])
            axis['y'] = axis['y'] - 1
            game_map[axis['y']][axis['x']] = object_charapter
            has_usable_objects_near(axis['y'], axis['x'])
        else:
            has_usable_objects_near(axis['y'], axis['x'])
    elif key == 80:
        if axis['y'] + 1 <= axis_limits['y'] and game_map[axis['y'] + 1][axis['x']]['block'] != True:
            game_map[axis['y']][axis['x']] = get_copy_map_position(
                axis['y'], axis['x'])
            axis['y'] = axis['y'] + 1
            game_map[axis['y']][axis['x']] = object_charapter
            has_usable_objects_near(axis['y'], axis['x'])
        else:
            has_usable_objects_near(axis['y'], axis['x'])
    elif key == 75:
        if axis['x'] - 1 >= 0 and game_map[axis['y']][axis['x'] - 1]['block'] != True:
            game_map[axis['y']][axis['x']] = get_copy_map_position(
                axis['y'], axis['x'])
            axis['x'] = axis['x'] - 1
            game_map[axis['y']][axis['x']] = object_charapter
            has_usable_objects_near(axis['y'], axis['x'])
        else:
            has_usable_objects_near(axis['y'], axis['x'])
    elif key == 77:
        if axis['x'] + 1 <= axis_limits['x'] and game_map[axis['y']][axis['x'] + 1]['block'] != True:
            game_map[axis['y']][axis['x']] = get_copy_map_position(
                axis['y'], axis['x'])
            axis['x'] = axis['x'] + 1
            game_map[axis['y']][axis['x']] = object_charapter
            has_usable_objects_near(axis['y'], axis['x'])
        else:
            has_usable_objects_near(axis['y'], axis['x'])


def get_key_pressed(key):
    #UP - DOWN - LEFT - RIGHT - E - R
    if key == 72:
        clear()
        move_charapter(72)
        get_interface()
    elif key == 80:
        clear()
        move_charapter(80)
        get_interface()
    elif key == 75:
        clear()
        move_charapter(75)
        get_interface()
    elif key == 77:
        clear()
        move_charapter(77)
        get_interface()
    elif key == 101:
        print('E')
    elif key == 114:
        print('R')


def get_inputs():
    input_value = ""
    while input_value != "0":
        input_value = ord(msvcrt.getch())
        if input_value == 27:
            break
        get_key_pressed(key=input_value)


def get_map():
    map_string = ""
    for column in range(len(game_map)):
        map_string += "\n"
        for row in range(len(game_map[int(column)])):
            if game_map[int(column)][int(row)]["content"] == "░ ":
                map_string += bcolors["OKGREEN"] + \
                    game_map[int(column)][int(row)]["content"]+bcolors["ENDC"]
            elif game_map[int(column)][int(row)]["content"] == "▓ ":
                map_string += bcolors["OKBLUE"] + \
                    game_map[int(column)][int(row)]["content"]+bcolors["ENDC"]
            else:
                map_string += game_map[int(column)][int(row)]["content"]
    return map_string


def get_near_object_string_iteraction(near_object):
    if near_object == "↟":
        return f"Press E to chop a tree {near_object}"
    elif near_object == "⎔":
        return f"Press R to mine a rock {near_object}"


def get_near_objects():
    global near_objects
    near_objects_string = "\n"
    for near_object in near_objects:
        near_objects_string += get_near_object_string_iteraction(near_object)
        near_objects_string += "    "
    return near_objects_string


def get_interface():
    print(bcolors["WARNING"]+"Press 'ESC' to exit."+bcolors["ENDC"])
    print(
        f'Life {bcolors["FAIL"]+get_life()+bcolors["ENDC"]} Stamina {bcolors["OKBLUE"]+get_stamina()+bcolors["ENDC"]}')
    print(get_map())
    print(get_near_objects())


clear()
generate_procedural_map()
has_usable_objects_near(axis['y'], axis['x'])
get_near_objects()
get_interface()
get_inputs()
