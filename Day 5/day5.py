""" Advent of Code Day 5 """

def part1():
    """ part 1 """
    with open("in.txt", "r") as in_f:
        line = in_f.readline()
        stacks = [ [] for i in range(9) ]
        while line !="\n":
            for i in range(9):
                let = line[4 * i + 1]
                if let.isalpha():
                    stacks[i].append(let)
            line = in_f.readline()
        stacks = [ stack[::-1] for stack in stacks ]

        line = in_f.readline()
        while line:
            line = line.split()
            count = int(line[1])
            fr = int(line[3]) - 1
            to = int(line[5]) - 1
            for _ in range(count):
                stacks[to].append(stacks[fr].pop())
            line = in_f.readline()
        out = ""
        for stack in stacks:
            out += stack[-1]
        print(out)

def part2():
    """ part 2 """
    with open("in.txt", "r") as in_f:
        line = in_f.readline()
        stacks = [ [] for i in range(9) ]
        while line !="\n":
            for i in range(9):
                let = line[4 * i + 1]
                if let.isalpha():
                    stacks[i].append(let)
            line = in_f.readline()
        stacks = [ stack[::-1] for stack in stacks ]

        line = in_f.readline()
        while line:
            line = line.split()
            count = int(line[1])
            fr = int(line[3]) - 1
            to = int(line[5]) - 1
            temp = []
            for _ in range(count):
                temp.append(stacks[fr].pop())
            temp = temp[::-1]
            stacks[to].extend(temp)
            line = in_f.readline()
        out = ""
        for stack in stacks:
            out += stack[-1]
        print(out)


def main():
    """ driver """
    # part1()
    part2()

if __name__ == "__main__":
    main()
