class Student():
    def __init__(self, name, school, color):
        self.name = name
        self.school = school
        self.fav_color = color

    def speak(self,):
        print(f"Moje oblíbená barva je {self.fav_color}")

hvezdon = Student("Hvězdoň", "Třebešín", "yellow")
rehor = Student("Řehoř", "Úžlabina", "blue")

hvezdon.speak()
