def mydeco(fun):
    def wrapper():
        print("before function call")
        fun()
        print("after function call")
    return wrapper
@mydeco
def display():
    print("hello gopal")
display()