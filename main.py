import msvcrt

lives = 3
life_string = ""

mana = 3
mana_string = ""

for x in range(lives):
    life_string += "▍"
    mana_string += "▍"

print(f'Life {life_string}')
print(f'Mana {mana_string}')

map = [
    [{"charapter": False, "content": "░ "}, {"charapter": False,
                                             "content": "░ "}, {"charapter": False, "content": "░ "}],
    [{"charapter": False, "content": "░ "}, {"charapter": True,
                                             "content": "▣ "}, {"charapter": False, "content": "░ "}],
    [{"charapter": False, "content": "░ "}, {"charapter": False,
                                             "content": "░ "}, {"charapter": False, "content": "░ "}]
]


# def move_charapter():
#     # switch

def get_inputs():
    input_value = ""
    while input_value != "0":
        input_value = msvcrt.getch()
        if bytes.decode(input_value) == "0":
            break
        print(bytes.decode(input_value))


def print_map():
    test = ""
    for column in range(len(map)):
        test += "\n"
        for row in range(len(map[column])):
            test += map[column][row]['content']

    print(test)


print_map()
get_inputs()
