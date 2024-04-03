import pygame
from player import Player
from pipe import Pipe
from score import Score


WIDTH = 600
HEIGHT = 600
RUN = True
pygame.font.init()
GAME_STATUS = 'main' #main, game, menu
bg = pygame.image.load("background.jpg")


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Group Project")
clock = pygame.time.Clock()



def main():
    global RUN
    global GAME_STATUS
    high_score = 0

    image = pygame.image.load("bird.png")
    player = Player(50, 300, image, 0,(600,600))
    pipe1 = Pipe(400, 0, 20, 200, 'green', -1)
    pipe2 = Pipe(600, 0, 20, 200, 'green', -1)
    pipe3 = Pipe(800, 0, 20, 200, 'green', -1)

    pipeList = []
    pipeList.append(pipe1)
    pipeList.append(pipe2)
    pipeList.append(pipe3)

    score = Score()

    font = pygame.font.SysFont(None, 36)

    gameOver = False



    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                RUN = False

        if GAME_STATUS == 'game':

            if gameOver == False:
                screen.blit(bg, (0, 0))

                for pipe in pipeList:
                    pipe.draw(screen)
                    pipe.update(clock.tick())

                    if pipe.x < 200 and pipe.x > 198:
                        p1 = Pipe(800, 0, 20, 200, 'green', -1)
                        pipeList.append(p1)
                        p1.draw(screen)
                        p1.update(clock.tick())
                    elif pipe.x < 90 and pipe.x > 88:
                        score.add_one()

                    # pipe intersection
                    collide = pipe.intersect(player)
                    if collide:
                        gameOver = True
                        GAME_STATUS = 'menu'




                player.draw(screen)
                player.update(clock.tick())

                # if player falls down / flies too high
                if player.y > 600 or player.y < 0:
                    gameOver = True

                score_text = font.render(f"Score: {score.get_score()}", True, (0, 0, 0))
                screen.blit(score_text, (10, 10))


                pygame.display.update()
                clock.tick(60)
            else:
                #game over
                GAME_STATUS = "menu"
                gameOver = True

        elif GAME_STATUS == 'main':
            #screen.fill((0, 0, 0))
            screen.blit(bg, (0, 0))
            score_text = font.render(f"Welcome to Flappy Bird!", True, (0, 0, 0))
            text_rect = score_text.get_rect(center=(WIDTH/2, HEIGHT/2))
            begin_text = font.render("Press any key to begin!", True, (0, 0, 0))
            text_rect1 = begin_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))
            screen.blit(score_text, text_rect)
            screen.blit(begin_text, text_rect1)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    GAME_STATUS = 'game'

        elif GAME_STATUS == 'menu':
            #screen.fill((0, 0, 0))

            final = font.render(f"You lose. Your score was: {score.get_score()}", True, (0, 0, 0))
            final_rect = final.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            if score.get_score() > high_score:
                high_score = score.get_score()
            high = font.render(f"The high score is: {high_score}", True, (0, 0, 0))
            high_rect = high.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))

            again = font.render("Press any key to play again!", True, (0, 0, 0))
            again_rect = again.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))

            screen.blit(final, final_rect)
            screen.blit(again, again_rect)
            screen.blit(high, high_rect)

            pygame.display.flip()
            player.x = 50
            player.y = 300


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    player.x = 50
                    player.y = 300
                    score.reset_score()
                    for pipe in pipeList:
                        pipeList.remove(pipe)
                    pipe1 = Pipe(400, 0, 20, 200, 'green', -1)
                    pipe2 = Pipe(600, 0, 20, 200, 'green', -1)
                    pipe3 = Pipe(800, 0, 20, 200, 'green', -1)

                    pipeList = []
                    pipeList.append(pipe1)
                    pipeList.append(pipe2)
                    pipeList.append(pipe3)
                    GAME_STATUS = 'game'
                    gameOver = False



if __name__ == "__main__":
    main()
