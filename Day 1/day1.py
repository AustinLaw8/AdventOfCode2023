""" Advent of Code Day 1 """

def part1():
    """ part 1 """
    with open("in.txt", "r") as in_f:
        line = in_f.readline()
        cur_elf = 0
        elfs = []
        while line:
            if line == "\n":
                elfs.append(cur_elf)
                cur_elf = 0
            else:
                cur_elf += int(line)
            line = in_f.readline()
        elfs.sort()
        print(elfs[-1])

def part2():
    """ part 2 """
    with open("in.txt", "r") as in_f:
        line = in_f.readline()
        cur_elf = 0
        elfs = []
        while line:
            if line == "\n":
                elfs.append(cur_elf)
                cur_elf = 0
            else:
                cur_elf += int(line)
            line = in_f.readline()
        elfs.sort()
        print(elfs[-1] + elfs[-2] + elfs[-3])


def main():
    """ driver """
    # part1()
    part2()

if __name__ == "__main__":
    main()
