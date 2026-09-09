def multi(x):
    def calculator(y):
        return y*x
    return calculator
d=multi(3)
print(d(3))