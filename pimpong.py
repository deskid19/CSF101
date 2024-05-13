import pygame
import random
import time

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define game constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

class Ball:
    def _init_(self):
        self.reset()

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x = random.choice([-3, 3])
        self.speed_y = 3

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def check_collision(self):
        if self.x <= BALL_RADIUS or self.x >= WIDTH - BALL_RADIUS:
            self.speed_x = -self.speed_x
        if self.y <= BALL_RADIUS:
            self.speed_y = -self.speed_y

class Paddle:
    def _init_(self):
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - self.height - 10

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= 10
        elif direction == "right" and self.x < WIDTH - self.width:
            self.x += 10

class Game:
    def _init_(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ping Pong")
        self.clock = pygame.time.Clock()

        self.ball = Ball()
        self.paddle = Paddle()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
        self.start_time = 0
        self.countdown_seconds = 3  # Countdown timer duration in seconds

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

    def update(self):
        self.ball.move()
        self.ball.check_collision()

        if self.ball.y >= HEIGHT - BALL_RADIUS - PADDLE_HEIGHT:
            if self.paddle.x <= self.ball.x <= self.paddle.x + PADDLE_WIDTH:
                self.ball.speed_y = -self.ball.speed_y
                self.score += 1

    def draw(self):
        self.screen.fill(BLACK)
        pygame.draw.circle(self.screen, WHITE, (self.ball.x, self.ball.y), BALL_RADIUS)
        pygame.draw.rect(self.screen, WHITE, (self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height))
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            game_over_text = self.font.render(f"Game Over! Your score: {self.score}", True, WHITE)
            game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(game_over_text, game_over_rect)
        elif self.start_time > 0:
            # Display countdown timer
            seconds_left = self.countdown_seconds - int(time.time() - self.start_time)
            if seconds_left > 0:
                countdown_text = self.font.render(f"Starting in: {seconds_left}", True, WHITE)
                countdown_rect = countdown_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                self.screen.blit(countdown_text, countdown_rect)

        pygame.display.flip()

    def run(self):
        self.start_time = time.time()
        while not self.game_over:
            self.handle_events()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.paddle.move("left")
            elif keys[pygame.K_RIGHT]:
                self.paddle.move("right")

            if self.start_time > 0 and time.time() - self.start_time >= self.countdown_seconds:
                self.start_time = 0  # Countdown timer complete, start game

            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

if _name_ == "_main_":
    game = Game()
    game.run()