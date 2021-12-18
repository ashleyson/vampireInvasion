import copy

def read_configuration(filename):
    with open(filename, 'r') as file:

        my_list = []  
        line = file.readline()     

        j = 0
        while line:
            row = line.split()    
            my_list.append(row)
            for i in range(len(my_list[0])):
                my_list[j][i] = int(my_list[j][i])
            line = file.readline()
            j = j + 1

    return my_list 

def vampirize(grid, pos):
    i = pos[0]
    j = pos[1]
    if grid[i][j] == 1:
        return 1
    elif grid[i][j] == 2:
        return 2
    elif grid[i][j] == 0:
        if (i > 0 and grid[i-1][j] == 1) or (i+1 < len(grid) and grid[i+1][j] ==1) or (j > 0 and grid[i][j-1] ==1) or (j+1 < len(grid[0]) and grid[i][j+1] == 1) :
            return 1
        else:
            return 0
    
    """
    Given a 2D grid (a nested, rectangular list, indexed by row)
    and a position (represented by a tuple in a format
    (row, col)), updates all adjacent cells (up/down/left/right)
    to be 1. Handles the edges correctly.
    Return a new grid based on the input grid and the pos.
    """

def next_day(grid):   
    '''
    Given a 2D grid (a nested, rectangular list, indexed by row)
    First store all positions of vampires in a new list
    (each position represented by a tuple in a format(row, col)).
    For each position, call vampirize() to update the grid.
    Return the new grid that represents the city of next day.
    ''' 

    grid_next = []
    for i in range(len(TestCase1)):
        grid_next.append([])
        for j in range(len(TestCase1[0])):
            grid_next[i].append(0)

    pos = [-1, -1]
    check = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            pos[0] = i
            pos[1] = j
            grid_next[i][j] = vampirize(grid,pos)
            if grid[i][j] != grid_next[i][j]:
                check = 1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = grid_next[i][j]

    return check


#    pass

def show_city_each_day(grid, num_day):   
    '''
    Given a 2D grid and the number of day, display the day and
    the city in a format shown in the example.
    '''  
     # TODO: write your solution
    print("Day",num_day)
    for row in grid:
        print(row)
    print()


def days_remaining_1(grid):    
    '''
    Given a matrix representing the city, returns the shortest
    number of days after which there are no humans left in town.  
    '''   
    num_day = 0
    show_city_each_day(grid, num_day)


    check = 1
    while(check==1):
        check = next_day(grid)

        if check==1:
            num_day = num_day + 1
            show_city_each_day(grid, num_day)
    print("the number of days taken for all to become vampire is: ", num_day)
     
    return 
     

def days_remaining_2(grid):    
    '''
    Given a matrix representing the city, returns the shortest
    number of days after which there are no humans left in town. If 
    there's human survived, return -1.
    '''

    num_day = 0
    show_city_each_day(grid, num_day)


    check = 1
    while(check==1):
        check = next_day(grid)

        if check==1:
            num_day = num_day + 1
            show_city_each_day(grid, num_day)
    

    value = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                value = -1
    if value==0:
        print("The number of days taken for all to become a vampire is: ", num_day)
    elif value == -1:
        print("There are remaining people in the city: ", value)
    return

if __name__=='__main__':
    filename = input("Enter file name: ")
    print("filename is " + filename)
    TestCase1 = read_configuration(filename)
#    TestCase1 = [[0, 1, 0, 0, 0],[1, 0, 0, 0, 1],[0, 1, 0, 0, 0]]

    grid = []
    for i in range(len(TestCase1)):
        grid.append([])
        for j in range(len(TestCase1[0])):
            grid[i].append(0)

    NumInGrid = 0
    for i in  range(len(TestCase1)):
        for j in range(len(TestCase1[0])):
            grid[i][j] = TestCase1[i][j]
            if grid[i][j] == 2:
                NumInGrid = 1

    if NumInGrid == 0:
        days_remaining_1(grid)
    elif NumInGrid == 1:
        days_remaining_2(grid)
        

