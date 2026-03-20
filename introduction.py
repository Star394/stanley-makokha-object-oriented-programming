class student:
    #constructor to initialize object
    def __init__(self, name, age):
        self.name = name
        self.age = age

        #method (behavior)
        def display_info(self):
            print("Name:", self.name)
            print("Age:", self.age)

            #creating objects (instances of the class)
            student1 = student("Velma", 18)
            student2 = student("Stanley", 22)

            #accessing object methods
            student1.display_info()
            print("------")
            student2.display_info()