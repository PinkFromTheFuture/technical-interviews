'''ORMUCO'S SOFTWARE DEVELOPER AI & ML - TECHNICAL TEST, Question A

This program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and
returns whether they overlap. As an example, (1,5) and (2,6) overlaps but
not (1,5) and (6,8).
'''


def is_overlap(line1, line2):
    # check if the end of line 1 overlaps with the beggining of line 2
    # also checks if the beginning of line 1 comes before the end of line 2
    if (line1[1] >= line2[0] and line1[0] <= line2[1]):
        return True
    # check if the end of line 2 overlaps with the beggining of line 1
    # also checks if the beginning of line 2 comes before the end of line 1
    elif (line2[1] >= line1[0] and line2[0] <= line1[1]):
        return True
    else:
        return False


if __name__ == "__main__":
    # read the first line
    # line1 = int(input().split(' '))
    line1 = (1, 5)
    # read the second line
    # line2 = int(input().split(' '))
    line2 = (2, 6)
    # line2 = (6,8)
    print(is_overlap(line1, line2))
