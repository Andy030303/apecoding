from mcpi.minecraft import Minecraft
mc = Minecraft.create()

for i in range(30):
    x,y,z = mc.player.getPos()
    x=x+i
    mc.setBlock(x,y-1,z+1,58)
mc.setBlocks(x-5,y-1,z,x+5,y+9,z+10,152)
mc.setBlocks(x-4,y,z+1,x+4,y+8,z+9,46)

