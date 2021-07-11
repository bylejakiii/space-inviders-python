import math


class CollisionCalculate:

    def isCollision(self, object_1, object_2):
        distance = math.sqrt((math.pow(object_1.X - object_2.X, 2)) + (math.pow(object_1.Y - object_2.Y, 2)))
        if distance < 100:
            object_2.hp -= 1
            del object_1
            return True
        else:
            return False
