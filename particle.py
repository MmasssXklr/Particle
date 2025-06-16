import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particles Game")

# Clock
clock = pygame.time.Clock()

# Particle class
class Particle:
    def __init__(self):
        self.x = random.uniform(100, WIDTH - 100)
        self.y = random.uniform(100, HEIGHT - 100)
        self.radius = random.randint(5, 10)
        self.color = (
            random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255)
        )
        self.vel_x = random.uniform(-2, 2)
        self.vel_y = random.uniform(-2, 2)
        self.gravity = 0.1
        self.friction = 0.98

    def update(self, mouse_pos):
        mx, my = mouse_pos
        dx = self.x - mx
        dy = self.y - my
        dist = math.hypot(dx, dy)

        if dist < 100 and dist > 0:
            force = 100 / dist  # stronger when closer
            angle = math.atan2(dy, dx)
            self.vel_x += math.cos(angle) * force
            self.vel_y += math.sin(angle) * force

        # Apply gravity
        self.vel_y += self.gravity

        # Update position
        self.x += self.vel_x
        self.y += self.vel_y

        # Bounce off walls
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.vel_x *= -1
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.vel_y *= -0.9
            self.y = HEIGHT - self.radius

        # Apply friction
        self.vel_x *= self.friction
        self.vel_y *= self.friction

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Particle list
particles = [Particle() for _ in range(100)]

# Main loop
running = True
while running:
    clock.tick(60)
    screen.fill((20, 20, 40))  # Dark background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()

    # Update and draw particles
    for p in particles:
        p.update(mouse_pos)
        p.draw(screen)

    pygame.display.flip()

pygame.quit()
