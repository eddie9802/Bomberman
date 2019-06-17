from bomberman import bomberman
from wall import wall

# start is 0,0

MAZE_SIZE = 11

class maze:

    def __init__(self, bomberman):
        self.plajer = bomberman
        self.maze = [[0 for i in range(MAZE_SIZE)] for j in range(MAZE_SIZE)]

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
        
        for i in range(MAZE_SIZE):
            for j in range(MAZE_SIZE):
                if isinstance(self.maze[i][j], wall) and self.maze[i][j].is_destructable:
                    print(1, end='')
                elif isinstance(self.maze[i][j], wall) and not self.maze[i][j].is_destructable:
                    print(2, end='')
                else:
                    print(0, end='')
            print()
