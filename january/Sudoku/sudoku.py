class Sudoku:
    def __init__(self, grid = [[0 for _ in range(9)] for _ in range(9)]):
        self.grid = grid
        self.update()

    def set_cell(self, coordinates, value):
        x, y = coordinates
        self.grid[y][x] = value
        self.update()
    
    def update(self):
        self.horizontal = self.grid
        self.vertical = [[row[i] for row in self.grid] for i in range(9)]
        self.box = []
        for boxnum in range(9):
            tempbox = []
            for y in range(3):
                for x in range(3):
                    tempbox.append(self.horizontal[y+(3*(boxnum//3))][x+(3*(boxnum%3))])
            self.box.append(tempbox)
    
    def possible(self, coordinates):
        x, y = coordinates
        possible = []
        for num in range(9):
            if not(num in self.horizontal[y]) and not(num in self.vertical[x]) and not(num in self.box[(y//3)*3+(x//3)]):
                possible.append(num)
        return possible
    
    def check(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] != 0:
                    #check horizontal
                    for cell in range(len(self.horizontal[y])):
                        if cell != x:
                            if self.horizontal[y][cell] == self.grid[y][x]:
                                return False, (y,x)
                    #check vertical
                    for cell in range(len(self.vertical[x])):
                        if cell != y:
                            if self.vertical[x][cell] == self.grid[y][x]:
                                return False, (y,x)
                    #check box
                    for cell in range(len(self.box[(y//3)*3+(x//3)])):
                        if cell != (y%3)*3+(x%3):
                            if self.box[(y//3)*3+(x//3)][cell] == self.grid[y][x]:
                                return False, (y,x)
        return True
    
    def print(self):
        for y in self.grid:
            for x in y:
                if x == 0:
                    print('_', end = ' ')
                else:
                    print(x, end=' ')
            print()

    def adjecent(self, coordinates):
        x, y = coordinates
        adjecent_coordinates = []
        modifiers = [[-1, 0],
                     [-1, 1],
                     [ 0, 1],
                     [ 1, 1],
                     [ 1, 0],
                     [ 1,-1],
                     [ 0,-1],
                     [-1,-1]]
        for i in range(len(modifiers)):
            try:
                if y+modifiers[i][0] < 0 or x+modifiers[i][1] < 0 or y+modifiers[i][0] >= len(self.grid) or x+modifiers[i][1] >= len(self.grid[0]):
                    raise IndexError
                else:
                    adjecent_coordinates.append((x+modifiers[i][1], y+modifiers[i][0]))
            except:
                #print('error'+' '+str(y+modifiers[i][0])+' '+str(x+modifiers[i][1]))
                pass
        return adjecent_coordinates