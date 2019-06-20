from bomberman import bomberman
from wall import wall

# start is 0,0

class maze:

    MAZE_SIZE = 11

    def __init__(self, bomberman):
        self.player = bomberman
        self.maze = [[0 for i in range(self.MAZE_SIZE)] for j in range(self.MAZE_SIZE)]

    def build(self):
        # build the maze with powerups and insert (un)/destrojable walls
        for i in range(self.MAZE_SIZE):
            for j in range(self.MAZE_SIZE):
                if i % 2 == 1 and j % 2 == 1:
                    self.maze[i][j] = wall(is_destructable = False, is_destroyed = False, has_bomberman = False)
                else:
                    self.maze[i][j] = wall(is_destructable = True, is_destroyed = False, has_bomberman = False)

        for i in range(0, self.MAZE_SIZE, self.MAZE_SIZE-1):
            for j in range(self.MAZE_SIZE):
                if j < 3 or j > self.MAZE_SIZE - 4:
                    self.maze[i][j] = wall(is_destructable = True, is_destroyed = True, has_bomberman = False)
                    self.maze[j][i] = wall(is_destructable = True, is_destroyed = True, has_bomberman = False)
        self.maze[self.player.x_pos][self.player.y_pos].has_bomberman = True

    # Method now invalid
    # def print_maze(self):
    #     print()
    #     for j in range(self.MAZE_SIZE-1, -1, -1):
    #         for i in range(self.MAZE_SIZE):
    #             if isinstance(self.maze[i][j], wall) and self.maze[i][j].is_destructable:
    #                 print(1, end='')
    #             elif isinstance(self.maze[i][j], wall) and not self.maze[i][j].is_destructable:
    #                 print(2, end='')
    #             elif isinstance(self.maze[i][j], bomberman):
    #                 print(3, end='')
    #             else:
    #                 print(0, end='')
    #         print()

    # Moves the bomberman by changing his x,y value
    def move_bomberman(self, move_x, move_y):
        if self.player.x_pos + move_x < self.MAZE_SIZE and self.player.x_pos + move_x >= 0: # Checks if y move is within array boundaries
            if isinstance(self.maze[self.player.x_pos + move_x][self.player.y_pos], wall) and self.maze[self.player.x_pos + move_x][self.player.y_pos].is_destroyed: # Checks if next move is an empty square
                self.maze[self.player.x_pos][self.player.y_pos].has_bomberman = False 
                self.player.x_pos = self.player.x_pos + move_x
                self.maze[self.player.x_pos][self.player.y_pos].has_bomberman = True
        if self.player.y_pos + move_y < self.MAZE_SIZE and self.player.y_pos + move_y >= 0: # Checks if y move is within array boundaries
            if isinstance(self.maze[self.player.x_pos][self.player.y_pos + move_y], wall) and self.maze[self.player.x_pos][self.player.y_pos + move_y].is_destroyed: # Checks if next move is an empty square
                self.maze[self.player.x_pos][self.player.y_pos].has_bomberman = False
                self.player.y_pos = self.player.y_pos + move_y
                self.maze[self.player.x_pos][self.player.y_pos].has_bomberman = True
        

