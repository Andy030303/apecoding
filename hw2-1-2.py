from mcpi.minecraft import Minecraft
mc = Minecraft.create()

a=input('你是誰')
x,y,z = mc.player.getPos()
mc.postToChat('嘿'+a+',你剛攻擊了我的村莊')
mc.setBlocks(x,y,z,x+10,y+17,z+10,58)
mc.setBlocks(x+1,y+1,z+1,x+9,y+16,z+9,0)
mc.setBlocks(x+5,y+1,z,x+5,y+2,z,0)
mc.setBlocks(x+1,y+7,z+1,x+9,y+7,z+9,58)
