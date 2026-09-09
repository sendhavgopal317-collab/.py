def display(name):
    message=f"Hello, {name}!"
    def display_message():
        print(message)
    return display_message()
ref=display("gopal")
ref()