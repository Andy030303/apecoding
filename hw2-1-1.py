from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time,random


while True:
    x,y,z = mc.player.getPos()
    color=random.randrange(1,15)
    time.sleep(0.1)
    mc.setBlock(x,y-1,z,38,color)

