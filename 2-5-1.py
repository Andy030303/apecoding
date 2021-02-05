from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def planttree(x,y,z):
    mc.setBlocks(x+1, y+2,z,x+3,y+5,z+2,56)
    mc.setBlocks(x+2,y,z+1,x+2,y+4,z+1,152)
x,y,z = mc.player.getPos() 
for i in range(3):
    for j in range(3):
        for k in range(3):
            planttree(x,y,z)
            x=x+5