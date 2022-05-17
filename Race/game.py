from config.definitions import ROOT_DIR
import tkinter as tk
from PIL import ImageTk,Image
import time


class gameClass:
    def __init__(self) -> None:
        self.root=tk.Tk()
        self.root.title("Racing Game")
        self.root.state("zoomed")
        self.i=1681
        self.pic = ImageTk.PhotoImage(Image.open("background.jpg"))
        self.car_original = Image.open("car.png")
        self.car_resized = self.car_original.resize((200,200))
        self.car = ImageTk.PhotoImage(self.car_resized)
        self.myCanv = tk.Canvas(self.root,width=1920,height=500)
        self.myCanv.place(x=0,y=0)
        self.car_height = 290
        self.myCanv.create_image(self.i,250,image=self.pic)
        self.myCanv.create_image(960,self.car_height,image = self.car)


        self.snow_house_x = 1900
        self.snow_house_original_pic = Image.open("snow_house.png")
        self.snow_house_modified_pic = self.snow_house_original_pic.resize((300,300))
        self.snow_house = ImageTk.PhotoImage(self.snow_house_modified_pic)
        self.myCanv.create_image(self.snow_house_x,200,image=self.snow_house)

        self.speed=0

        self.increaseSpeedButton = tk.Button(self.root,text="Increase Speed by 1",command=lambda : self.increaseSpeed(),bg="red")
        self.increaseSpeedButton.place(x=800,y=600)

        self.decreaseSpeedButton = tk.Button(self.root,text="Decrease Speed by 1",command=lambda : self.decreaseSpeed(),bg="light green")
        self.decreaseSpeedButton.place(x=1000,y=600)
        
        

        self.speedometer = tk.Label(self.root,text=f"Speed: {self.speed} km/h")
        self.speedometer.place(x=900,y=520)
        
        self.jump_not_done = True

        self.jumpB = tk.Button(self.root,text="Jump",command=self.jump,bg="light blue")
        self.jumpB.place(x=900,y=650)
              
        
        self.showBackground()

        self.root.mainloop()

    def jump(self):
        if self.car_height <= 290 and self.jump_not_done == True and self.car_height > 200:
            self.car_height -= 2
            self.root.after(2,self.jump)
        elif self.jump_not_done == True and self.car_height == 200:
            self.jump_not_done = False
            self.root.after(2,self.jump)
        elif self.jump_not_done == False and self.car_height >= 200 and self.car_height <290:
            self.car_height += 2
            self.root.after(2,self.jump)
        elif self.jump_not_done == False and self.car_height == 290:
            self.jump_not_done = True

    def showBackground(self):
        self.myCanv.destroy()
          
        self.i -= self.speed
        self.snow_house_x -= self.speed
        self.pic = ImageTk.PhotoImage(Image.open("background.jpg"))
        self.myCanv = tk.Canvas(self.root,width=1920,height=500)
        self.myCanv.place(x=0,y=0)
        self.myCanv.create_image(self.i,250,image=self.pic)
        self.myCanv.create_image(self.snow_house_x,200,image=self.snow_house)
        self.myCanv.create_image(960,self.car_height,image = self.car)
        
        self.speedometer.config(text=f"Speed: {self.speed} km/h")
        if self.snow_house_x < -200:
            self.snow_house_x = 2400
        if self.i > 565:
            self.root.after(5,self.showBackground)
        elif self.i <= 565:
            self.i=1681
            
            self.root.after(5,self.showBackground)
        

    def increaseSpeed(self):
        self.speed += 1
        

    def decreaseSpeed(self):
        if self.speed > 0:
            self.speed -= 1

gameClass()
