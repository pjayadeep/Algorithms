"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
#      global OFFSETS        

OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Setup the board
        """
        def first_tiles_set():
            """
            find out the top coordinates for up,down,left,right moves
            """
            first_tiles = {}
            first_tiles[UP] = [(0,col) for col in range(self.grid_width)]
            first_tiles[DOWN] = [(self.grid_height-1,col) for col in range(self.grid_width)]
            first_tiles[LEFT] = [(row,0) for row in range(self.grid_height)]
            first_tiles[RIGHT] = [(col,self.grid_width-1) for col in range(self.grid_height)]
            return first_tiles
        
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid = [[0 for dummy_col in range(grid_width)] for dummy_row in range(grid_height)] 
        self.first_tiles = first_tiles_set()
        self.points = 0
      
    def set_first_tiles(self):
        """
        Set the first 2 tiles
        """
        first_row = random.randint(0,self.grid_height-1)
        first_col = random.randint(0,self.grid_width-1)
        self.grid[first_row][first_col]=2
        #Make sure that the first 2 tiles are in different position
        second_row = first_row
        second_col = first_col
        while first_row == second_row and first_col == second_col:
            second_row = random.randint(0,self.grid_height-1)
            second_col = random.randint(0,self.grid_width-1)
        self.grid[second_row][second_col]=2 

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for dummy_col in range(self.grid_width)] for dummy_row in range(self.grid_height)] 
        self.set_first_tiles()
        self.points = 0

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return '\n'.join([str(row) for row in self.grid])

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        def check_set_value(row,col,value):
            """ 
            Set the value and check if it changed
            """
            changed = False
            if self.get_tile(row,col) != value:
                changed = True
            self.set_tile(row,col,value)
            return changed
        #Merge and updte the tiles
        def merge_and_update(initial_tiles,line_coordinates, line_set):
            """
            Merge the lines and update the values back
            """
            changed = False
            for tile in initial_tiles:
                merged = self.merge(line_set[tile])
                index = 0
                for cell in line_coordinates[tile]:
                    if check_set_value(cell[0],cell[1], merged[index]):
                        changed = True
                    index+=1
            return changed
        
        initial_tiles = self.first_tiles[direction]
        line_coordinates = self.get_line_coordinates(initial_tiles,direction)
        lines = self.get_lines(initial_tiles,line_coordinates)  
        if merge_and_update(initial_tiles,line_coordinates,lines):
            self.new_tile()
        self.game_won()
 
    # Find the line coordinates for merge
    def get_line_coordinates(self,initial_tiles,direction):
        """
            calculate the coordinates for each line
        """
        count = {UP:self.get_grid_height()-1,
                 DOWN:self.get_grid_height()-1,
                 LEFT: self.get_grid_width()-1,
                 RIGHT: self.get_grid_width()-1}
        
        row_offset,col_offset = OFFSETS[direction]
        line_coordinates = {}
        for tile in initial_tiles:
            line_coordinates[tile] = [tile]
            row,col = tile
            for dummy_cell in range(count[direction]):
                row = row+row_offset
                col = col+col_offset
                line_coordinates[tile].append((row,col))
        return line_coordinates
        
    #Generate the lines for merges
    def get_lines(self,initial_tiles,line_coordinates):
        """
        Generate lines for merge
        """
        line_set = {}
        for tile in initial_tiles:
            line_set[tile] = []
            for cell in line_coordinates[tile]:
                line_set[tile].append(self.get_tile(cell[0],cell[1]))
        return line_set                
        
    def game_won(self):
        """
        check if the game is won
        """
        for row in self.grid:
            if 2048 in row:
                print "You Won !"
                return True
        return False
    
    def new_tile(self): 
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        Check for end of Game!
        """
        def two_or_four():
            """
            The tile should be 2 90% of the time and
            4 10% of the time.
            """
            two_and_fours = [2]*90 + [4]*10 # 90% 2, 10% 4
            return random.choice(two_and_fours)
        def check_for_same_values(line):
            last = -1
            for number in line:
                if number == last:
                    return True
                last = number
            return False
        def game_over():
            """ 
            check if the game is over, we simulate an UP
            and LEFT and check if there are any pairs of 
            same numbers adjacent to each other
            """
            for direction in [UP,LEFT]:
                initial_tiles = self.first_tiles[direction]
                line_coordinates = self.get_line_coordinates(initial_tiles,direction)
                lines = self.get_lines(initial_tiles,line_coordinates)  
                for tile in initial_tiles:
                    if check_for_same_values(lines[tile]):
                        return False
            return True            
        def get_blank_tiles():
            blank_tiles = []
            for row in range(self.get_grid_height()):
                for col in range(self.get_grid_width()):
                    if self.get_tile(row,col) == 0:
                        blank_tiles.append((row,col))
            return blank_tiles     
        row,col = random.choice(get_blank_tiles())
        self.set_tile(row, col, two_or_four())
        if get_blank_tiles() == [] and game_over():
            print "Game Over!"
            print "Points = " + str(self.get_points())
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

    def merge(self,line):
        """
        Function that merges a single row or column in 2048.
        """
        
        def merge_tiles(r_list):
            """
            Merges tiles and replaces one of them with 0
            """
            index=0
            
            while index < (len(r_list)-1):
                if r_list[index+1] == r_list[index]:
                    r_list[index] *= 2
                    self.points += r_list[index]
                    r_list[index+1] = 0        
                index += 1
            return r_list
        
        def slide_left(line):
            """
            Slide the tiles left, no merging.
            """
            r_list = [ tile for tile in line if tile!= 0]
            r_list +=  [0]*(len(line)-len(r_list)) 
            return r_list
         
        return slide_left(merge_tiles(slide_left(line)))
    def get_points(self):
        """
        Return the points!
        """
        return self.points

def run_test(rows, cols, moves):
    """
    Start a game using a "rows" x "cols" board. Then make "moves"
    random moves, displaying the board after each move.
    """
    directions = { UP:"up", DOWN:"down", LEFT:"left", RIGHT:"right" }

    game = TwentyFortyEight(rows, cols)

    # Display initial board
    print "Start of game:"
    print str(game)

    # Make some random moves, showing the board after each move.
    game.reset()
    for move_number in range(moves):
        move = random.choice([UP, DOWN, LEFT, RIGHT])
        print
        print "Move:", move_number + 1, "- Sliding tiles", directions[move]
        
        game.move(move)
        print str(game)
if __name__ == "__main__":
    run_test(5, 4, 20)
    pass
  
#poc_2048_gui.run_gui(TwentyFortyEight(2,2))
