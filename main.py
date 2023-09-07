import pygame
import pygame_gui
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CIRCLE_RADIUS1 = 100
CIRCLE_RADIUS2 = 50
INITIAL_RADIUS = 50

CIRCLE_CENTER1 = [WIDTH // 2, HEIGHT // 2]
CIRCLE_CENTER2 = [WIDTH // 2, HEIGHT // 2]

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drag and Drop with Click Counter")

# Initialize Pygame GUI
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Initialize variables
dragging = False
click_count1 = 0
click_count2 = 0
circle_num = 0

# Function to check if a point (x, y) is within the circle
def is_inside_circle1(x, y):
    distance = pygame.math.Vector2(x - CIRCLE_CENTER1[0], y - CIRCLE_CENTER1[1]).length()
    return distance <= CIRCLE_RADIUS1

def is_inside_circle2(x, y):
    distance = pygame.math.Vector2(x - CIRCLE_CENTER2[0], y - CIRCLE_CENTER2[1]).length()
    return distance <= CIRCLE_RADIUS2

# Create a slider for controlling the circle's radius
slider_rect1 = pygame.Rect(10, 480, 200, 30)
slider1 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider_rect1, start_value=50, value_range=(1, 100), manager=manager)
label_rect1 = pygame.Rect(10, 450, 200, 30)
label = pygame_gui.elements.UILabel(relative_rect=label_rect1, text="Circle1 Radius:", manager=manager)

slider_rect2 = pygame.Rect(10, 550, 200, 30)
slider2 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider_rect2, start_value=50, value_range=(1, 100), manager=manager)
label_rect2 = pygame.Rect(10, 520, 200, 30)
label = pygame_gui.elements.UILabel(relative_rect=label_rect2, text="Circle2 Radius:", manager=manager)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.process_events(event)

        # # Handle events for the radius slider
        # if event.type  == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
        #     if event.ui_element == radius_slider:
        #         circle_radius = int(radius_slider.get_current_value())

        # # Handle events for the opacity slider
        # if event.type  == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
        #     if event.ui_element == opacity_slider:
        #         circle_opacity = int(opacity_slider.get_current_value())

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the circle
    # draw_circle()

    # Update the GUI
    manager.update(1 / 60.0)
    manager.draw_ui(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
