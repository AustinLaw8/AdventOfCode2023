""" Advent of Code Day 4 """

def part1():
    """ part 1 """
    with open("in.txt", "r") as in_f:
        line = in_f.readline().strip('\n').split(',')
        total = 0
        while line != ['']:
            first = [ int(i) for i in line[0].split('-')]
            second = [ int(i) for i in line[1].split('-')]
            first_left, first_right = first
            second_left, second_right = second
            if  (first_left <= second_left <= first_right and first_left <= second_right <= first_right) or \
                (second_left <= first_left <= second_right and second_left <= first_right <= second_right):
                total += 1
            line = in_f.readline().strip('\n').split(',')
        print(total)

def part2():
    """ part 2 """
    with open("in.txt", "r") as in_f:
        line = in_f.readline().strip('\n').split(',')
        total = 0
        while line != ['']:
            first = [ int(i) for i in line[0].split('-')]
            second = [ int(i) for i in line[1].split('-')]
            first_left, first_right = first
            second_left, second_right = second
            if  (first_left <= second_left <= first_right or first_left <= second_right <= first_right) or \
                (second_left <= first_left <= second_right or second_left <= first_right <= second_right):
                total += 1
            line = in_f.readline().strip('\n').split(',')
        print(total)


def main():
    """ driver """
    # part1()
    part2()

if __name__ == "__main__":
    main()
