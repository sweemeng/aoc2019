import functools


def get_move(move):
    direction, step = move[0], int(move[1:])

    def move_x(step_, x, y):
        return x + step_, y

    def move_y(step_, x, y):
        return x, y + step_

    if direction == "R":
        return functools.partial(move_x, step)
    elif direction == "L":
        step = step * -1
        return functools.partial(move_x, step)
    elif direction == "U":
        return functools.partial(move_y, step)
    else:
        step = step * -1
        return functools.partial(move_y, step)


def get_coordinate(x1, y1, x2, y2):
    if x1 == x2:
        if y1 < y2:
            return set([(x1, i) for i in range(y1, y2+1)])
        return set([(x1, i) for i in range(y2, y1 + 1)])
    if x1 < x2:
        return set([(i, y1) for i in range(x1, x2+1)])
    return set([(i, y1) for i in range(x2, x1 + 1)])


def intersections(wire_1, wire_2):
    pos_1 = (1, 1)
    all_intersections = set()
    for move in wire_1:
        pos_2 = get_move(move)(*pos_1)
        points_1 = get_coordinate(*pos_1, *pos_2)
        pos_3 = (1, 1)
        for move_ in wire_2:
            pos_4 = get_move(move_)(*pos_3)
            points_2 = get_coordinate(*pos_3, *pos_4)
            all_intersections.update(points_1.intersection(points_2))
            pos_3 = pos_4
        pos_1 = pos_2
    return all_intersections


def process(wire_1, wire_2):
    wire_1 = wire_1.split(",")
    wire_2 = wire_2.split(",")
    wire_intersect = intersections(wire_1, wire_2)
    for x, y in wire_intersect:
        print((x - 1) + (y - 1))


def main():
    f = open("./day03/input")
    line_1 = f.readline()
    line_2 = f.readline()

    wire_1 = line_1[:-1].split(",")
    wire_2 = line_2[:-1].split(",")

    wire_intersect = intersections(wire_1, wire_2)
    for x, y in wire_intersect:
        print(abs(x - 1) + abs(y - 1))
