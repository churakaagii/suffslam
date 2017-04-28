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
