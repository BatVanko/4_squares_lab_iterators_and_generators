# class Squares:
# def __init__(self, n):
#     self.n = n

def squares(n):
    i = 0
    while i < n:
        num = i + 1
        yield num * num
        i += 1


print(list(squares(5)))
