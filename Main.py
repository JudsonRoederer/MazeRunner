# Maze Runner Game
__version__ = "04.03.2025"
__author__ = "Judson Roederer"



import pygame
import random

#Here are my numorous flint sessions, the first ones I used flint too much and so I had to delete my code and come up with it more on my own. https://app.flintk12.com/activity/pygame-debug-le-1fe068/session/69674867-94ca-4ab1-a891-e8922e81006d      https://app.flintk12.com/activity/pygame-debug-le-1fe068/session/009c6bf4-64e9-4159-8162-081e06c3ccf0         https://app.flintk12.com/activity/pygame-debug-le-1fe068/session/37a5ac99-b8e1-447f-8188-b8419e674a9f          https://app.flintk12.com/activity/pygame-debug-le-1fe068/session/175119e4-919d-4ec3-9009-0d20e304efec     https://app.flintk12.com/activity/pygame-debug-le-1fe068/session/fcd53aad-ce79-443d-80ac-e1ff3d966de9
#Soloman helped me in class with this project, and so did Gabriel

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


pygame.font.init()
score = 0
high_score = 0
game_over = False
show_high_score_animation = False
high_score_animation_timer = 0
HIGH_SCORE_ANIMATION_DURATION = 180
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)

ghost = pygame.image.load('images/ghost.png')

# Ghost class
#Where I have the code for the ghost

class Ghost(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, ghost_value=1):
        super().__init__()
        self.image = pygame.image.load('images/ghost.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.value = ghost_value
        self.rect = self.image.get_rect()
        self.rect.y = start_y
        self.rect.x = start_x
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


class Wall(pygame.sprite.Sprite):
#This class repersents a wall that kills the player
    """This class represents the bar at the bottom that the player controls """

    def __init__(self, x, y, width, height, color):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """
# THIS CLASS REPERSENTS THE PLAYER AND ITS HOW YOU CONTROL IT
    # Set speed vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        if block_hit_list:
            self.rect.y += self.change_y
            return "JUST_HIT_THE_WALL"


class Room(object):
    # BASE CLASS FOR THE ROOMS
    # ROOM 1,2,3 ARE SUB-CLASSES THAT SHOW WHAT EACH ROOM DOES AND IS THE CODE FOR THAT ROOM
    """ Base class for all rooms. """

    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Room1(Room):
    """This creates all the walls in room 1"""

    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, BLUE]
                 ]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room2(Room):
    """This creates all the walls in room 2"""

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 500, GREEN],
                 [590, 50, 20, 500, GREEN]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room3(Room):
    """This creates all the walls in room 3"""

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)


def main():
    #MAIN FUNCTION THIS IS WHERE ALL OF THE OTHER CODE HAPPENS
    """ Main Program """
    # Define ghost positions
    global high_score
    ghost_positions = [(100, 100), (200, 200), (323, 475), (575, 125),
                       (678, 324), (365, 765), (564, 342), (123, 528)]

    lives = 1
    score = 0
    ghost_group = pygame.sprite.Group()

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])

    # Set the title of the window
    pygame.display.set_caption('Maze Runner')

    # Create the player paddle object
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    # Create ghosts with one special ghost
    for pos in ghost_positions:
        if pos == (123, 528):
            new_ghost = Ghost(pos[0], pos[1], ghost_value=10)
        else:
            new_ghost = Ghost(pos[0], pos[1])
        ghost_group.add(new_ghost)


    done = False
    while not done:

        screen.fill(BLACK)

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)

        # --- Game Logic ---
        # CHECKS THE WALLS FOR COLLISIONS
        if pygame.sprite.spritecollide(player, current_room.wall_list, False):
            lives -= 1

            if lives == 0:
                screen.fill(BLACK)
                sound_effect = pygame.mixer.Sound('sounds/blip3.wav')
                sound_effect.play()
                gameover_text = font.render("Game Over", True, (255, 255, 255))
                screen.blit(gameover_text, (200, 200))
                if score > high_score:
                    high_score = score
                high_score_text = font.render(f'High Score: {high_score}', True, WHITE)
                screen.blit(high_score_text, (550, 80))

                pygame.display.flip()  # Make sure to update the display
                pygame.time.wait(2000)  # Wait 2 seconds to show game over


                pygame.quit()
                done = True

        # Move the player
        player.move(current_room.wall_list)

        # Update ghosts
        ghost_group.update()

        # Check for ghost collisions
        ghosts_collected = pygame.sprite.spritecollide(player, ghost_group, True)
        for collected_ghost in ghosts_collected:
            score += collected_ghost.value

        # TRANSITIONS YOU FROM ROOM TO ROOM
        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790

        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0

        # Draws everything
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
        ghost_group.draw(screen)


        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (650, 10))

        lives_text = font.render(f'Lives: {lives}', True, WHITE)
        screen.blit(lives_text, (650, 50))

        pygame.display.flip()

        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()

