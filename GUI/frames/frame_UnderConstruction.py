from customtkinter import CTkLabel, CTkButton, CTkFrame



class UnderConstructionFrame(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = CTkLabel(self, text="This page is still under Construction.\nPlease come back later")
        label.grid(row=0, column=1, padx=10, pady=10)
        return_button = CTkButton(self, text="Return",
                                  command=lambda: controller.show_frame('MainFrame'))
        return_button.grid(row=0, column=0, padx=10, pady=10)
