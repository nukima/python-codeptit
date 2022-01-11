class rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color.lower().title()

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"{self.perimeter()} {self.area()} {self.color}"

txt = input()
tmp = txt.split()
hcn = rectangle(int(tmp[0]), int(tmp[1]), tmp[2])
print(hcn)