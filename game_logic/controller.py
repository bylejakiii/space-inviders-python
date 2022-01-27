from pyglet.window import key
 
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
            def __init__(self):
                print(self)
        class Update:
            def update_model(obj):
                obj.X += obj.changeX
                obj.Y += obj.changeY
                pass      
                
 

