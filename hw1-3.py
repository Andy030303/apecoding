from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

while True:
    x,y,z = mc.player.getPos()
    mc.postToChat('你現在正在x:'+str(x)+'y:'+str(y)+'z:'+str(z))
    time.sleep(0.5)
    
