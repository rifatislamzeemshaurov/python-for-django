"""A tiny module of greeting functions (used in Chapter 08)."""


def say_hello(name):
    return f"Hello, {name}!"


def say_goodbye(name):
    return f"Goodbye, {name}! See you soon."


# This only runs when you run the file directly: python greetings.py
if __name__ == "__main__":
    print("You ran greetings.py directly!")
    print(say_hello("World"))
