# Implement remote control calss that allows you to press "next" button to go to the next.

class RemoteControl:
    def __init__(self):
        self.channels = ["Otv","Trang Tv", "Jay Jagannath", "Cn"]
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1

        if self.index == len(self.channels):
            raise StopIteration
        
        return self.channels[self.index]
    
remote = RemoteControl()
button = iter(remote)
print(next(button))
print(next(button))
print(next(button))
print(next(button))
print(next(button))

