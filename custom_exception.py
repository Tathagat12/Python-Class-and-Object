# try:
#     raise MemoryError("memory limit exceeded.")
# except MemoryError as e:
#     print(e)
# output : memory limit exceeded.

class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg

    def print_exception(self):
        print("User defined exception: %s" % self.msg)

# custom exception handling
try:
    raise Accident("crash between two cars")
except Accident as e:
    e.print_exception()

# finally block use
try:
    f = open("c:\\code\\data.txt")
    x = 1/0
except FileNotFoundError as e:
    print("inside except")
finally:
    f.close()




        