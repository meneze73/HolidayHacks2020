import arcade 

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
Menu_Title = "Santa's Workshop"

class MainMenuWindow(arcade.Window):
    def __init__(self, width, height, title,):
           super().__init__(width,height, title)
           self.set_location(400,200)
           self.background = None
    
    def setup(self):
        self.background = arcade.load_texture("Sprites/Main_Menu_Background.png")
        self.startButton = arcade.Sprite("Sprites/Start_Button.png", scale = 0.25,center_x= 700,center_y =400)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.startButton.draw()


def main():
    window = MainMenuWindow(SCREEN_WIDTH,SCREEN_HEIGHT, Menu_Title)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
