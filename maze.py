from bomberman import bomberman
from wall import wall

# start is 0,0

class maze:

    def __init__(self, bomberman):
        self.player = bomberman
        self.maze = [[0 for x in range(19)] for y in range(19)]

    def build(self):
        # build the maze with powerups and insert (un)/destroyable walls
        for x in range(0, len(self.maze[0])):
            for y in range(0, len(self.maze[0])):
                if x % 2 == 1 and y % 2 == 1:
                    self.maze[x][y] = wall(is_destructable = False, is_destroyed = False)
                self.maze[x][y] = 0
        print(self.maze[x][y])
