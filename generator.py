# Generator is a simple way of creating iterator.

def remote_control_next():
    yield "cnn"
    yield "espn"

iter = remote_control_next()
print(iter)
print(next(iter))
print(next(iter))