# IMPORTING PYTHON LIBRARY ("PYGAME")
import pygame
import random

# BALL ANIMATION
def ball_animation():

    global ball_speed_x,ball_speed_y,p1_score,p2_score,score_time
    # MOVING THE BALL
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # BOUNCING THE BALL
    if ball.bottom >= 595 or ball.top <= 5:
        pygame.mixer.Sound.play(paddle_sound) 
        ball_speed_y *= -1
    
    # INCREMENTING THE SCORE
    if ball.right >= 900:
        pygame.mixer.Sound.play(score_sound) 
        p2_score += 1
        score_time = pygame.time.get_ticks()

    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)  
        p1_score += 1
        score_time = pygame.time.get_ticks()
        

    # COLLISION WITH  RIGHT PADDLE
    if ball.colliderect(p1) and ball_speed_x > 0:
        pygame.mixer.Sound.play(paddle_sound) 
        if abs(ball.right - p1.left) < 10:
           ball_speed_x *= -1
        elif abs(ball.bottom - p1.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - p1.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    # COLLISION WITH LEFT PADDLE
    if ball.colliderect(p2) and ball_speed_x < 0:
        pygame.mixer.Sound.play(paddle_sound) 
        if abs(ball.left - p2.right) < 10:
           ball_speed_x *= -1
        elif abs(ball.bottom - p2.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - p2.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1


# PLAYER ANIMATIONS
def player_animation():

    # MOVEMENT OF PADDLES
    p1.y += p1_speed
    p2.y += p2_speed

    # BOUNDRY FOR THE PADDLES
    if p1.top <= 0:
        p1.top = 0
    if p1.bottom >= 600:
        p1.bottom = 600
    if p2.top <= 0:
        p2.top = 0
    if p2.bottom >= 600:
        p2.bottom = 600

# RESETIING THE BALL AND TIMER
def ball_restart():

    global ball_speed_x,ball_speed_y,score_time
    current_time = pygame.time.get_ticks()
    ball.center = (450,300)

    # COUNT DOWN TIMER
    if current_time - score_time < 700:
        three = game_font.render("3",True,(200,200,200))
        window.blit(three,(440,315))
    if 700 < current_time - score_time < 1400:
        two = game_font.render("2",True,(200,200,200))
        window.blit(two,(440,315))
    if 1400 < current_time - score_time < 2100:
        one = game_font.render("1",True,(200,200,200))
        window.blit(one,(440,315))

    # DELAY START
    if current_time - score_time < 2100:
        ball_speed_x,ball_speed_y = 0,0
    else:
        ball_speed_x = 7 * random.choice((1,-1))
        ball_speed_y = 7 * random.choice((1,-1))
        score_time = None

# INITIALIZING PYGAME
pygame.mixer.pre_init(44100,-16,2,400)
pygame.init()

# CREATING WINDOW
window = pygame.display.set_mode((900,600))
clock = pygame.time.Clock()

# TITLE OF WINDOW 
pygame.display.set_caption("PONG GAME") 

# GAME RECTANGLES
ball = pygame.Rect(440,290,20,20)
p1 = pygame.Rect(870,250,20,100)
p2 = pygame.Rect(10,250,20,100)

# DECLARING VARIABLES FOR SPEED OF BALL AND PADDLES
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
p1_speed = 0
p2_speed = 0

# DECLARING VARIABLES FOR SCORE
p1_score = 0
p2_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)

# IMPORTING SOUND
paddle_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.mp3")

# DECLARING VARIABLES FOR TIMER
score_time = True

# EVENT LOOP
cond = True
while cond:

# SETTING THE FRAME RATE TO 50fps
    clock.tick(50)

  # TO QUIT THE GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cond = False

# RIGHT PADDLE MOVEMENT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                p1_speed += 7
            if event.key == pygame.K_UP:
                p1_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                p1_speed -= 7
            if event.key == pygame.K_UP:
                p1_speed += 7

# LEFT PADDLE MOVEMENT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                p2_speed += 7
            if event.key == pygame.K_w:
                p2_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                p2_speed -= 7
            if event.key == pygame.K_w:
                p2_speed += 7

    ball_animation()
    player_animation()

  # VISUALS ON THE SCREEN        
    window.fill((0,0,0))
    pygame.draw.aaline(window,(255,255,255),(450,0),(450,600))
    pygame.draw.ellipse(window,(200,200,200), ball)
    pygame.draw.rect(window,(200,200,200), p1)
    pygame.draw.rect(window,(200,200,200), p2)
    p1_text = game_font.render(f"{p1_score}",True,(200,200,200))
    window.blit(p1_text,(460,10))
    p2_text = game_font.render(f"{p2_score}",True,(200,200,200))
    window.blit(p2_text,(425,10))
    if score_time:
        ball_restart()


  # UPDATING THE WINDOW
    pygame.display.update()