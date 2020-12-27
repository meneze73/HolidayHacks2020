"""
WELCOME TO "SANTA'S WORKSHOP" FOR HOLIDAYS HACKS 2020 
By Minnie Menezes, Alaa Hatoum, and Robert Menezes 

Original code (before modifications and personalizations) from Platformer Game in Python Arcade Library Files 
"""
import arcade
import random 

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Santa's Workshop"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
DEER_SCALING = 0.5              # STILL NEED TO APPLY THESE TO LATER IN THE CODE 
SIGN_SCALING = 0.5 

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1 
PLAYER_JUMP_SPEED = 20 

# How many pixels to keep as a minimum margin between the character and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100

# Deer Module Modifications/Possibilities 
scarvesSource = ['imagesGame/scarfBlue.png', 'imagesGame/scarfPink.png', 'imagesGame/scarfWhite.png'] 
bootsSource = ['imagesGame/bootsGreen.png', 'imagesGame/bootsRed.png', 'imagesGame/bootsYellow.png'] 
hatsSource = ['imagesGame/hatBlack.png', 'imagesGame/hatPurple.png', 'imagesGame/hatGray.png'] 

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should go into a list.
        self.correct_feed_deer_list = None 
        self.wrong_feed_deer_list = None                # ADD A STRIKE 
        self.correct_dont_feed_sign_list = None 
        self.wrong_dont_feed_sign_list = None           # ADD A STRIKE 

        self.accessories_list = None 

        self.wall_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the STRIKES 
        self.strike = 0

        # Keep track of timer --> will be ~displayed~ as countdown 
        self.total_time = 0.0

        # Load sounds
        self.CORRECT_deer_sound = arcade.load_sound("soundsGame/correctDeer.wav")       # MUST STILL APPLY THESE BELOW 
        self.CORRECT_sign_sound = arcade.load_sound("soundsGame/correctSign.wav")
        self.WRONG_sound = arcade.load_sound("soundsGame/wrong.wav")
        self.jump_sound = arcade.load_sound("soundsGame/jump.wav")

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)        # You can change the BACKGROUND COLOR HERE!! Check out the other options here: https://arcade.academy/arcade.csscolor.html#csscolor 

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # Used to keep track of our scrolling           # ---- For some reason this is identical to lines in __init__ ... 
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the STRIKE 
        self.strike = 0

        # Keep track of timer 
        self.total_time = 0.0                           # ----- ...down to here 

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.correct_feed_deer_list = arcade.SpriteList() 
        self.wrong_feed_deer_list = arcade.SpriteList()                # ADD A STRIKE 
        self.correct_dont_feed_sign_list = arcade.SpriteList() 
        self.wrong_dont_feed_sign_list = arcade.SpriteList()           # ADD A STRIKE 

        self.accessories_list = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        image_source = "imagesGame/elf_stand.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 55
        self.player_sprite.center_y = 105
        self.player_list.append(self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 2000, 64):
            ground = arcade.Sprite("imagesGame/snowMid.png", TILE_SCALING)
            ground.center_x = x
            ground.center_y = 32
            self.wall_list.append(ground)
        
        # This shows using a loop to play multiple sprites vertically 
        for x in [0, 1985]: 
            for y in range (95, 500, 64): 
                crate = arcade.Sprite("imagesGame/crate.png", TILE_SCALING)
                crate.center_x = x 
                crate.center_y = y
                self.wall_list.append(crate)

        # North Pole welcome sign 
        pole = arcade.Sprite("imagesGame/northPole.png", TILE_SCALING) 
        pole.center_x = 200
        pole.center_y = 96
        self.wall_list.append(pole)

        # Placing the locations for the DEER 
        # This shows using a coordinate list to place sprites
        float_coords_list = [[500, 196],
                           [800, 196],
                           [1100, 196],
                           [1400, 196]]

        # Deer locations 
        deer_coords_list = [[500, 96],
                           [800, 96],
                           [1100, 96],
                           [1400, 96]]

        # Sign locations 
        sign_coords_list = [[500, 255],
                           [800, 255],
                           [1100, 255],
                           [1400, 255]]

        for coordinate in float_coords_list:
            # Add a floating crate on location 
            wall = arcade.Sprite("imagesGame/snow.png", TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)
        
        for location in deer_coords_list: 
            # Add deers to positions below grounds
            deer = arcade.Sprite("imagesGame/nakedReindeer.png", DEER_SCALING)
            deer.position = location 
            self.correct_feed_deer_list.append(deer)        # ASSUME THEY ARE ALL CORRECT FOR NOW 

            scarfChoice = random.randint(0, 2)
            scarf = arcade.Sprite(scarvesSource[scarfChoice], DEER_SCALING)
            scarf.position = location 
            self.accessories_list.append(scarf)

            bootChoice = random.randint(0, 2) 
            boot = arcade.Sprite(bootsSource[bootChoice], DEER_SCALING)
            boot.position = location 
            self.accessories_list.append(boot)

            hatChoice = random.randint(0, 2)
            hat = arcade.Sprite(hatsSource[hatChoice], DEER_SCALING)
            hat.position = location 
            self.accessories_list.append(hat)
        
        # Use a loop to place the DO NOT FEED signs for our character to pick up
        for place in sign_coords_list:
            sign = arcade.Sprite("imagesGame/sign.png", SIGN_SCALING) # FIX UP PROPER SCALE, IMAGE 
            sign.position = place
            self.wrong_dont_feed_sign_list.append(sign) # --> change list as necessary 

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # --- Manage Timer --- 

        # Calculate minutes 
        minutesToGo = 2 - int(self.total_time) // 60        # MUST STILL ADD CONDITION OF RUNNING OUT OF TIME 

        # Calculate seconds by using a modulus (remainder)
        secondsToGo = 59 - int(self.total_time) % 60

        # Figure out our countdown 
        countdown = f"Time: {minutesToGo:02d}:{secondsToGo:02d}"

        #        -----

        # Draw our sprites
        self.wall_list.draw()
        self.correct_feed_deer_list.draw()
        self.wrong_feed_deer_list.draw() 
        self.correct_dont_feed_sign_list.draw()
        self.wrong_dont_feed_sign_list.draw()
        self.player_list.draw()
        self.accessories_list.draw()

        # Draw our STRIKES on the screen, scrolling it with the viewport
        strike_text = f"Strikes: {self.strike}"
        arcade.draw_text(strike_text, 10 + self.view_left, 10 + self.view_bottom, arcade.csscolor.WHITE, 18)

        # Draw our timer text on the screen, scrolling it with the viewport 
        arcade.draw_text(countdown, 870 + self.view_left, 10 + self.view_bottom, arcade.color.WHITE, 18)


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        #elif key == arcade.key.LEFT or key == arcade.key.A:                 # MIGHT HAVE TO REMOVE THIS ABILITY SO THAT PLAYERS CANNOT BACKTRACK AND EXTRA POINTS 
            #self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED            # Is there any better solution?? 
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player with the physics engine
        self.physics_engine.update()

        # See if we hit anything... 
        accessories_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.accessories_list) 
        wrong_sign_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.wrong_dont_feed_sign_list)
        correct_sign_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.correct_dont_feed_sign_list)
        wrong_deer_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.wrong_feed_deer_list)
        correct_deer_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.correct_feed_deer_list)

        # Loop through each accessory to remove it from play 
        for accessory in accessories_hit_list: 
            accessory.remove_from_sprite_lists()    # Remove accessory (no need for any extra sound or points; deer will already account for that) 
        
        # Loop through each sign to remove it --> WRONG sign 
        for Wsign in wrong_sign_hit_list: 
            Wsign.remove_from_sprite_lists() # Remove sign 
            arcade.play_sound(self.WRONG_sound)
            # Add one to the STRIKES 
            self.strike += 1
        
        # ... --> CORRECT sign 
        for Csign in correct_sign_hit_list: 
            Csign.remove_from_sprite_lists()
            arcade.play_sound(self.CORRECT_sign_sound)
        
        # Loop through each deer to remove it --> WRONG sign 
        for Wdeer in wrong_deer_hit_list:
            Cdeer.remove_from_sprite_lists()            # Remove the deer 
            arcade.play_sound(self.WRONG_deer_sound)            # Play a sound
            # Add one to the STRIKES 
            self.strike += 1

        # ... --> CORRECT DEER 
        for Cdeer in correct_deer_hit_list: 
            Cdeer.remove_from_sprite_lists()            # Remove the deer 
            arcade.play_sound(self.CORRECT_deer_sound)          # Play a sound 

        # Update timer 
        self.total_time += delta_time

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left, self.view_bottom, SCREEN_HEIGHT + self.view_bottom)

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()