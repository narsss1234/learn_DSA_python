class Cookie:
    def __init__(self,color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self,color):
        self.color = color

green_cookie = Cookie("green")

print(green_cookie.get_color())

green_cookie.set_color("dark green")

print(green_cookie.get_color())