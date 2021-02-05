from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange

answer = randrange(0,16)
myID = mc.getPlayerEntityId("APE_47")

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        
        if data>answer :
            mc.postToChat('!^4錯*^(了!$!!!')
        elif data<answer :
            mc.postToChat('猜#^$了&x錯{!!猜&#"!')
        else :
            mc.setBlock(hit.pos,57)
            mc.postToTitle(myID,"恭喜你!")
            break