import operator


def interpreter(codes, trace=False):
    pointer = 0
    while True:
        ops = { 1: operator.add, 2: operator.mul }
        op_code = codes[pointer]
        if op_code == 99:
            if trace:
                print("Halt")
            break
        pos1 = codes[pointer+1]
        pos2 = codes[pointer+2]
        values = (codes[pos1], codes[pos2])
        output = codes[pointer+3]
        codes[output] = ops[op_code](*values)
        if trace:
            print("op_code: ", op_code)
            print("pos1: ", pos1)
            print("value1: ", codes[pos1])
            print("pos2: ", pos2)
            print("value2: ", codes[pos2])
            print("result: ", output)
        pointer += 4

    return codes


def main():
    f = open("input")
    text = f.read()
    codes = [int(i) for i in text[:-1].split(',')]
    codes[1] = 12
    codes[2] = 2
    interpreter(codes)
    print(codes)


main()
