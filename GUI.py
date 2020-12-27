import arcade 

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
CENTER_X = 625
CENTER_Y = 390
RADIUS = 60
LINETHICKNESS = 6
start_x = 250
start_y = 450 
Menu_Title = "Santa's Workshop"
Play = False

class MainMenuWindow(arcade.View):
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

class InstructionView(arcade.View):
    def setup(self):
        self.background = arcade.load_texture("Sprites/Main_Menu_Background.png")
        self.startButton = arcade.Sprite("Sprites/Start_Button.png", scale = 0.25,center_x= CENTER_X,center_y =CENTER_Y)
    def on_show(self):
        arcade.set_background_color(arcade.color.WILD_BLUE_YONDER)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome to\nSanta's Workshop",start_x,start_y,arcade.color.BLACK_BEAN,50, font_name='GARA',align= "center", anchor_x= "center", anchor_y="center", bold= True)
    def on_mouse_press(self,x,y,button,modifiers):
        game_view = InstructionView()
        game_view.setup()
        self.window.show_view(game_view)

def main():
    window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT, Menu_Title)
    start_view =  MainMenuWindow
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
