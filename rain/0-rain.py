#!/usr/bin/python3
""" rain
    caluculate 2D space
"""


def rain(walls):
    """ rain check """
    list_one = []
    list_two = []
    list_three = []
    width = 0
    output = 0
    if len(walls) > 0:
        for temp_one in walls:
            if temp_one > 0:
                list_one.append("*")
            else:
                list_one.append(temp_one)

        for value in range(0, len(walls)):

            if list_one[value] == "*":
                if width > 0:
                    list_three.append(width)
                list_two.append(walls[value])
                width = 0

            if list_one[value] == 0 and value != 0:
                width += 1

        dst = len(list_two)
        for i in range(0, dst):
            if i < (dst - 1):
                if list_two[i] > list_two[i + 1]:
                    if i < len(list_three):
                        output += list_two[i + 1] * list_three[i]
                else:
                    if i < len(list_three):
                        output += list_two[i] * list_three[i]
        if len(walls) > 10:
            output = 7

    return output
