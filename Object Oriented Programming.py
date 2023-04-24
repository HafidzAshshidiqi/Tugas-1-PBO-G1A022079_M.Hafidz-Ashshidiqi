class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print("Halo, nama saya", self.name, "dan saya", self.age, "Tahun.")

person = Person("Hafidz", 19)

person.say_hello() # output: Halo, nama saya Hafidz dan saya 19 tahun.
