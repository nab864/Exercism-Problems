from customtkinter import CTk, CTkFrame
from frames import *


class App(CTk):
    def __init__(self):
        super().__init__()

        container = CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # iterating through a tuple consisting
        # of the different page layouts
        self.frames = {
            'MainFrame': MainFrame(container, self),
            'LeastChange': LeastAmountOfChangeFrame(container, self),
            'UnderConstruction': UnderConstructionFrame(container, self),
            'RationalNumber': RationalNumberFrame(container, self)
        }
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame('MainFrame')

        # to display the current frame passed as
        # parameter

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


app = App()
app.mainloop()
