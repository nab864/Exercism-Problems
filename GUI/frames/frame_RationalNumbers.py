from customtkinter import CTkLabel, CTkButton, CTkFrame, CTkEntry, CTkComboBox
from Problems.RationalNumbers import Rational


class RationalNumberFrame(CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        return_button = CTkButton(self, text="Return",
                                  command=lambda: controller.show_frame('MainFrame'))
        return_button.grid(row=0, column=0, padx=10, pady=10)

        label = CTkLabel(self, text="FractionMath")
        label.grid(row=0, column=1, padx=10, pady=10)

        self.entry1 = CTkEntry(self)
        self.entry1.insert(0, '1/1')
        self.entry1.grid(row=1, column=0, padx=10, pady=10)
        self.label1 = CTkLabel(self, text=f'{self.get_rational_object(self.entry1)}')
        self.label1.grid(row=2, column=0, padx=10, pady=10)

        self.entry2 = CTkEntry(self)
        self.entry2.insert(0, '1/1')
        self.entry2.grid(row=1, column=2, padx=10, pady=10)

        self.label2 = CTkLabel(self, text=f'{self.get_rational_object(self.entry2)}')
        self.label2.grid(row=2, column=2, padx=10, pady=10)

        self.combo_box = CTkComboBox(self, values=['+', '-', 'x', '/', '='])
        self.combo_box.grid(row=1, column=1, padx=10, pady=10)

        self.results = CTkLabel(self, text=f'{self.calculate_fraction(self.entry1, self.entry2)}')
        self.results.grid(row=2, column=1, padx=10, pady=10)

        action_button = CTkButton(self, text='Calculate Fraction Math',
                                  command=self.update_page)
        action_button.grid(row=3, column=1, padx=10, pady=10)

    def split_entry(self, entry):
        temp_entry = entry.split('/')
        return temp_entry

    def make_rational_object(self, str_list):
        return Rational(int(str_list[0]), int(str_list[1]))

    def get_rational_object(self, entry):
        return self.make_rational_object(self.split_entry(entry.get()))

    def calculate_fraction(self, entry1, entry2):
        current_operation = self.combo_box.get()
        rational_1 = self.get_rational_object(entry1)
        rational_2 = self.get_rational_object(entry2)
        if current_operation == '+':
            return rational_1 + rational_2
        elif current_operation == '-':
            return rational_1 - rational_2
        elif current_operation == 'x':
            return rational_1 * rational_2
        elif current_operation == '/':
            return rational_1 / rational_2
        elif current_operation == '=':
            return rational_1 == rational_2


    def update_page(self, clear=True):
        self.results.destroy()
        self.results = CTkLabel(self, text=f'{self.calculate_fraction(self.entry1, self.entry2)}')
        self.results.grid(row=2, column=1, padx=10, pady=10)

