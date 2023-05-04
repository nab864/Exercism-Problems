from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkFrame
from Problems.LeastAmountOfChange import change


class LeastAmountOfChangeFrame(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        return_button = CTkButton(self, text="Return",
                                  command=lambda: controller.show_frame('MainFrame'))
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
