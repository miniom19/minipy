import tkinter as tk

LARGE_FONT= ("Verdana", 12)

class ScrabbleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.title("Puntuador Scrabble")

        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Puntuador de Scrabble", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text = "visit page 1",
                            command = lambda: controller.show_frame(PageOne))
        button1.pack()
        
        button2 = tk.Button(self, text = "visit page 2",
                            command = lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page ONE", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text = "Home",
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()

        button1 = tk.Button(self, text = "visit page 2",
                            command = lambda: controller.show_frame(PageTwo))
        button1.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text = "One",
                            command = lambda: controller.show_frame(PageOne))
        button1.pack()
        
        button2 = tk.Button(self, text = "Home",
                            command = lambda: controller.show_frame(StartPage))
        button2.pack()

        
app = ScrabbleApp()
app.mainloop()
