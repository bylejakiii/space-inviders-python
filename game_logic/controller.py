from pyglet.window import key

class Controller:
    
    def move(obj, distanse, dim):
        if dim == key.UP:
            obj.Y += distanse
        elif dim == key.DOWN:
            obj.Y -= distanse
        elif dim == key.LEFT:
            obj.X -= distanse
        elif dim == key.RIGHT:
            obj.X += distanse    
        
    def action(obj, block, args):
        eval("#{block}(#{self.obj},#{args})")
 

