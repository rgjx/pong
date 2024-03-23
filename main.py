import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 10

BALL_SIZE = 20
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

font = pygame.font.Font(None, 36)

def draw_paddle(paddle):
    pygame.draw.rect(screen, WHITE, paddle)

def draw_ball(ball):
    pygame.draw.circle(screen, WHITE, ball.center, BALL_SIZE)

def move_ball(ball, ball_speed):
    ball.centerx += ball_speed[0]
    ball.centery += ball_speed[1]

def reset_ball():
    return pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

def main():
    player1_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    player2_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = reset_ball()

    ball_speed = [BALL_SPEED_X, BALL_SPEED_Y]

    player1_score = 0
    player2_score = 0

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1_paddle.top > 0:
            player1_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and player1_paddle.bottom < HEIGHT:
            player1_paddle.y += PADDLE_SPEED

        if keys[pygame.K_UP] and player2_paddle.top > 0:
            player2_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and player2_paddle.bottom < HEIGHT:
            player2_paddle.y += PADDLE_SPEED

        move_ball(ball, ball_speed)

        if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
            ball_speed[0] *= -1

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] *= -1

        if ball.left <= 0:
            player2_score += 1
            ball = reset_ball()
        elif ball.right >= WIDTH:
            player1_score += 1
            ball = reset_ball()

        screen.fill(BLACK)

        draw_paddle(player1_paddle)
        draw_paddle(player2_paddle)
        draw_ball(ball)

        score_text = font.render(f"Player 1: {player1_score}  Player 2: {player2_score}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
