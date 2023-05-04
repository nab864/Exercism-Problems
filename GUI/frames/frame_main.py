from customtkinter import CTkLabel, CTkButton, CTkFrame


class MainFrame(CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        label = CTkLabel(self, text="Startpage")
        label.grid(row=0, column=1, padx=10, pady=10)

        button1 = CTkButton(self, text="LeastAmountOfChange",
                            command=lambda: controller.show_frame('LeastChange'),
                            fg_color='green')
        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = CTkButton(self, text="AllYourBase",
                            command=lambda: controller.show_frame('UnderConstruction'))
        button2.grid(row=1, column=1, padx=10, pady=10)

        button3 = CTkButton(self, text="BankAccount",
                            command=lambda: controller.show_frame('UnderConstruction'))
        button3.grid(row=1, column=2, padx=10, pady=10)

        button4 = CTkButton(self, text="BookStore",
                            command=lambda: controller.show_frame('UnderConstruction'))
        button4.grid(row=2, column=0, padx=10, pady=10)

        button5 = CTkButton(self, text="Bowling",
                            command=lambda: controller.show_frame('UnderConstruction'))
        button5.grid(row=2, column=1, padx=10, pady=10)

        button6 = CTkButton(self, text="Hangman",
                            command=lambda: controller.show_frame('UnderConstruction'))
        button6.grid(row=2, column=2, padx=10, pady=10)

        button7 = CTkButton(self, text="KillerSodoku",
                            command=lambda: controller.show_frame('UnderConstruction'))
        button7.grid(row=3, column=0, padx=10, pady=10)

        button8 = CTkButton(self, text="PascalsTriangle",
                            command=lambda: controller.show_frame('UnderConstruction'))
        button8.grid(row=3, column=1, padx=10, pady=10)

        button9 = CTkButton(self, text="RationalNumbers",
                            command=lambda: controller.show_frame('RationalNumber'),
                            fg_color='green')
        button9.grid(row=3, column=2, padx=10, pady=10)