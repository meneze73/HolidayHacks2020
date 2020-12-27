"""
Example Game Graphics - Code from Platformer Game in Python Arcade Library Files 
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Some Coolio Game Title!"
CENTER_X = 625
CENTER_Y = 390
RADIUS = 60
LINETHICKNESS = 6
start_x = 250
start_y = 450 
Menu_Title = "Santa's Workshop"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
#COIN_SCALING = 0.5             # ALL OF THE COIN CONTENT HAS BEEN COMMENTED OUT 

class MainMenuView(arcade.View):
    def __init__(self):
           super().__init__()
           self.background = None
           self.hover = False 
           self.click = False
           self.release = False
    
    def setup(self):
        self.background = arcade.load_texture("Sprites/Main_Menu_Background.png")
        self.startButton = arcade.Sprite("Sprites/Start_Button.png", scale = 0.25,center_x= CENTER_X,center_y =CENTER_Y)


    def on_mouse_motion(self,x,y,dx,dy):
        if (CENTER_X-RADIUS)<x<(CENTER_X+RADIUS) and (CENTER_Y-RADIUS)<y<(CENTER_Y+RADIUS):
            self.hover = True
        else:
            self.hover = False
    def on_mouse_press(self,x,y,button,modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.click = True
            print("click")
        else:
            self.click = False
    def on_mouse_release(self,x,y,button,modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.release = True
            print("release")
        else:
            self.release = False       
            
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.startButton.draw()  
        arcade.draw_text("Welcome to\nSanta's Workshop",start_x,start_y,arcade.color.WHITE,50, font_name='GARA',align= "center", anchor_x= "center", anchor_y="center", bold= True)
        if self.hover == True:
            arcade.draw_circle_outline(center_x=CENTER_X,center_y= CENTER_Y,radius= RADIUS,color= arcade.color.MINT_GREEN,border_width=LINETHICKNESS)
        else:
            pass

class MyGame(arcade.View):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__()

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        #self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)        # You can change the BACKGROUND COLOR HERE!! Check out the other options here: https://arcade.academy/arcade.csscolor.html#csscolor 

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        #self.coin_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        image_source = "imagesGame/elf_stand.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 55
        self.player_sprite.center_y = 105
        self.player_list.append(self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 1250, 64):
            wall = arcade.Sprite("imagesGame/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[512, 96],
                           [256, 96],
                           [768, 96]]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite("imagesGame/signRight.png", TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()
        #self.coin_list.draw()
        self.player_list.draw()


def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    start_view = MainMenuView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()