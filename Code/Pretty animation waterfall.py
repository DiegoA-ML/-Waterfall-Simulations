import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Monte Carlo Waterfall Animation")

# Colors
SKY_BLUE = (135, 206, 235)
WATER_BLUE = (64, 164, 223)
ROCK_BROWN = (101, 67, 33)

# Monte Carlo function for generating random numbers
def monte_carlo_random():
    while True:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if y <= math.exp(-x):  # Using exponential distribution for more natural flow
            return x

# Particle class for water droplets
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5 + 10 * monte_carlo_random()  # Speed between 5 and 15
        self.size = 2 + 3 * monte_carlo_random()  # Size between 2 and 5

    def move(self):
        self.y += self.speed
        # Add some horizontal movement using Monte Carlo
        self.x += (monte_carlo_random() - 0.5) * 2
        if self.y > height:
            self.reset()

    def reset(self):
        self.y = random.randint(-50, 0)
        self.x = width // 2 + (monte_carlo_random() - 0.5) * 200  # Spread around the center

    def draw(self, surface):
        pygame.draw.circle(surface, WATER_BLUE, (int(self.x), int(self.y)), int(self.size))

# Create particles
particles = [Particle(width // 2 + (monte_carlo_random() - 0.5) * 200, random.randint(-50, height)) 
             for _ in range(500)]

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(SKY_BLUE)

    # Draw rocks
    pygame.draw.rect(screen, ROCK_BROWN, (0, height - 100, width, 100))
    pygame.draw.polygon(screen, ROCK_BROWN, [(0, height - 100), (width, height - 100), 
                                             (width, height), (0, height)])

    # Update and draw particles
    for particle in particles:
        particle.move()
        particle.draw(screen)

    # Draw water pool
    pygame.draw.rect(screen, WATER_BLUE, (0, height - 50, width, 50))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()