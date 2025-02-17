# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
	# Start pygame and set screen size
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Start Clock and set dealta time (dt)
	clock = pygame.time.Clock()
	dt = 0

	# create update & draw groups
	UpdateGroup = pygame.sprite.Group()
	DrawGroup = pygame.sprite.Group()

	# Spawn Player and add to groups
	Player.containers = (UpdateGroup, DrawGroup)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	# game Loop
	while True:
		# Close on exit button pressed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		# Update and Draw GameLoop
		GameUpdate(dt, UpdateGroup)
		GameDraw(screen, DrawGroup)

		# tick dealta time
		dt = clock.tick(60)/1000	

def GameUpdate(dt, updateGroup):
	# update Objects
	for obj in updateGroup:
		updateGroup.update(dt)

def GameDraw(screen, drawGroup):
	# Fill Background
	screen.fill("black")

	# Draw Objects
	for obj in drawGroup:
		obj.draw(screen)

	# push draw changes *** DO LAST ***
	pygame.display.flip()



if __name__ == "__main__":
	main()
