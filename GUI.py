import arcade 

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
CENTER_X = 625
CENTER_Y = 390
CENTER_X1 = CENTER_X -120
CENTER_Y1 = CENTER_Y -150
RADIUS = 60
LINETHICKNESS = 6
start_x = 250
start_y = 450 
Menu_Title = "Santa's Workshop"

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

class GameOver(arcade.View):
    def on_show(self):
        self.hover = False
        self.click = False
        self.release = False
        self.background = arcade.load_texture("Sprites/Will_Ferrel_Game_over.png")
        self.startButton = arcade.Sprite("Sprites/Restart_Button.png", scale = 0.5,center_x= CENTER_X-120,center_y =CENTER_Y-150)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.startButton.draw()  
        arcade.draw_text("GAME          OVER",start_x-110,start_y,arcade.color.RED_DEVIL,75, font_name='GARA')
        arcade.draw_circle_outline(center_x=CENTER_X1,center_y= CENTER_Y1,radius= RADIUS*1.5,color= arcade.color.BLACK,border_width=LINETHICKNESS)
        if self.hover == True:
            arcade.draw_circle_filled(center_x=CENTER_X1,center_y= CENTER_Y1,radius= RADIUS*1.4,color= arcade.color.MINT_GREEN)
        else:
            pass
    
    def on_mouse_motion(self,x,y,dx,dy):
        if (CENTER_X1-RADIUS)<x<(CENTER_X1+RADIUS) and (CENTER_Y1-RADIUS)<y<(CENTER_Y1+RADIUS):
            self.hover = True
        else:
            self.hover = False
    def on_mouse_press(self,x,y,button,modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.click = True
        else:
            self.click = False
    def on_mouse_release(self,x,y,button,modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.release = True
        else:
            self.release = False
        if self.hover and self.click and self.release:
            game_view = MainMenuWindow()
            game_view.setup()
            self.window.show_view(game_view)
        else:
            pass

def main():
    window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT, Menu_Title)
    start_view =  GameOver()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
