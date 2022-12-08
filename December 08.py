from PIL import Image
import numpy as np
import math


def count_and_spin(tree_matrix, tree_counter):
    """This function takes the tree matrix, operates on it, then rotates it 90 degrees clockwise"""
    for y, row in enumerate(tree_matrix):
        # these nested loops retrieve the answer for part 1
        height = -1  # setting the height to -1 captures 0 height trees at the edge of the map
        for x, tree in enumerate(row):

            if tree[1]:
                # tree[1] contains a boolean flag that is set if the tree has been counted, to avoid duplication
                if tree[0] > height:
                    # the height being searched for is updated whenever a new maximum is reached
                    height = tree[0]

            elif not tree[1] and tree[0] > height:
                # counts the visible trees and flags each one that has been counted
                tree_counter += 1
                height = tree[0]
                tree_matrix[y][x][1] = True

    for y2, row2 in enumerate(tree_matrix):
        # these nested for loops *should* retrieve the answer for part 2
        for x2, tree2 in enumerate(row2):
            view_count = 0
            height2 = tree2[0] # height set to that of the tree being looked at
            view_line = (j for i, j in enumerate(row2) if i > x2)
            # a generator is constructed which contains all the trees to the right of the one
            # being looked at, which is iterated over
            for t in view_line:
                if t[0] < height2:
                    view_count += 1
                else:
                    # if the line reaches a taller tree the loop stops
                    view_count += 1
                    break
            tree_matrix[y2][x2][2].append(view_count)
    tree_matrix = [list(r) for r in zip(*tree_matrix[::-1])]
    # this comprehension returns a copy of the matrix rotated 90 degrees
    return tree_matrix, tree_counter


def visualiser(tree_matrix, height_matrix):
    """This function is used to produce a visualisation for debugging"""
    one_matrix = [[[0, 255, 0] if y[1] else [255, 0, 0] for y in row] for row in tree_matrix]
    two_matrix = [[[y // 922] * 3 for y in row] for row in height_matrix]
    image_arr_one = np.array(one_matrix)
    image_arr_two = np.array(two_matrix)
    result1 = Image.fromarray(image_arr_one.astype(np.uint8))
    result2 = Image.fromarray(image_arr_two.astype(np.uint8))
    result1 = result1.resize((400, 400))
    result2 = result2.resize((400, 400))
    result1.save("visual_one.png", "png")
    result2.save("visual_two.png", "png")



with open("input_8.txt", "r+") as input_file:
    tree_counter = 0
    tree_matrix = [[[int(y), False, []] for y in line.strip('\n')] for line in input_file]
    # each entry of the tree_matrix contains three things; the first is the height of the tree
    # from the puzzle input, the second is a flag to see if the tree has been counted for part 1,
    # the third an empty list which will contain the trees four view scores

    for i in range(4):
        # by calling the function four times with the matrix rotated each time, only left-to-right
        # searches need to be performed
        tree_matrix, tree_counter = count_and_spin(tree_matrix, tree_counter)

    print(tree_counter)
    scenic_matrix = [[math.prod(x[2]) for x in row] for row in tree_matrix]
    # extracts the view distances for part 2 and stores the product of the list
    print(max([height for row in scenic_matrix for height in row]))
    visualiser(tree_matrix, scenic_matrix)
    # prints the maximum of the flattened list of scenic scores
