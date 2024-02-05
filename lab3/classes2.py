class Shape:
    def get_user_input(self):
        self.input_val = int(input())

class Square(Shape):
    def __init__(self):
        super().__init__()
        self.length = None

    def calculate_area(self):
        return self.length ** 2

    def get_user_input(self):
        super().get_user_input()
        self.length = self.input_val

square_instance = Square()

square_instance.get_user_input()

area_result = square_instance.calculate_area()

print("Area of the square:", area_result)
