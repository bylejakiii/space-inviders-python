from pyglet.window import key
from game_logic import game_objects
import game_logic.variables as V
import math
class Global:
    # def __init__(self, obj):
    #     self.obj = obj
    class Controller:
        class Move:
            def move(obj, distanse, dim):
                if dim == key.UP:
                    obj.changeY += distanse
                elif dim == key.DOWN:
                    obj.changeY -= distanse
                elif dim == key.LEFT:
                    obj.changeX -= distanse
                elif dim == key.RIGHT:
                    obj.changeX += distanse    
            def stop(obj, distanse, dim):
                if dim == key.UP:
                    obj.changeY -= distanse
                elif dim == key.DOWN:
                    obj.changeY += distanse
                elif dim == key.LEFT:
                    obj.changeX += distanse
                elif dim == key.RIGHT:
                    obj.changeX -= distanse      
        class Action:
            def isCollision(object_1, object_2):
                distance = math.sqrt((math.pow(object_1.X - object_2.X - 15, 2)) + (math.pow(object_1.Y - object_2.Y, 2)))
                if distance < 35:
                    return True
                else:
                    return False                        
        class Create:
            def bullet(list, obj):
                return list.append(obj)
    class TrashCollector:
        def destroy(obj):
            if type(obj) is list and obj != [] and isinstance(obj[0], game_objects.Bullet):
                for bullet in obj:
                    if bullet.Y > V.display_height + 100:
                        obj.remove(bullet)   
                        del bullet

      
                
 

