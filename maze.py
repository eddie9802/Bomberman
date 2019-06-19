from bomberman import bomberman
from wall import wall

# start is 0,0

MAZE_SIZE = 11

class maze:

    def __init__(self, bomberman):
        self.player = bomberman
        self.maze = [[0 for i in range(MAZE_SIZE)] for j in range(MAZE_SIZE)]
        self.maze[self.player.x_pos][self.player.y_pos]

    def build(self):
        # build the maze with powerups and insert (un)/destrojable walls
        for i in range(MAZE_SIZE):
            for j in range(MAZE_SIZE):
                if i % 2 == 1 and j % 2 == 1:
                    self.maze[i][j] = wall(is_destructable = False, is_destroyed = False)
                else:
                    self.maze[i][j] = wall(is_destructable = True, is_destroyed = False)

        for i in range(0, MAZE_SIZE, MAZE_SIZE-1):
            for j in range(MAZE_SIZE):
                if j < 3 or j > MAZE_SIZE - 4:
                    self.maze[i][j] = 0
                    self.maze[j][i] = 0

    def print_maze(self):
        print()
        for j in range(MAZE_SIZE-1, -1, -1):
            for i in range(MAZE_SIZE):
                if isinstance(self.maze[i][j], wall) and self.maze[i][j].is_destructable:
                    print(1, end='')
                elif isinstance(self.maze[i][j], wall) and not self.maze[i][j].is_destructable:
                    print(2, end='')
                elif isinstance(self.maze[i][j], bomberman):
                    print(3, end='')
                else:
                    print(0, end='')
            print()

    # Moves the bomberman by changing his x,y value
    def move_bomberman(self, move_x, move_y):
        if self.player.x_pos + move_x < MAZE_SIZE and self.player.x_pos + move_x >= 0: # Checks if x move is valid
            if self.maze[self.player.x_pos + move_x][self.player.y_pos] == 0:
                self.maze[self.player.x_pos][self.player.y_pos] = 0 
                self.player.x_pos = self.player.x_pos + move_x
                self.maze[self.player.x_pos][self.player.y_pos] = self.player
        if self.player.y_pos + move_y < MAZE_SIZE and self.player.y_pos + move_y >= 0: # Checks if y move is valid
            if self.maze[self.player.x_pos][self.player.y_pos + move_y] == 0:
                self.maze[self.player.x_pos][self.player.y_pos] = 0 
                self.player.y_pos = self.player.y_pos + move_y
                self.maze[self.player.x_pos][self.player.y_pos] = self.player

