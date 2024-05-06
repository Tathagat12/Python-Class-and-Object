class Human:
    """ Human is a class that represents a human object,
        it have set of entities like properties, methods.
    """
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == 'tennis player':
            print(f"{self.name} play tennis.")
        elif self.occupation == 'actor':
            print(f"{self.name} shoots flim.")

    def speak(self):
        print(f"{self.name} says how are you?." )

tom = Human("Tom", "actor")
tom.do_work()
tom.speak()

maria = Human("Maria", "tennis player")
maria.do_work()
maria.speak()
