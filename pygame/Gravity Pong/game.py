import pygame as pg
import time
from player import Player
from ball import Ball
from physics_object import PhysicsObject
import gui_classes as gui
from debug import debug
from debug import kinematics_info

class Game():
    def __init__(self):
    # initialise pygame
        pg.init()
    # set game loop states
        self.running, self.playing = True, False
        self.LPLAYER_UP_KEY, self.LPLAYER_DOWN_KEY, self.RPLAYER_UP_KEY, self.RPLAYER_DOWN_KEY, self.PLAYER_LEFT_KEY,self.PLAYER_RIGHT_KEY, self.START_KEY = False, False, False, False, False, False, False
    # set screen
        self.screen = pg.display.set_mode((1000, 600)) # initialise Screen Surface
        screen_centre_x = (self.screen.get_width() / 2) - 12.5
        screen_centre_y = (self.screen.get_height() / 2) - 12.5
    # set clock
        #self.FPS = 30  # set frames per second
        self.clock = pg.time.Clock()
    # variables
        self.ball_speed = 200
        self.screen_colour = (50, 50, 50)
        self.paddle_colour = (255, 255, 255)
        self.lplayer_score = 0
        self.rplayer_score = 0
    
    # DEFINE ACTORS
        self.actor_list = pg.sprite.Group()  # declare lplayer list as sprite group
        self.player_list = pg.sprite.Group()
        self.ball_list = pg.sprite.Group()
    # PLAYERS
        self.paddle_img = pg.image.load('sprites/paddle.png').convert()  # load image
    # setup left player
        self.lplayer = Player(self.paddle_img, 40, 250, 0, [0,0], 0, False, 400)
        self.lplayer.add(self.actor_list, self.player_list)
    # setup right player
        self.rplayer = Player(self.paddle_img, 940, 250, 0, [0,0], 0, False, 200)
        self.rplayer.add(self.actor_list, self.player_list)
        ''' 
    # setup player ball
        self.player_ball_img = pg.image.load('sprites/red_ball_cross.png')  # load image
        self.player_ball = Player(self.player_ball_img, 500, 100, 0, 0, 10, True, 5)
        self.player_ball.add(self.actor_list, self.player_list)
        '''
    # BALLS
    # setup hit ball
        self.hit_ball_img = pg.image.load('sprites/red_ball.png').convert_alpha()  # load image
        self.hit_ball = Ball(self.hit_ball_img, 700, 300, self.ball_speed, [1,1], 10, True)
        self.hit_ball.add(self.actor_list, self.ball_list)
    # setup hit ball 2
        self.hit_ball_img2 = pg.image.load('sprites/yellow_ball.png')  # load image
        self.hit_ball2 = Ball(self.hit_ball_img2, 740, 300, 200, [1,1], 10, True)
        self.hit_ball2.add(self.actor_list, self.ball_list)
    # setup hit ball 3
        self.hit_ball_img3 = pg.image.load('sprites/green_ball.png')  # load image
        self.hit_ball3 = Ball(self.hit_ball_img3, 400, 300, 200, [1,1], 10, True)
        self.hit_ball3.add(self.actor_list, self.ball_list)
    # setup hit ball 4
        self.hit_ball_img4 = pg.image.load('sprites/blue_ball.png')  # load image
        self.hit_ball4 = Ball(self.hit_ball_img4, 500, 200,200, [1,1], 10, True)
        self.hit_ball4.add(self.actor_list, self.ball_list)
    # setup hit ball 5
        self.hit_ball_img5 = pg.image.load('sprites/purple_ball.png')  # load image
        self.hit_ball5 = Ball(self.hit_ball_img5, 500, 500, 200, [1,1], 10, True)
        self.hit_ball5.add(self.actor_list, self.ball_list)
    
    # setup gravity well
        self.gravity_well_img = pg.image.load('sprites/black_hole.png')
        self.gravity_well = PhysicsObject(self.gravity_well_img, screen_centre_x, screen_centre_y, 0, 0, 0, False)
        self.gravity_well.add(self.actor_list)

        self.font = pg.font.SysFont(None, 50)
        self.scoreboard = gui.Text("Left_Player: {}    Right_Player: {}".format(self.lplayer_score, self.rplayer_score), self.font, (255, 255, 255), 250, 20)

    def game_loop(self):
        previous_time = time.time()
        while self.playing: # the game loop
        # calculate delta time
            dt = time.time() - previous_time
            previous_time = time.time()
            FPS = round(dt,4)
        # player input handling
            self.check_events() #check for player interaction
            self.lplayer.control_player(self.LPLAYER_UP_KEY, self.LPLAYER_DOWN_KEY)  # convert player interaction into velocity
            self.rplayer.control_player(self.RPLAYER_UP_KEY, self.RPLAYER_DOWN_KEY)
            #self.player_ball.control_player(self.RPLAYER_UP_KEY, self.RPLAYER_DOWN_KEY, self.PLAYER_LEFT_KEY, self.PLAYER_RIGHT_KEY)
        # physics updates
            for ball in self.ball_list:
                ball.ball_bounce(self.screen)
                ball.goal_collision(self.screen, self)
            for object in self.actor_list:
                object.update(dt, True, self.gravity_well) #update physics bodies
                if object not in self.ball_list:
                    for ball in self.ball_list:
                        ball.object_rebound(object)
            for player in self.player_list:
                    player.boundary_collision(self.screen)
           
                
            
        # draw game objects onto display surface
            self.screen.fill(self.screen_colour) # set background colour
            self.scoreboard.text = "Left_Player: {}    Right_Player: {}".format(self.lplayer_score, self.rplayer_score)
            self.scoreboard.draw_text(self.screen) # draw scoreboard text onto display surface
            self.actor_list.draw(self.screen) # display actors on screen
        # DEBUGGING
            debug("delta time: {}".format(dt))
            debug("FPS: {}".format(FPS), 25)
            debug("Player Left Pos: {}, Velocity: {}, Direction: {}".format(self.lplayer.position, self.lplayer.velocity, self.lplayer.direction), 50)
            debug("Player Right Pos: {}, Velocity: {}, Direction: {}".format(self.rplayer.position, self.rplayer.velocity, self.rplayer.direction), 75)
            debug("Ball Pos: {}, Velocity: {}, Direction: {}".format(self.hit_ball.position, self.hit_ball.velocity, self.hit_ball.direction), 100)
            #kinematics_info(self.hit_ball, self.screen, arrows=True)
        # update display
            pg.display.update() # update the display
        # clock/fps
            self.clock.tick(60) #tick clock
            

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False  # turns off game
                # left player
                if event.key == pg.K_w:
                    self.LPLAYER_UP_KEY = True
                if event.key == pg.K_s:
                    self.LPLAYER_DOWN_KEY = True
                # right player
                if event.key == pg.K_UP:
                    self.RPLAYER_UP_KEY = True
                if event.key == pg.K_DOWN:
                    self.RPLAYER_DOWN_KEY = True
                # ball player
                if event.key == pg.K_LEFT:
                    self.PLAYER_LEFT_KEY = True
                if event.key == pg.K_RIGHT:
                    self.PLAYER_RIGHT_KEY = True
            if event.type == pg.KEYUP:
                # left player
                if event.key == pg.K_w:
                    self.LPLAYER_UP_KEY = False
                if event.key == pg.K_s:
                    self.LPLAYER_DOWN_KEY = False
                # right player
                if event.key == pg.K_UP:
                    self.RPLAYER_UP_KEY = False
                if event.key == pg.K_DOWN:
                    self.RPLAYER_DOWN_KEY = False
                # ball player
                if event.key == pg.K_LEFT:
                    self.PLAYER_LEFT_KEY = False
                if event.key == pg.K_RIGHT:
                    self.PLAYER_RIGHT_KEY = False