# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

# Spawn Player
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def main():
	# Start pygame and set screen size
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Start Clock and set dealta time (dt)
	clock = pygame.time.Clock()
	dt = 0

	# game Loop
	while True:
		# Close on exit button pressed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		# Update and Draw GameLoop
		GameUpdate(dt)
		GameDraw(screen)
		

		# tick dealta time
		dt = clock.tick(60)/1000	

def GameUpdate(dt):
	player.update(dt)

def GameDraw(screen):
	# Fill Background
	screen.fill("black")

	# Draw player
	player.draw(screen)

	# push draw changes *** DO LAST ***
	pygame.display.flip()



if __name__ == "__main__":
	main()
