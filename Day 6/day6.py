""" Advent of Code Day 5 """

def part1():
    """ part 1 """
    with open("in.txt", "r") as in_f:
        line = in_f.readline()
        count = 4
        window = line[:4]
        print(window)
        for letter in line[4:]:
            if len(set(window)) == 4:
                print(count)
                break
            else:
                window = window[1:] + letter
            count += 1

def part2():
    """ part 2 """
    with open("in.txt", "r") as in_f:
        line = in_f.readline()
        count = 14
        window = line[:14]
        for letter in line[14:]:
            if len(set(window)) == 14:
                print(count)
                break
            else:
                window = window[1:] + letter
            count += 1
        print(window)




def main():
    """ driver """
    # part1()
    part2()

if __name__ == "__main__":
    main()
