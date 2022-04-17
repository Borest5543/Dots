import pygame
from pygame.locals import *
import random
import time

class Circles_random:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('bolinha')

		self.screen_width = 700
		self.screen_height = 700
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

		self.fps = pygame.time.Clock()
		self.var()
		self.colors()

	def var(self):
		self.threshold = 40

		self.color_pos1 = 2
		self.color_pos2 = 1

		self.tick = 0
		self.draw_radius = 1

		self.dictionary = {}
		self.dictionary_list = []
		self.total = 150
		return 0

	def colors(self):
		self.black = (0, 0, 0)
		self.fake_black = (10, 10, 10)
		self.gray = (128, 128, 128)
		self.blue = (0, 0, 255)
		self.red = (255, 0, 0)
		self.green = (0, 255, 0)
		self.white = (255,255,255)
		self.color_list = [self.black, self.red, self.blue, self.green, self.white, self.gray]
		return self.color_pos1, self.color_pos2
	
	def random_color(self):
		color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
		return color

	def draw_random_circle(self, color=(255,255,255)):
		color 
		radius = random.randrange(1,20)
		posx = random.randrange(radius,self.screen_width-radius)
		posy = random.randrange(radius,self.screen_height-radius)
		velx = random.randrange(-10,11,1)/10
		vely = random.randrange(-10,11,1)/10
		
		return posx, posy, color, radius, velx, vely

	def draw_lines(self, color=(0,0,255)):
		x1 = 0
		x2 = 0
		y1 = 0
		y2 = 0
		for i in range(len(self.dictionary_list)):
			for j in range(len(self.dictionary_list)):
				if i >= j:
					pass
				else:
					x1 = self.dictionary[self.dictionary_list[j]][0]
					x2 = self.dictionary[self.dictionary_list[i]][0]
					y1 = self.dictionary[self.dictionary_list[j]][1]
					y2 = self.dictionary[self.dictionary_list[i]][1]
					if (  (((x2-x1)**2)+((y2-y1)**2))**(1/2)) <= self.threshold:
						pygame.draw.line(self.screen, color, (x2, y2), (x1, y1))
		return 0 

	def change_pos(self):
		for i in self.dictionary.keys():
			j = {i:[round(self.dictionary[i][0]+self.dictionary[i][4],1), round(self.dictionary[i][1]+self.dictionary[i][5],1), self.dictionary[i][2], self.dictionary[i][3], self.dictionary[i][4], self.dictionary[i][5]]}
			self.dictionary.update(j)
				
		for i in self.dictionary.keys():
			if self.dictionary[i][0] > self.screen_width-self.dictionary[i][3]:
				j = {i:[self.screen_width-self.dictionary[i][3], self.dictionary[i][1]+self.dictionary[i][5], self.dictionary[i][2], self.dictionary[i][3], -self.dictionary[i][4], self.dictionary[i][5]]}

			if self.dictionary[i][0] <= self.dictionary[i][3]:
				j = {i:[self.dictionary[i][3], self.dictionary[i][1]+self.dictionary[i][5], self.dictionary[i][2], self.dictionary[i][3], -self.dictionary[i][4], self.dictionary[i][5]]}

			if self.dictionary[i][1] >= self.screen_height-self.dictionary[i][3]:
				j = {i:[self.dictionary[i][0]+self.dictionary[i][4], self.screen_height-self.dictionary[i][3], self.dictionary[i][2], self.dictionary[i][3], self.dictionary[i][4], -self.dictionary[i][5]]}

			if self.dictionary[i][1] <= self.dictionary[i][3]:
				j = {i:[self.dictionary[i][0]+self.dictionary[i][4], self.dictionary[i][3], self.dictionary[i][2], self.dictionary[i][3], self.dictionary[i][4], -self.dictionary[i][5]]}
			self.dictionary.update(j)
		return 0

	def commands(self):
		if pygame.key.get_pressed()[K_SPACE]:
			if self.tick == 0:
				self.tick = 1
			else:
				self.tick = 0
			print("space {}".format(self.tick))
			time.sleep(0.2)
			

		if pygame.key.get_pressed()[K_UP]:
			if self.threshold < (self.screen_width**2 + self.screen_height**2)**(1/2):
				self.threshold +=1
		elif pygame.key.get_pressed()[K_DOWN]:
			if self.threshold > 0:
				self.threshold -=1
		if pygame.key.get_pressed()[K_RIGHT]:
			self.color_pos1 +=1
			time.sleep(0.08)
			if self.color_pos1 > len(self.color_list)-1:
				self.color_pos1 = 0
		elif pygame.key.get_pressed()[K_LEFT]:
			self.color_pos2 +=1
			time.sleep(0.08)
			if self.color_pos2 > len(self.color_list)-1:
				self.color_pos2 = 0

		if pygame.key.get_pressed()[K_c]:
			self.color_list.append( self.random_color())
		if pygame.key.get_pressed()[K_v]:
			self.color_list.clear()
			self.color_pos1 = 0
			self.color_pos2 = 0
			self.color_list.append(self.random_color())
			time.sleep(0.08)

		if pygame.key.get_pressed()[K_r]:
			if self.draw_radius:
				self.draw_radius = 0
			else:
				self.draw_radius = 1
			time.sleep(0.08)


		return self.threshold, self.color_pos1, self.color_pos2

	def main(self):
		for i in range(self.total):
			self.dictionary["circle_{}".format(i)] = list(self.draw_random_circle())
			self.dictionary_list.append("circle_{}".format(i))

		while True:
			if self.tick == 0:
				self.screen.fill(self.black)
				self.fps.tick(30)

				self.commands()
				
				self.draw_lines(self.color_list[self.color_pos1])

				for i in self.dictionary.values():
					pygame.draw.circle(self.screen, color=self.color_list[self.color_pos2], center=(i[0], i[1]), radius=2)
					if self.draw_radius:
						pygame.draw.circle(self.screen, color=(40,0,0), center=(i[0], i[1]), radius=self.threshold/2, width=1)			

				self.change_pos()
			else:
				self.commands()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

			pygame.display.update()

if __name__ == '__main__':
	play = Circles_random()
	play.main()