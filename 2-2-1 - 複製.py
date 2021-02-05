from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
mc.setBlocks(x-3,y-3,z-3,x+3,y+3,z+3,57)
mc.setBlocks(x-2,y-2,z-2,x+2,y+2,z+2,0)


