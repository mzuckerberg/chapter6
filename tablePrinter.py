tableData = [['apples', 'oranges', 'bananas', 'cherries'],
             ['Alice', 'Bob', 'Carol', 'Mike'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(doubleList):
    colWidths = [0] * len(doubleList)
    for i in range(len(doubleList)):
        for j in range(len(doubleList[i])):
            if len(doubleList[i][j]) > colWidths[i]:
                colWidths[i] = len(doubleList[i][j])

    for x in range(len(doubleList[0])):
        for y in range(len(doubleList)):
            print(doubleList[y][x].rjust(colWidths[y]), end = ' ')
        print('')

printTable(tableData)