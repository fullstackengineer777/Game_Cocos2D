import pygame
import pygame_gui
import sys
import time
import threading


# Initialize Pygame
pygame.init()


# Constants
# WIDTH, HEIGHT = 1200, 800
WIDTH, HEIGHT = 1800, 1000
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CIRCLE_RADIUS1 = 100
CIRCLE_RADIUS2 = 50
INITIAL_RADIUS = 50
game_mode = True
drawing = True
circle_center = (0,0)
CIRCLE_CENTER1 = [WIDTH // 2, HEIGHT // 2]
CIRCLE_CENTER2 = [WIDTH // 2, HEIGHT // 2]
# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Demo")

# Initialize Pygame GUI
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Load the custom theme
# theme = pygame_gui.core.ui_theme.UiTheme("my_theme.json")
# theme = pygame_gui.core.ui_theme.UiTheme("custom_theme.json")
# Initialize variables
dragging = False
click_count1 = 0
click_count2 = 0
click_count3 = 0
game_started = False
game_paused = False
INITIAL_TIME = 10
TOTOAL_TOUCHES = 100
total_count = 0
total_points = []
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
  
slider_rect1 = pygame.Rect(WIDTH - 220, HEIGHT/2 - 120, 200, 30)
slider1 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider_rect1, start_value=50, value_range=(1, 300), manager=manager)
label_rect1 = pygame.Rect(WIDTH - 220, HEIGHT/2 - 150, 200, 30)
slider_label1 = pygame_gui.elements.UILabel(relative_rect=label_rect1, text="Red Circle Radius:", manager=manager)

slider_rect2 = pygame.Rect(WIDTH - 220, HEIGHT/2 - 50, 200, 30)
slider2 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider_rect2, start_value=50, value_range=(1, 300), manager=manager)
label_rect2 = pygame.Rect(WIDTH - 220, HEIGHT/2 - 80, 200, 30)
slider_label2 = pygame_gui.elements.UILabel(relative_rect=label_rect2, text="Blue Circle Radius:", manager=manager)

slider_rect3 = pygame.Rect(WIDTH - 220, HEIGHT/2 - 300, 200, 30)
slider3 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider_rect3, start_value=50, value_range=(1, 300), manager=manager)
label_rect3 = pygame.Rect(WIDTH - 220, HEIGHT/2 - 330, 200, 30)
slider_label3 = pygame_gui.elements.UILabel(relative_rect=label_rect3, text="Set Time 0 ~ 5 min:", manager=manager)
slider_rect4 = pygame.Rect(WIDTH - 220, HEIGHT/2 - 300, 200, 30)
slider4 = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider_rect4, start_value=50, value_range=(1, 200), manager=manager)
label_rect4 = pygame.Rect(WIDTH - 220, HEIGHT/2 - 330, 200, 30)
slider_label4 = pygame_gui.elements.UILabel(relative_rect=label_rect4, text="Set Counter 0 ~ 200:", manager=manager)

start_button_rect = pygame.Rect(WIDTH - 200, HEIGHT - 150, 150, 50)
start_button = pygame_gui.elements.UIButton(relative_rect=start_button_rect, text="Start", manager=manager)
end_button_rect = pygame.Rect(WIDTH - 200, HEIGHT - 150, 150, 50)
end_button = pygame_gui.elements.UIButton(relative_rect=start_button_rect, text="Restart", manager=manager)
end_button.hide()

label_rect_score1 = pygame.Rect(WIDTH - 200, HEIGHT/2 + 80, 100, 30)
slider_label_score1 = pygame_gui.elements.UILabel(relative_rect=label_rect_score1, text="Red Score:", manager=manager)
label_rect_score2 = pygame.Rect(WIDTH - 200, HEIGHT/2 +  140, 100, 30)
slider_label_score2 = pygame_gui.elements.UILabel(relative_rect=label_rect_score2, text="Blue Score:", manager=manager)
label_rect_score3 = pygame.Rect(WIDTH - 200, HEIGHT/2 + 200, 100, 30)
slider_label_score3 = pygame_gui.elements.UILabel(relative_rect=label_rect_score3, text="Space Score:", manager=manager)
label_rect_score3 = pygame.Rect(WIDTH - 200, HEIGHT/2 + 20, 100, 30)
slider_label_score3 = pygame_gui.elements.UILabel(relative_rect=label_rect_score3, text="Total Score:", manager=manager)


# Define the functions for each game mode
def start_mode_a():
    global game_mode
    game_mode = False
    mode_b_button.show()
    mode_a_button.hide()
    slider3.show()
    slider_label3.show()
    slider4.hide()
    slider_label4.hide()
    print("Set Time Mode Game")

def start_mode_b():
    global game_mode
    game_mode = True
    mode_a_button.show()
    mode_b_button.hide()
    slider3.hide()
    slider_label3.hide()
    slider4.show()
    slider_label4.show()
    print("Set Total touch Mode Game")

# Create buttons for the game modes
mode_a_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((WIDTH - 220, HEIGHT/2 - 250), (200, 50)),
    text='Total Touch Mode',
    manager=manager
)

mode_b_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((WIDTH - 220, HEIGHT/2 - 250), (200, 50)),
    text='Time Mode',
    manager=manager
)

start_mode_b()

def start_countdown_thread():
    print("starting counting down thread")
    countdown_thread = threading.Thread(target=countdown_timer)
    # countdown_thread.daemon = True
    countdown_thread.start()

running = True
def countdown_timer():
    global countdown_time, game_paused
    # countdown_time = INITIAL_TIME
    while running:
        # Update the countdown timer
        countdown_time -= 1
        # Sleep for 1 second
        time.sleep(1)
        print(countdown_time)
        if(countdown_time == 0 and game_mode == False):
            pause_game()


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
    slider4.hide()
    slider_label4.hide()
    
    print(f"thread?  { game_mode }")
    global countdown_time
    countdown_time = int(slider3.get_current_value())
    global TOTOAL_TOUCHES
    TOTOAL_TOUCHES = int(slider4.get_current_value())
    print(f"TOTOAL_TOUCHES = {TOTOAL_TOUCHES}")
    if game_mode == False :
        start_countdown_thread()
    
    slider_label3.hide()

    start_button.hide()
    end_button.show()
    mode_a_button.hide()
    mode_b_button.hide()
    print(countdown_time)
    # countdown_thread.join()
    global game_paused
    game_paused = False
    
    print("aa")
    print(game_paused)
    global total_points
    total_points.clear()

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
    if(game_mode == True):
        start_mode_b()
    else:
        start_mode_a()
    start_button.show()
    end_button.hide()
    # //stop counting
    global countdown_timer
    countdown_time = -1
    global game_paused
    game_paused = False

    global total_points
    total_points.clear()
    global total_count
    total_count = 0

def pause_game():
    CIRCLE_RADIUS1 = 100
    CIRCLE_RADIUS2 = 50
    INITIAL_RADIUS = 50
    click_count1 = 0
    click_count2 = 0
    click_count3 = 0
    global game_started
    game_started = False
    print("Game Ended!")
    slider1.show()
    slider2.show()
    slider_label1.show()
    slider_label2.show()
    if(game_mode == True):
        start_mode_b()
    else:
        start_mode_a()
    end_button.show()
    start_button.hide()
    print("Timeout!!!")
    # alarm text
    global game_paused
    game_paused = True

    global countdown_time
    countdown_time = -1
    global total_count
    total_count = 0

def check_sum(center):
    # global drawing
    # drawing = True
    global circle_center
    circle_center = center
    global total_count
    total_count = total_count + 1
    print(f"total_count = {total_count}")
    global total_points
    total_points.append(center)
    if( game_mode == True) and (TOTOAL_TOUCHES <= total_count):
        pause_game()


# Main game loop
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
                            check_sum(event.pos)
                    else:
                        circle_num = 1
                        if game_started: 
                            click_count1 += 9
                            print(f"Red Circle Click Count: {click_count1}")
                            check_sum(event.pos)
                else:
                    if is_inside_circle1(x, y) :
                        dragging = True
                        circle_num = 1
                        if game_started: 
                            click_count1 += 9
                            print(f"Red Circle Click Count: {click_count1}")
                            check_sum(event.pos)
                    if is_inside_circle2(x, y) :
                        dragging = True
                        circle_num = 2 
                        if game_started: 
                            click_count2 += 4
                            print(f"Blue Circle Click Count: {click_count2}")
                            check_sum(event.pos)
                    if not is_inside_circle1(x,y) and not is_inside_circle2(x,y) and  game_started:
                        click_count3 += 5
                        circle_num = 3
                        check_sum(event.pos)
                    # update_score()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                # drawing = False
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
        if event.type  == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == slider4:
                TOTOAL_TOUCHES = int(slider4.get_current_value())


        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start_button:
                start_game()
                
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == end_button:
                restart_game()
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == mode_a_button:
                start_mode_a()
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == mode_b_button:
                start_mode_b()
        
                

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw a red circle
    pygame.draw.circle(screen, RED, CIRCLE_CENTER1, CIRCLE_RADIUS1)
    pygame.draw.circle(screen, (52, 122, 235), CIRCLE_CENTER2, CIRCLE_RADIUS2)
     # Display a message before starting the game

    font = pygame.font.Font(None, 72)
    text_score1 = font.render(str(click_count1), True, RED)
    score_rect1 = text_score1.get_rect(center=(WIDTH - 50, HEIGHT/2 + 100))
    screen.blit(text_score1, score_rect1)

    text_score2 = font.render(str(click_count2), True, (52, 122, 235))
    score_rect2 = text_score2.get_rect(center=(WIDTH - 50, HEIGHT/2 + 160))
    screen.blit(text_score2, score_rect2)

    text_score3 = font.render(str(click_count3), True, (0, 255, 0))
    score_rect3 = text_score3.get_rect(center=(WIDTH - 50, HEIGHT/2 + 220))
    screen.blit(text_score3, score_rect3)

    text_score4 = font.render(str(click_count1 + click_count2 + click_count3), True, (255,255,255))
    score_rect4 = text_score4.get_rect(center=(WIDTH - 50, HEIGHT/2 + 40))
    screen.blit(text_score4, score_rect4)


    for pt in total_points:
        pygame.draw.circle(screen, (0,255,0), pt, 5)
        

    if game_paused:
        # print(game_paused)
        font = pygame.font.Font(None, 60)
        text_score3 = font.render("Game end!!!", True, (0, 255, 0))
        score_rect3 = text_score3.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text_score3, score_rect3)

    # Update the GUI
    manager.update(1 / 60.0)
    manager.draw_ui(screen)

    # if drawing:
    #     pygame.draw.circle(screen, (0,255,0), circle_center, 5)

    # Update the display
    pygame.display.flip()

    if countdown_complete == True:
        pause_game()
   
# Quit Pygame
pygame.quit()
sys.exit()

