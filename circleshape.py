import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def update(self, dt):
        # sub-classes must override
        pass

    def draw(self, screen):
        # sub-classes must override
        pass

    def CollidesWith(self, circleShape):
        return (
            pygame.math.Vector2.distance_to(self.position, circleShape.position) <= 
            (self.radius + circleShape.radius)
        )