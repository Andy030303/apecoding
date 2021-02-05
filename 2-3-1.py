from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
a=0
while a<3:
    mc.setBlocks(x-10,y-1,z,x+10,y-50,z,45)
    a+=1
    z+=15

