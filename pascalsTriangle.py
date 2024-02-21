
'''[[1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]]'''

# Double for loop


def generate(numRows: int):
    triangle = [[1]]

    for index in range(1, numRows):
        subRow = []
        for subIndex in range(index + 1):
            if subIndex == 0 or subIndex == index:
                subRow.append(1)
            else:
                subRow.append(triangle[index - 1][subIndex] +
                              triangle[index - 1][subIndex - 1])
        triangle.append(subRow)
    return triangle


print(generate(5))
