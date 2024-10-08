import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Complex Adventure Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player settings
player_pos = [WIDTH // 2, HEIGHT // 2]
player_size = 50
player_health = 100

# Enemy settings
enemy_size = 50
enemies = []

# Item settings
items = []
item_size = 30

# Levels
levels = [
    {"background": (0, 0, 100), "enemies": 5},
    {"background": (100, 0, 0), "enemies": 10},
]
current_level = 0

# Game loop control
running = True
clock = pygame.time.Clock()

# Inventory
inventory = []

# Storyline
story_lines = [
    "Welcome to the adventure!",
    "Defeat enemies to progress.",
    "Find items to restore health.",
]

def spawn_enemy():
    x = random.randint(0, WIDTH - enemy_size)
    y = random.randint(0, HEIGHT - enemy_size)
    enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))

def spawn_item():
    x = random.randint(0, WIDTH - item_size)
    y = random.randint(0, HEIGHT - item_size)
    items.append(pygame.Rect(x, y, item_size, item_size))

def load_level(level_index):
    global enemies
    enemies.clear()
    for _ in range(levels[level_index]["enemies"]):
        spawn_enemy()

def draw_player():
    pygame.draw.rect(screen, GREEN, (*player_pos, player_size, player_size))

def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

def draw_items():
    for item in items:
        pygame.draw.rect(screen, WHITE, item)

def handle_collisions():
    global player_health
    player_rect = pygame.Rect(*player_pos, player_size, player_size)
    for enemy in enemies[:]:
        if player_rect.colliderect(enemy):
            enemies.remove(enemy)
            player_health -= 20
            print(f"Health: {player_health}")

def handle_item_collisions():
    global player_health
    player_rect = pygame.Rect(*player_pos, player_size, player_size)
    for item in items[:]:
        if player_rect.colliderect(item):
            items.remove(item)
            player_health += 20  # Restore health
            print(f"Health: {player_health}")

def move_enemies():
    for enemy in enemies:
        if player_pos[0] < enemy.x:
            enemy.x -= 1
        elif player_pos[0] > enemy.x:
            enemy.x += 1
        if player_pos[1] < enemy.y:
            enemy.y -= 1
        elif player_pos[1] > enemy.y:
            enemy.y += 1

def attack():
    attack_range = 70
    attack_rect = pygame.Rect(player_pos[0] - attack_range // 2, player_pos[1] - attack_range // 2, attack_range, attack_range)
    for enemy in enemies[:]:
        if attack_rect.colliderect(enemy):
            enemies.remove(enemy)
            print("Enemy defeated!")

def display_inventory():
    font = pygame.font.Font(None, 36)
    for i, item in enumerate(inventory):
        item_text = font.render(f'Item {i + 1}: {item}', True, WHITE)
        screen.blit(item_text, (10, 50 + i * 30))

def display_story():
    font = pygame.font.Font(None, 36)
    if current_level < len(story_lines):
        story_text = font.render(story_lines[current_level], True, WHITE)
        screen.blit(story_text, (10, HEIGHT - 50))

# Load the first level
load_level(current_level)

# Main game loop
while running:
    screen.fill(levels[current_level]["background"])

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5
    if keys[pygame.K_SPACE]:  # Press SPACE to attack
        attack()

    handle_collisions()
    handle_item_collisions()

    # Spawn enemies and items periodically
    if random.randint(0, 100) < 2:
        spawn_enemy()
    if random.randint(0, 100) < 2:
        spawn_item()

    move_enemies()
    draw_player()
    draw_enemies()
    draw_items()
    display_inventory()
    display_story()

    # Check if all enemies are defeated to move to the next level
    if not enemies and current_level < len(levels) - 1:
        current_level += 1
        load_level(current_level)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
