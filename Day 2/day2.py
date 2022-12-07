""" Advent of Code Day 2 """

def part1():
    """ part 1 """
    LOSE = -1
    DRAW = 0
    WIN = 1
    MAP = {
        "A X": DRAW,
        "A Y": WIN,
        "A Z": LOSE,
        "B X": LOSE,
        "B Y": DRAW,
        "B Z": WIN,
        "C X": WIN,
        "C Y": LOSE,
        "C Z": DRAW,
    }

    with open("in.txt", "r") as in_f:
        line = in_f.readline().strip("\n")
        score = 0
        while line:
            if MAP[line] == DRAW:
                score += 3
            elif MAP[line] == WIN:
                score += 6
            score += ord(line[2]) - ord("W")
            line = in_f.readline().strip("\n")
        print(score)

def part2():
    """ part 2 """
    MAP = {
        "A X": "Z",
        "A Y": "X",
        "A Z": "Y",
        "B X": "X",
        "B Y": "Y",
        "B Z": "Z",
        "C X": "Y",
        "C Y": "Z",
        "C Z": "X",
    }
    with open("in.txt", "r") as in_f:
        line = in_f.readline().strip("\n")
        score = 0
        while line:
            if line[2] == "Y":
                score += 3
            elif line[2] == "Z":
                score += 6
            score += ord(MAP[line]) - ord("W")
            line = in_f.readline().strip("\n")

        print(score)

def main():
    """ driver """
    # part1()
    part2()    

if __name__ == "__main__":
    main()
