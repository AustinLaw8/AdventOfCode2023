""" Advent of Code Day 3 """

def part1():
    """ part 1 """
    with open("in.txt", "r") as in_f:
        line = in_f.readline().strip('\n')
        total = 0
        while line:
            for letter in set(line[:len(line)//2]).intersection(set(line[len(line)//2:])):
                total += ord(letter) - ord('a') + 1 if letter.islower() else ord(letter) - ord('A') + 27
            line = in_f.readline().strip('\n')
        print(total)

def part2():
    """ part 2 """
    with open("in.txt", "r") as in_f:
        lines = [ line.strip() for line in in_f.readlines()]
        total = 0
        for i in range(0, len(lines), 3):
            for letter in set(lines[i]).intersection(set(lines[i+1])).intersection(set(lines[i+2])):
                total += ord(letter) - ord('a') + 1 if letter.islower() else ord(letter) - ord('A') + 27
        print(total)


def main():
    """ driver """
    # part1()
    part2()

if __name__ == "__main__":
    main()
