import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from PIL import ImageTk, Image
import PIL
import os
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")


        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        # use the next line if you also want to get rid of the titlebar
        self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (w, h))
        self.bind("<Escape>", exit)
        self.configure(background='#C8C9CC')

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill= "both", expand=False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self,)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            filler = 50
            frame.grid(row=0, column=0, sticky="S", ipadx= self.winfo_screenheight(), ipady=self.winfo_screenheight(), pady= 3)

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background= "white")
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=0)

        self.logo = ImageTk.PhotoImage(Image.open("assetsCNDH/Logo.PNG"))
        logoIm = tk.Label(self, image=self.logo, bg="white")
        logoIm.grid(row=0, column =2, columnspan = 1)

        self.ubi = ImageTk.PhotoImage(Image.open("assetsCNDH/Ubicacion.PNG"))
        label = tk.Label(self, image=self.ubi, font=controller.title_font, bg= "white")
        label.grid(column =2, row =2)


        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.grid(column =1, row = 3, sticky= "E")
        button2.grid(column =3, row =3, sticky= "W")




class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="green")

        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":

    app = SampleApp()
    app.mainloop()