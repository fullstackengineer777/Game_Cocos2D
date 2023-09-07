import pygame
import pygame_gui
import sys
import time
import threading

# Initialize Pygame
pygame.init()

# Initialize Pygame GUI

# Constants
WIDTH, HEIGHT = 1600, 800
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CIRCLE_RADIUS1 = 100
CIRCLE_RADIUS2 = 50
INITIAL_RADIUS = 50

CIRCLE_CENTER1 = [WIDTH // 2, HEIGHT // 2]
CIRCLE_CENTER2 = [WIDTH // 2, HEIGHT // 2]

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Demo")

# Initialize Pygame GUI
manager = pygame_gui.UIManager((WIDTH, HEIGHT))
# Initialize variables
dragging = False
click_count1 = 0
click_count2 = 0
click_count3 = 0
game_started = False
game_paused = False
INITIAL_TIME = 300
countdown_time = INITIAL_TIME  # Change this to your desired countdown time
countdown_complete = False
circle_num = 0
# Function to check if a point (x, y) is within the circle
def is_inside_circle1(x, y):
    distance = pygame.math.Vector2(x - CIRCLE_CENTER1[0], y - CIRCLE_CENTER1[1]).length()
    return distance <= CIRCLE_RADIUS1

def is_inside_circle2(x, y):
    distance = pygame.math.Vector2(x - CIRCLE_CENTER2[0], y - CIRCLE_CENTER2[1]).length()
    return distance <= CIRCLE_RADIUS2

# def update_score():
    # Display a message before starting the game
    # font = pygame.font.Font(None, 24)
    # text_surface1 = font.render(str(click_count1), True, RED)
    # text_rect1 = text_surface1.get_rect(center=(700,550))
    # screen.blit(text_surface1, text_rect1)

    # text_surface2 = font.render(str(click_count2), True, BLUE)
    # text_rect2 = text_surface2.get_rect(center=(730,550))
    # screen.blit(text_surface2, text_rect2)

    # text_surface3 = font.render(str(click_count3), True, BLUE)
    # text_rect3 = text_surface3.get_rect(center=(730,550))
    # screen.blit(text_surface3, text_rect3)

    #  score_lbl1.set_text(str(click_count1))
    #  score_lbl2.set_text(str(click_count2))
    #  score_lbl3.set_text(str(click_count3))

# Create a slider for controlling the circle's radius

# score_rect1 = pygame.Rect(700, 550, 20, 20)
# score_lbl1 = pygame_gui.elements.UILabel(relative_rect=score_rect1, text=str(click_count1), manager=manager)
# score_rect2 = pygame.Rect(730, 550, 20, 20)
# score_lbl2 = pygame_gui.elements.UILabel(relative_rect=score_rect2, text=str(click_count2), manager=manager)
# score_rect3 = pygame.Rect(760, 550, 20, 20)
# score_lbl3 = pygame_gui.elements.UILabel(relative_rect=score_rect3, text=str(click_count3), manager=manager)
  
slider_rect1 = pygame.Rect(10, HEIGHT - 120, 200, 30)
slider1 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider_rect1, start_value=50, value_range=(1, 300), manager=manager)
label_rect1 = pygame.Rect(10, HEIGHT - 150, 200, 30)
slider_label1 = pygame_gui.elements.UILabel(relative_rect=label_rect1, text="Red Circle Radius:", manager=manager)

slider_rect2 = pygame.Rect(10, HEIGHT - 50, 200, 30)
slider2 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider_rect2, start_value=50, value_range=(1, 300), manager=manager)
label_rect2 = pygame.Rect(10, HEIGHT - 80, 200, 30)
slider_label2 = pygame_gui.elements.UILabel(relative_rect=label_rect2, text="Blue Circle Radius:", manager=manager)

slider_rect3 = pygame.Rect(220, HEIGHT - 50, 200, 30)
slider3 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider_rect3, start_value=50, value_range=(1, 300), manager=manager)
label_rect3 = pygame.Rect(220, HEIGHT - 80, 200, 30)
slider_label3 = pygame_gui.elements.UILabel(relative_rect=label_rect3, text="Set Time 0 ~ 5 min:", manager=manager)

start_button_rect = pygame.Rect(WIDTH/2 - 50, HEIGHT - 50, 100, 30)
start_button = pygame_gui.elements.UIButton(relative_rect=start_button_rect, text="Start", manager=manager)
end_button_rect = pygame.Rect(WIDTH/2 - 50, HEIGHT - 50, 100, 30)
end_button = pygame_gui.elements.UIButton(relative_rect=start_button_rect, text="Restart", manager=manager)
end_button.hide()

label_rect_score2 = pygame.Rect(450, HEIGHT - 110, 100, 30)
slider_label_score2 = pygame_gui.elements.UILabel(relative_rect=label_rect_score2, text="Red Score:", manager=manager)
label_rect_score2 = pygame.Rect(450, HEIGHT - 80, 100, 30)
slider_label_score2 = pygame_gui.elements.UILabel(relative_rect=label_rect_score2, text="Blue Score:", manager=manager)
label_rect_score2 = pygame.Rect(450, HEIGHT - 50, 100, 30)
slider_label_score2 = pygame_gui.elements.UILabel(relative_rect=label_rect_score2, text="Ground Score:", manager=manager)

def start_game():
    global game_started# Start the game when the button is pressed
    game_started = True
    print("Game started!")
    global click_count1
    click_count1 = 0
    global click_count2
    click_count2 = 0
    global click_count3
    click_count3 = 0
    slider1.hide()
    slider2.hide()
    slider_label1.hide()
    slider_label2.hide()
    slider3.hide()
    countdown_thread = threading.Thread(target=countdown_timer)
    slider_label3.hide()

    start_button.hide()
    end_button.show()
    print(countdown_time)
    countdown_thread.start()
    # countdown_thread.join()
    global game_paused
    game_paused = False
    print("aa")
    print(game_paused)
def restart_game():
    global CIRCLE_RADIUS1
    CIRCLE_RADIUS1 = 100
    global CIRCLE_RADIUS2
    CIRCLE_RADIUS2 = 50
    global INITIAL_RADIUS
    INITIAL_RADIUS = 50
    global click_count1
    click_count1 = 0
    global click_count2
    click_count2 = 0
    global click_count3
    click_count3 = 0
    print(click_count1)
    global game_started
    game_started = False
    print("Game Ended!")
    slider1.show()
    slider2.show()
    slider_label1.show()
    slider_label2.show()
    slider3.show()
    slider_label3.show()
    start_button.show()
    end_button.hide()
    # //stop counting
    global countdown_timer
    countdown_time = -1
    global game_paused
    game_paused = False
# Function for the countdown timer
def pause_game():
    CIRCLE_RADIUS1 = 100
    CIRCLE_RADIUS2 = 50
    INITIAL_RADIUS = 50
    click_count1 = 0
    click_count2 = 0
    click_count3 = 0
    game_started = False
    print("Game Ended!")
    slider1.show()
    slider2.show()
    slider_label1.show()
    slider_label2.show()
    slider3.show()
    slider_label3.show()
    end_button.show()
    start_button.hide()
    print("Timeout!!!")
    # alarm text
    global game_paused
    game_paused = True

    global countdown_timer
    countdown_time = -1

def countdown_timer():
    global countdown_time, game_paused
    # countdown_time = INITIAL_TIME
    while countdown_time > 0 :
        # Update the countdown timer
        countdown_time -= 1
        # Sleep for 1 second
        time.sleep(1)
        print(countdown_time)

      
    # Countdown is complete
    pause_game()
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        
        
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Check for left mouse button click
                x, y = event.pos
                if(is_inside_circle1(x, y) and is_inside_circle2(x, y)):
                    dragging = True
                    if CIRCLE_RADIUS1 > CIRCLE_RADIUS2:
                        circle_num = 2 
                        if game_started: 
                            click_count2 += 4
                            print(f"Blue Circle Click Count: {click_count2}")
                    else:
                        circle_num = 1
                        if game_started: 
                            click_count1 += 9
                            print(f"Red Circle Click Count: {click_count1}")
                else:
                    if is_inside_circle1(x, y) :
                        dragging = True
                        circle_num = 1
                        if game_started: 
                            click_count1 += 9
                            print(f"Red Circle Click Count: {click_count1}")
                    if is_inside_circle2(x, y) :
                        dragging = True
                        circle_num = 2 
                        if game_started: 
                            click_count2 += 4
                            print(f"Blue Circle Click Count: {click_count2}")
                    if not is_inside_circle1(x,y) and not is_inside_circle2(x,y) and  game_started:
                        click_count3 += 5
                        circle_num = 3
                    # update_score()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging and circle_num == 1:
                CIRCLE_CENTER1[0], CIRCLE_CENTER1[1] = event.pos
            if dragging and circle_num == 2:
                CIRCLE_CENTER2[0], CIRCLE_CENTER2[1] = event.pos

        manager.process_events(event)
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == slider1:
                CIRCLE_RADIUS1 = int(slider1.get_current_value())

        # Handle events for the opacity slider
        if event.type  == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == slider2:
                CIRCLE_RADIUS2 = int(slider2.get_current_value())
        #Change game time
        if event.type  == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == slider3:
                countdown_time = int(slider3.get_current_value())


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start_button:
                start_game()
                
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == end_button:
                restart_game()
                

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw a red circle
    pygame.draw.circle(screen, RED, CIRCLE_CENTER1, CIRCLE_RADIUS1)
    pygame.draw.circle(screen, BLUE, CIRCLE_CENTER2, CIRCLE_RADIUS2)
     # Display a message before starting the game
    font = pygame.font.Font(None, 24)
    text_score1 = font.render(str(click_count1), True, RED)
    score_rect1 = text_score1.get_rect(center=(560,HEIGHT - 92))
    screen.blit(text_score1, score_rect1)

    text_score2 = font.render(str(click_count2), True, BLUE)
    score_rect2 = text_score2.get_rect(center=(560,HEIGHT - 62))
    screen.blit(text_score2, score_rect2)

    text_score3 = font.render(str(click_count3), True, (0, 255, 0))
    score_rect3 = text_score3.get_rect(center=(560,HEIGHT - 32))
 
    screen.blit(text_score3, score_rect3)
    if game_paused:
        # print(game_paused)
        font = pygame.font.Font(None, 60)
        text_score3 = font.render("Game end!!!", True, (0, 255, 0))
        score_rect3 = text_score3.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text_score3, score_rect3)

    # Update the GUI
    manager.update(1 / 60.0)
    manager.draw_ui(screen)

    # Update the display
    pygame.display.flip()

    if countdown_complete == True:
        pause_game()
   
# Quit Pygame
pygame.quit()
sys.exit()

