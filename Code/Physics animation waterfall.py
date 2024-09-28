import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Waterfall properties
num_particles = 500
particles = []

# Monte Carlo Randomization function for natural spread
def monte_carlo_randomization():
    r = random.random()
    return math.sqrt(r) if random.random() < 0.5 else -math.sqrt(r)

# Particle properties
class Particle:
    def __init__(self):
        self.x = width - 100  # Starting near the right edge for angle
        self.y = 50  # Start higher up
        self.vx = -random.uniform(2, 4)  # Negative x-velocity for leftward flow
        self.vy = random.uniform(1, 3)  # Slight downward movement

    def update(self):
        self.vy += 0.1  # Gravity effect
        self.x += self.vx
        self.y += self.vy

        # Interaction with bottom platform
        if self.y > height // 2 and self.vx < 0:
            self.vx = -self.vx * 0.7  # Bounce effect
            self.vy = -self.vy * 0.3  # Reduced speed after bounce

    def draw(self):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), 3)

# Create particles
for _ in range(num_particles):
    particles.append(Particle())

# Main simulation loop
running = True
while running:
    screen.fill(WHITE)

    # Draw platform (representing the structure in the image)
    pygame.draw.rect(screen, GRAY, (200, height // 2, 400, 20))
    pygame.draw.rect(screen, GRAY, (440, height // 5, 20, 400))
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw particles
    for particle in particles:
        particle.update()
        particle.draw()

        # Reset particles when they go off-screen (bottom or sides)
        if particle.y > height or particle.x < 0 or particle.x > width:
            particles.remove(particle)
            particles.append(Particle())

    pygame.display.flip()
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
