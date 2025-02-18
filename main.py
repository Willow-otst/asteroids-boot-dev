# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	# Start pygame and set screen size
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Start Clock and set dealta time (dt)
	clock = pygame.time.Clock()
	dt = 0

	# create asteroids, shots, update & draw groups
	UpdateGroup = pygame.sprite.Group()
	DrawGroup = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# setup asteroid field
	Asteroid.containers = (asteroids, UpdateGroup, DrawGroup)
	AsteroidField.containers = UpdateGroup
	asteroid_field = AsteroidField()

	# Spawn Player and add to groups
	Player.containers = (UpdateGroup, DrawGroup)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	# add shots containers
	Shot.containers = (shots, UpdateGroup, DrawGroup)

	# game Loop
	while True:
		# Close on exit button pressed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		# Update and Draw GameLoop
		GameUpdate(dt, UpdateGroup)
		GameDraw(screen, DrawGroup)

		
		for asteroid in asteroids:
			# check player collisions
			if player.CollidesWith(asteroid):
				print("Game Over!")
				quit()

			# check shot collisions
			for shot in shots:
				if shot.CollidesWith(asteroid):
					shot.kill()
					asteroid.split()

		# tick dealta time
		dt = clock.tick(60)/1000	

def GameUpdate(dt, updateGroup):
	# update Objects
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
