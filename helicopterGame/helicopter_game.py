import pygame
import random
import math
from pygame import mixer
from time import sleep
class play:
	running = True
	
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Mario')
		screen=pygame.display.set_mode((800,600))
		blockImg = pygame.image.load('block.png')

		mixer.music.load('helicopter.mp3')
		mixer.music.play(-1)

		b_x=[]
		b_y=[]
		for i in range(5):
			b_x.append(672 + random.randint(0,700) )
			b_y.append(472)
		b_x_c=-0.8
		def block(x,y,i):
			screen.blit(blockImg,(x[i],y[i]))

		cloudImg=pygame.image.load('cloud.png')
		c_x=[]
		c_y=[]
		for i in range(5):
			c_x.append(672 + random.randint(0,700) )
			c_y.append(random.randint(0,100))
		c_x_c=-0.8

		def cloud(x,y,i):
			screen.blit(cloudImg,(x[i],y[i]))

		helicopterImg=pygame.image.load('helicopter.png')
		h_x=400
		h_y=526
		h_y_c=0
		def helicopter(x,y):
			screen.blit(helicopterImg,(x,y))

		def isCollision_ch(x1,y1,x2,y2,i):
			d = math.sqrt(math.pow(x1[i]-x2 ,2) + math.pow(y1[i]-y2, 2))
			if d<64:
				return True
			else:
				return False
		def isCollision_hb(x1,y1,x2,y2,i):
			d = math.sqrt(math.pow(x1[i]-x2 ,2) + math.pow(y1[i]-y2, 2))
			if d<64:
				return True
			else:
				return False


		score_value =0
		font =pygame.font.Font('freesansbold.ttf',40)

		def score():
			score =font.render('Score: '+str(score_value),True,(0,0,0))
			screen.blit(score,(10,10))

		
		while self.running:
			screen.fill((255,255,255))
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					self.running =False
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_SPACE:
						h_y_c = -1
				elif e.type == pygame.KEYUP:
					if e.key == pygame.K_SPACE:
						h_y_c = 1
			for i in range(5):
				block(b_x,b_y,i)
				b_x[i] += b_x_c
				if b_x[i]<=0:
					b_x[i]=672+random.randint(-150,500)
				cloud(c_x,c_y,i)
				c_x[i]+= c_x_c
				if c_x[i] <=0:
					c_x[i]=672+random.randint(-150,500)
					c_y[i]=random.randint(0,300)
				if isCollision_hb(b_x,b_y,h_x,h_y,i) or isCollision_ch(c_x,c_y,h_x,h_y,i):
					explosion  = mixer.Sound('Explosion.wav')
					explosion.play()
					self.running = False


			helicopter(h_x,h_y)
			h_y+=h_y_c
			if h_y>=526:
				h_y=526
			elif h_y<=0:
				h_y=0
			score_value+=1
			score()
			
			pygame.display.update()
		explosionImg=pygame.image.load('explosion.png')
		screen.blit(explosionImg,(h_x,h_y))
		pygame.display.update()
	def hold(self):
		pygame.init()
		pygame.display.set_caption('Mario')
		screen=pygame.display.set_mode((800,600))
		self.running =True
		while self.running:
			screen.fill((255,255,255))
			font =pygame.font.Font('freesansbold.ttf',42)
			hold = font.render('Press 1 to play again or press 0 to quit.',True,(0,0,0))
			screen.blit(hold,(0,250))
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					self.running =False
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_0:
						self.running=False
					elif e.key == pygame.K_1:
						self.__init__()
						self.hold()
			pygame.display.update()



p =play()
p.hold()


