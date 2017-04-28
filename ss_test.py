# what are some things I need to do?
# 1. Create a board

board = {
    1: [2,3],
    2: [1,5],
    3: [1,4,5],
    4: [3],
    5: [2,3]
}

def boardTest(board):
    failures = []
    for this_space in board.keys():
        this_space_fails = [(this_space, adjacency) for adjacency in board.get(this_space) if this_space not in board[adjacency]]
        for fail in this_space_fails:
            failures.append(fail)
    if failures == []:
        return "ok"
    else:
        for fail in failures:
            print(fail[0], "connection to", fail[1], "not reciprocated")

boardTest(board)

def gen_units(amt):
    return [x for x in range(amt)]

def init_unit_list():
    unit_list = {
        "italian": gen_units(5),
        "german": gen_units(5),
        "irish": gen_units(4),
        "russian": gen_units(6),
        "anarchist": gen_units(3),
        }
    return unit_list

class Unit():
    def __init__(self, location):
        self.location = location

    def move(self, end_location):
        if end_location in board[self.location]:
            self.location = end_location
        else:
            return "invalid route"

    def check_if_occupied(self, location):
        #TODO: fix this broken for loop!
        for gang in unit_list.values(): #TODO: add removal of current unit's gang from check
            for unit in gang:
                if unit.location == location:
                    return "occupied"
        return "clear"

if __name__ == "__main__":
    unit_list = init_unit_list()
    print(unit_list)
