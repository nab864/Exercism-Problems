from customtkinter import *
from Problems.LeastAmountOfChange import change


class App(CTk):
    def __init__(self):
        super().__init__()

        container = CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (MainPage, LeastAmountOfChange, UnderConstruction):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

        # to display the current frame passed as
        # parameter

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class UnderConstruction(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = CTkLabel(self, text="This page is still under Construction.\nPlease come back later")
        label.grid(row=0, column=1,padx=10, pady=10)
        return_button = CTkButton(self, text="Return",
                                  command=lambda: controller.show_frame(MainPage))
        return_button.grid(row=0, column=0, padx=10, pady=10)
class MainPage(CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        label = CTkLabel(self, text="Startpage")
        label.grid(row=0, column=1, padx=10, pady=10)

        button1 = CTkButton(self, text="LeastAmountOfChange",
                            command=lambda: controller.show_frame(LeastAmountOfChange))
        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = CTkButton(self, text="AllYourBase",
                            command=lambda: controller.show_frame(UnderConstruction))
        button2.grid(row=1, column=1, padx=10, pady=10)

        button3 = CTkButton(self, text="BankAccount",
                            command=lambda: controller.show_frame(UnderConstruction))
        button3.grid(row=1, column=2, padx=10, pady=10)

        button4 = CTkButton(self, text="BookStore",
                            command=lambda: controller.show_frame(UnderConstruction))
        button4.grid(row=2, column=0, padx=10, pady=10)

        button5 = CTkButton(self, text="Bowling",
                            command=lambda: controller.show_frame(UnderConstruction))
        button5.grid(row=2, column=1, padx=10, pady=10)

        button6 = CTkButton(self, text="Hangman",
                            command=lambda: controller.show_frame(UnderConstruction))
        button6.grid(row=2, column=2, padx=10, pady=10)

        button7 = CTkButton(self, text="KillerSodoku",
                            command=lambda: controller.show_frame(UnderConstruction))
        button7.grid(row=3, column=0, padx=10, pady=10)

        button8 = CTkButton(self, text="PascalsTriangle",
                            command=lambda: controller.show_frame(UnderConstruction))
        button8.grid(row=3, column=1, padx=10, pady=10)

        button9 = CTkButton(self, text="RationalNumbers",
                            command=lambda: controller.show_frame(UnderConstruction))
        button9.grid(row=3, column=2, padx=10, pady=10)
class LeastAmountOfChange(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        return_button = CTkButton(self, text="Return",
                                  command=lambda: controller.show_frame(MainPage))
        return_button.grid(row=0, column=0, padx=10, pady=10)

        label = CTkLabel(self, text="LeastAmountOfChange")
        label.grid(row=0, column=1, padx=10, pady=10)

        self.entry = CTkEntry(self)
        self.entry.insert(0, '1')
        self.entry.grid(row=1, column=0, padx=10, pady=10)

        action_button = CTkButton(self, text='Determine Least Change',
                                  command=self.update_page)
        action_button.grid(row=1, column=1, padx=10, pady=10)
        self.results = CTkLabel(self, text=f"{self.function(float(self.entry.get()))}")
        self.results.grid(row=3, column=0, padx=10, pady=10)


    def function(self, user_input):
        return change(user_input)

    def update_page(self):
        self.results.destroy()
        self.results = CTkLabel(self, text=f"{self.function(float(self.entry.get()))}")
        self.results.grid(row=3, column=0, padx=10, pady=10)



app = App()
app.mainloop()
