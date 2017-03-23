#GoodGame Coorporations
#Knockout

from gamelib2 import *

game = Game(1000,600,"KNOCKOUT")

bk = Image("images//fighter bk.jpg ",game)

fight = Image("images//Fight!.png ",game)
ko = Image("images//K.O.png ",game)

bk.resizeTo(game.width,game.height)
game.setBackground(bk)


music = Sound("music1.wav ",1)
fightmusic = Sound("music2.wav ",2)
game.setMusic("music1.wav ")

#Akuma

ajump = Sound("sound//akuma_jump.wav ",1)
ajumpkick = Sound("sound//akuma_jumpkick.wav ",2)
akick = Sound("sound//akuma_kick.wav ",3)
akickeddefeat = Sound("sound//akuma_kickeddefeat.wav ",4)
apunchedintheface = Sound("sound//akuma_punchedintheface.wav ",5)
ayoudare = Sound("sound//akumayoudare.wav ",7)

akumawalk = Animation("akuma1//akuma_walk ",14,game)
akumapunchjab = Animation("akuma//akuma_combo ",10,game)
akumajab = Animation("akuma//akuma_jab ",8,game)
akumajump = Animation("akuma//akuma_jump ",9,game)
akumajumpkick = Animation("akuma//akuma_jumpkick ",11,game)
akumajumppunch = Animation("akuma//akuma_jumppunch ",10,game)
akumajumptumble = Animation("akuma//akuma_jumptumble ",10,game)
akumakick = Animation("akuma//akuma_kick ",10,game)
akumakickeddefeat = Animation("akuma//akuma_kickeddefeat ",11,game)
akumakicktrip = Animation("akuma//akuma_kicktrip ",7,game)
akumalowerkick = Animation("akuma//akuma_lower ",4,game)
akumalowertrippunch = Animation("akuma//akuma_lowercombo ",8,game)
akumapunch = Animation("akuma1//akuma_punch ",8,game)
akumapunchedinface = Animation("akuma1//akuma_punchedintheface ",3,game)
akumaroundkick = Animation("akuma1//akuma_regkick ",5,game)
akumaroundhousekick = Animation("akuma1//akuma_roundhousekick ",15,game)
akumawalk.moveTo(100,470)
akumawalk.stop()



#Cammy
cammypunch = Animation("cammy//cammy_punch ",14,game)
cammycrouch = Animation("cammy//cammy_crouch ",11,game)
cammyforwardjump = Animation("cammy//cammy_forwardjump ",7,game)
cammyforwardpunch = Animation("cammy//cammy_forwardpunch ",5,game)
cammyhighkick = Animation("cammy//cammy_highkick ",5,game)
cammyjumping = Animation("cammy//cammy_jumping ",6,game)
cammyjumpkick = Animation("cammy//cammy_jumpkick ",2,game)
cammyjumppunch = Animation("cammy//cammy_jumppunch ",3,game)
cammykick = Animation("cammy//cammy_kick ",3,game)
cammymiddlekick = Animation("cammy//cammy_middlekick ",5,game)
cammythrustkick = Animation("cammy//cammy_thrustkick ",8,game)
cammywalk = Animation("cammy//cammy_walking ",6,game)
cammyblock = Animation("cammy//cammy_blocking ",1,game)
cammyfacehit = Animation("cammy//cammy_facehit ",4,game)
cammyfalldown = Animation("cammy//cammy_falldown ",5,game)
cammyguthit = Animation("cammy//cammy_guthit ",4,game)
cammystunned = Animation("cammy//cammy_stunned ",4,game)
cammyvictory = Animation("cammy//cammy_victory ",5,game)
cammywalk.moveTo(850,470)
cammywalk.stop()

title = Image("images//start.png", game)
bk1 = Image("images//bk1.png",game)
vs = Image("images//vs.png",game)
title.resizeTo(game.width-12,game.height-12)
bk1.resizeTo(game.width-12,game.height-12)
vs.resizeTo(game.width-12,game.height-12)
title.draw()
game.drawText("Press [SPACE] to Start", 135, 500,Font(red,35,blue))
game.playMusic()
game.update()
game.wait(K_SPACE)

bk1.draw()
game.drawText("A long, ancient time ago, there were two fighters known as",230,260,Font(blue,30,white))
game.update()
time.sleep(1.5)
game.wait(K_SPACE)

bk1.draw()
game.drawText("Akuma and Cammy.",390,260,Font(blue,30,white))
game.update()
time.sleep(1.5)
game.wait(K_SPACE)

bk1.draw()
game.drawText("They didn't get along too well . . .",320,260,Font(blue,30,white))
game.update()
time.sleep(1.5)
game.wait(K_SPACE)

bk1.draw()
game.drawText("They had no reason for fighting one another, they just",230,260,Font(blue,30,white))
game.drawText("wanted entertainment. ",380,310,Font(blue,30,white))
game.update()
time.sleep(1.5)
game.wait(K_SPACE)

bk1.draw()
game.drawText("Take on the challenge of either being",290,260,Font(blue,30,white))
game.update()
time.sleep(1.5)
game.wait(K_SPACE)

bk1.draw()
game.drawText("Akuma as the lettered keys or",320,260,Font(blue,30,white))
game.update()
time.sleep(1.5)
game.wait(K_SPACE)

bk1.draw()
game.drawText("Cammy as the numbered keys.",320,260,Font(blue,30,white))
game.update()
time.sleep(1.5)
game.wait(K_SPACE)

bk1.draw()
game.drawText("Why won't you take the risk and enter the game?",250,290,Font(blue,30,white))
game.update()
time.sleep(1.5)
game.wait(K_SPACE)

bk1.draw()
game.drawText("Don't say I didn't warn you.",320,290,Font(blue,30,white))
game.update()
time.sleep(1.5)
game.wait(K_SPACE)

bk1.draw()
game.drawText("I will not guarentee you'll come out alive!",270,290,Font(blue,30,white))
game.drawText("Press [SPACE] to Continue", game.width/2 + 150, game.height-65, Font(blue,25,green))
game.update()
time.sleep(1.5)
game.wait(K_SPACE)

vs.draw()
game.update()
time.sleep(3)

game.stopMusic()
fightmusic.play()

#akuma
x = 140
y = 205
akumawalk.resizeTo(x,y)
akumaroundhousekick.resizeTo(x,y)
akumajab.resizeTo(x,y)
akumakick.resizeTo(x,y)
akumalowertrippunch.resizeTo(x,y)
akumapunchjab.resizeTo(x,y)
akumajumpkick.resizeTo(x,y)
akumajump.resizeTo(x,y)
akumajumppunch.resizeTo(x,y)
akumajumptumble.resizeTo(x,y)
akumakicktrip.resizeTo(x,y)
akumalowerkick.resizeTo(x,y)
akumapunch.resizeTo(x,y)
akumaroundkick.resizeTo(x,y)



#cammy

cfinish = Sound("sound//cammy_finish.wav ",1)
cguthit = Sound("sound//cammy_guthit.wav ",2)
chighkick = Sound("sound//cammy_highkick.wav ",3)
cjump = Sound("sound//cammy_jump.wav ",4)
ckick = Sound("sound//cammy_kick.wav ",5)
cwins = Sound("sound//cammywins.wav ",6)
csorryitsmyturn = Sound("sound//sorrynowitsmyturn.wav ",7)

w = 160
z = 190

c = +5
e = -0

r = -5
t = -0


cammypunch.resizeTo(w,z)
cammycrouch.resizeTo(w,z)
cammyforwardjump.resizeTo(w,z)
cammyforwardpunch.resizeTo(w,z)
cammyhighkick.resizeTo(w,z)
cammyjumping.resizeTo(w,z)
cammyjumpkick.resizeTo(w,z)
cammyjumppunch.resizeTo(w,z)
cammykick.resizeTo(w,z)
cammymiddlekick.resizeTo(w,z)
cammythrustkick.resizeTo(w,z)
cammywalk.resizeTo(w,z)
cammyblock.resizeTo(w,z)
cammyfacehit.resizeTo(w,z)
cammyfalldown.resizeTo(w,z)
cammyguthit.resizeTo(w,z)
cammystunned.resizeTo(w,z)
cammyvictory.resizeTo(w,z)

while not game.over:
    game.processInput()
    game.drawBackground()
    

    if keys.Pressed[K_a]: 
        akumawalk.nextFrame()
        akumawalk.moveX(-8)
    elif keys.Pressed[K_d]: 
        akumawalk.prevFrame()
        akumawalk.moveX(8)
    elif keys.Pressed[K_k]:
        akumaroundhousekick.moveTo(akumawalk.x - 15,akumawalk.y - 15)
    elif keys.Pressed[K_z]: 
        akumakick.moveTo(akumawalk.x,akumawalk.y)
    elif keys.Pressed[K_s]: 
        akumajab.moveTo(akumawalk.x - 15,akumawalk.y - 15)
    elif keys.Pressed[K_q]: 
        akumapunchjab.moveTo(akumawalk.x - 15,akumawalk.y - 15)
    elif keys.Pressed[K_e]: 
        akumalowertrippunch.moveTo(akumawalk.x - 15,akumawalk.y - 15)
    elif keys.Pressed[K_b]: 
        akumaroundkick.moveTo(akumawalk.x - 15,akumawalk.y - 15)
    elif keys.Pressed[K_w]: 
        akumajump.moveTo(akumawalk.x ,akumawalk.y )
        ajump.play()
    elif keys.Pressed[K_u]: 
        akumajumpkick.moveTo(akumawalk.x ,akumawalk.y )
        akumajumpkick.moveX(8)
        ajumpkick.play()
    elif keys.Pressed[K_y]: 
        akumajumppunch.moveTo(akumawalk.x - 15,akumawalk.y - 15)
        akumajumppunch.moveX(8)
    elif keys.Pressed[K_g]: 
        akumakicktrip.moveTo(akumawalk.x - 15,akumawalk.y - 15)
    elif keys.Pressed[K_p]: 
        akumalowerkick.moveTo(akumawalk.x - 15,akumawalk.y - 15)
        akumalowerkick.moveX(8)
    elif keys.Pressed[K_h]: 
        akumapunch.moveTo(akumawalk.x - 15,akumawalk.y - 15)
        akick.play()
    else:
        akumawalk.draw()

    if keys.Pressed[K_RIGHT]:
        cammywalk.nextFrame()
        cammywalk.moveX(8)
    elif keys.Pressed[K_LEFT]:
        cammywalk.prevFrame()
        cammywalk.moveX(-8)
    elif keys.Pressed[K_UP]:
        cammyjumping.moveTo(cammywalk.x ,cammywalk.y )
        cjump.play()
    elif keys.Pressed[K_1]:
        cammypunch.moveTo(cammywalk.x,cammywalk.y )
    elif keys.Pressed[K_2]:
        cammycrouch.moveTo(cammywalk.x,cammywalk.y )
    elif keys.Pressed[K_3]:
        cammyforwardpunch.moveTo(cammywalk.x,cammywalk.y )
    elif keys.Pressed[K_4]:
        cammyhighkick.moveTo(cammywalk.x,cammywalk.y )
        chighkick.play()
    elif keys.Pressed[K_5]:
        cammyforwardjump.moveTo(cammywalk.x,cammywalk.y )
    elif keys.Pressed[K_6]:
        cammyjumpkick.moveTo(cammywalk.x,cammywalk.y )
    elif keys.Pressed[K_7]:
        cammykick.moveTo(cammywalk.x,cammywalk.y )
        ckick.play()
    elif keys.Pressed[K_8]:
        cammythrustkick.moveTo(cammywalk.x,cammywalk.y )
    else:
        cammywalk.draw()


    if akumapunchjab.collidedWith(cammywalk):
        cammywalk.health-=.25

    if akumajab.collidedWith(cammywalk):
        cammywalk.health-=.25

    if akumajumpkick.collidedWith(cammywalk):
        cammywalk.health-=.25

    if akumajumppunch.collidedWith(cammywalk):
        cammywalk.health-=.25

    if akumakick.collidedWith(cammywalk):
        cammywalk.health-=.25

    if akumakicktrip.collidedWith(cammywalk):
        cammywalk.health-=.25

    if akumalowerkick.collidedWith(cammywalk):
        cammywalk.health-=.25

    if akumalowertrippunch.collidedWith(cammywalk):
        cammywalk.health-=.25

    if akumapunch.collidedWith(cammywalk):
        cammywalk.health-=.25

    if akumaroundkick.collidedWith(cammywalk):
        cammywalk.health-=.25

    if cammypunch.collidedWith(akumawalk):
        akumawalk.health-=.25

    if cammyforwardpunch.collidedWith(akumawalk):
        akumawalk.health-=.25

    if cammyhighkick.collidedWith(akumawalk):
        akumawalk.health-=.25 

    if cammyjumppunch.collidedWith(akumawalk):
        akumawalk.health-=.25

    if cammykick.collidedWith(akumawalk):
        akumawalk.health-=.25

    if cammymiddlekick.collidedWith(akumawalk):
        akumawalk.health-=.25

    if cammythrustkick.collidedWith(akumawalk):
        akumawalk.health-=.25

    if cammywalk.health<=0: 
        game.drawText("AKUMA WINS",300,250,Font(red,90,black)) 
        game.over=True
        
        cammypunch.visible = False
        cammycrouch.visible = False
        cammyforwardjump.visible = False
        cammyforwardpunch.visible = False
        cammyhighkick.visible = False
        cammyjumping.visible = False
        cammyjumpkick.visible = False
        cammyjumppunch.visible = False
        cammykick.visible = False
        cammymiddlekick.visible = False
        cammythrustkick.visible = False
        cammywalk.visible = False
        cammyblock.visible = False
        cammyfacehit.visible = False
        cammyfalldown.visible = False
        cammyguthit.visible = False
        cammystunned.visible = False


        akumawalk.visible = False
        akumaroundhousekick.visible = False
        akumajab.visible = False
        akumakick.visible = False
        akumalowertrippunch.visible = False
        akumapunchjab.visible = False
        akumajumpkick.visible = False
        akumajump.visible = False
        akumajumppunch.visible = False
        akumajumptumble.visible = False
        akumakicktrip.visible = False
        akumalowerkick.visible = False
        akumapunch.visible = False
        akumaroundkick.visible = False
        
    if akumawalk.health<=0:
        game.drawText("CAMMY WINS",300,250,Font(yellow,90,green))
        game.over=True
        #cammyvictory.draw()
        
        cammyvictory.visable = True
        cammypunch.visible = False
        cammycrouch.visible = False
        cammyforwardjump.visible = False
        cammyforwardpunch.visible = False
        cammyhighkick.visible = False
        cammyjumping.visible = False
        cammyjumpkick.visible = False
        cammyjumppunch.visible = False
        cammykick.visible = False
        cammymiddlekick.visible = False
        cammythrustkick.visible = False
        cammywalk.visible = False
        cammyblock.visible = False
        cammyfacehit.visible = False
        cammyfalldown.visible = False
        cammyguthit.visible = False
        cammystunned.visible = False


        akumawalk.visible = False
        akumaroundhousekick.visible = False
        akumajab.visible = False
        akumakick.visible = False
        akumalowertrippunch.visible = False
        akumapunchjab.visible = False
        akumajumpkick.visible = False
        akumajump.visible = False
        akumajumppunch.visible = False
        akumajumptumble.visible = False
        akumakicktrip.visible = False
        akumalowerkick.visible = False
        akumapunch.visible = False
        akumaroundkick.visible = False





    game.drawText("Cammy's Health: " + str(cammywalk.health),700,15,Font(white,28,blue))
    game.drawText("Akuma's Health: " + str(akumawalk.health),100,15,Font(white,28,blue))

    game.update(10)

game.drawText("Press[ESC] to Exit ",400,500,Font(white,30,blue))
game.update(1)
game.wait(K_ESCAPE) 
game.quit()

    
