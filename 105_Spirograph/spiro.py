import pygame as pg
import random as rnd
import math as m
import os
from datetime import datetime  # Korrekte Importanweisung

def initialization(pos1, radius1):
    radius2 = radius1 * rnd.random()  # Ensure second circle is smaller
    radius3 = radius2 * rnd.random()  # Ensure third circle is smaller
    pos2 = pos1 + radius1 - radius2
    color.hsva = (rnd.randrange(360), 100, 100, 100)
    return radius2,radius3,pos2,False

def update_speed(scale_factor):
    """Update the speed by a scaling factor."""
    global speed
    speed *= scale_factor

def save_image(surface, base_filename='spirograph', directory='.', ext='.png'):
    """
    Save the current image to a file with a timestamp in the filename.
    The format is: base_filename_YYYY-MM-DD_HH-MM.png
    """
    # Get the current time and format it
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
    filename = f"{base_filename}_{timestamp}{ext}"
    filepath = os.path.join(directory, filename)
    
    # Save the surface to the file
    pg.image.save(surface, filepath)
    print(f"Image saved as {filename}")

# Initialize Pygame and setup window
pg.init()
WINDOW_SIZE = pg.Vector2(1200, 800)
window = pg.display.set_mode(WINDOW_SIZE)
background = pg.Surface(WINDOW_SIZE)
color = pg.Color(0)

color.hsva = (rnd.randrange(360), 100, 100, 100)

# Define initial parameters
draw_circles = True
draw_lines = False
speed = 0.1

# Define the positions and radii of the circles
pos1 = WINDOW_SIZE / 2
radius1 = pg.Vector2(min(WINDOW_SIZE) / 2, 0)
radius2, radius3, pos2, last_position = initialization(pos1, radius1)

# Main loop
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            match event.key:
                case pg.K_ESCAPE | pg.K_q:
                    running = False
                case pg.K_k:
                    draw_circles = not draw_circles
                case pg.K_l:
                    draw_lines = not draw_lines
                case pg.K_KP_PLUS:
                    update_speed(2)
                case pg.K_KP_MINUS:
                    update_speed(0.5)
                case pg.K_f:
                    color.hsva = (rnd.randrange(360), 100, 100, 100)
                case pg.K_RETURN:
                    radius2, radius3, pos2, last_position = initialization(pos1, radius1)
                case pg.K_n:
                    background.fill('black')
                    radius2, radius3, pos2, last_position = initialization(pos1, radius1)
                case pg.K_s:
                    save_image(background)

    # Update positions and angles
    window.fill('black')
    pos2 = pos1 + (pos2 - pos1).rotate(speed)
    
    # Rotate the smaller radii to simulate motion
    radius2 = radius2.rotate(-speed * radius1.length() / radius2.length())
    radius3 = radius3.rotate(-speed * radius1.length() / radius2.length())
    
    pos3 = pos2 + radius3

    # Drawing the circles and lines
    window.blit(background, (0, 0))
    if draw_circles:
        pg.draw.circle(window, 'white', pos1, radius1.length(), 1)
        pg.draw.circle(window, 'white', pos2, radius2.length(), 1)
        pg.draw.line(window, 'green', pos2, pos3, 1)
        pg.draw.circle(window, color, pos3, 5)
    
    if draw_lines and last_position:
        pg.draw.line(background, color, last_position, pos3, 2)

    last_position = pos3

    # Update the display
    pg.display.flip()

# Clean up Pygame
pg.quit()
