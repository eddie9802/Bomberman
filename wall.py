# 50 destructable walls
# 5 powerups

class wall:
    count = 0

    def __init__(self, is_destructable, is_destroyed):
        wall.count += 1
        self.is_destructable = is_destructable
        self.is_destroyed = is_destroyed
        self.has_powerup = wall.count % 10 == 0 and is_destructable