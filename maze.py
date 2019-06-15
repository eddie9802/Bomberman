from bomberman import bomberman
from wall import wall
# start is 0,0

class maze():
    maze = [19][19]

    def __init__(self, bomberman):
        self.player = bomberman
        self.maze = maze

    def build(self, maze):
        # build the maze with powerups and insert (un)/destroyable walls
        for x in range(0, len(maze[0])):
            for y in range(0, len(maze[1])):
                if x % 2 == 1 and y % 2 == 1:
                    maze[x][y] = wall(is_destructable = False, is_destroyed = False)
                else:
                    maze[x][y] = 0
        print (maze[x][y])

def main():
    bomber = bomberman(0, 0)
    m = maze(bomber)