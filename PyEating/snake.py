import pygame, sys, random, time

# Wake
check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame successfully initliazed...")    

# Play Surface
play_surface = pygame.display.set_mode((720,460))
pygame.display.set_caption("Py Eating")

# Colors
blue = pygame.Color(175, 238, 238) #Snake
black = pygame.Color(0, 0, 0) #Score
red = pygame.Color(255, 0, 0) # End Game
white = pygame.Color(255, 255, 255) #Background
purple = pygame.Color(106, 90, 205) #Speed Food
orange = pygame.Color(255, 127, 80) #Grow Food

# FPS Controller
fps_controller = pygame.time.Clock()

# Game Variables
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [(random.randrange(1, 72)*10), (random.randrange(1, 46)*10)]
food_spawn = True
# poison_position = [(random.randrange(1, 72)*10), (random.randrange(1, 46)*10)]
# poison_spawn = True
# speed = 30 ##fps?
direction = "RIGHT"
change_to = direction
score = 0

# Game Over Function() aka: go_var
def endGame():
    style_font = pygame.font.SysFont('monaco', 72)
    go_surface = style_font.render('Game Over!', True, red)
    go_rectangle = go_surface.get_rect()
    go_rectangle.midtop = (360, 15)
    play_surface.blit(go_surface, go_rectangle)
    scoreBoard(1)
    pygame.display.flip() # Update
    time.sleep(4)
    pygame.quit() #pygame exit
    sys.exit() #console exit

# Display Score
def scoreBoard(choice = 1):
    style_font = pygame.font.SysFont('monaco', 30)
    score_surface = style_font.render('Score: {0}'.format(score), True, black)
    score_rectangle = score_surface.get_rect()
    if choice == 1:
        score_rectangle.midtop = (80, 10)
    else:
        score_rectangle.midtop = (360, 120)
    play_surface.blit(score_surface, score_rectangle)
    

# Game Logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #pygame exit
            sys.exit() #console exit
        elif event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = "RIGHT"
            if  event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = "LEFT"
            if  event.key == pygame.K_UP or event.key == ord('w'):
                change_to = "UP"      
            if  event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = "DOWN"
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Validation Direction
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    
    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10

    #Snake Mechanism !!!NOT CHECKING FOR POISON YET!!!
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()    
    if food_spawn == False:
        food_position = [(random.randrange(1, 72)*10), (random.randrange(1, 46)*10)]
    food_spawn = True

    play_surface.fill(white)
    for position in snake_body:
        pygame.draw.rect(play_surface, blue, 
        pygame.Rect(position[0], position[1], 10, 10))
    
    pygame.draw.rect(play_surface, orange, 
    pygame.Rect(food_position[0], food_position[1], 10, 10))

    if snake_position[0] > 710 or snake_position[1] < 0:
        endGame()
    if snake_position[1] > 450 or snake_position[1] < 0:
        endGame()
    
    for rec in snake_body[1:]:
        if snake_position == rec[0] and snake_position[1] == rec[1]:
            endGame()

    scoreBoard(1)
    pygame.display.flip()
    fps_controller.tick(30)

    #pyinstaller
    #executable

    #edible poison speeds up game
    #sart screen