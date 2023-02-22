def archy_links(*args):
    print("This is archy Telegram - @VanDarkholmez")

def archy_decorator(func):
    def wrapper():
        print("Hello this is test of my decorator")
        func()
        print("Cya bastard")
    return wrapper()

archy_decorator(archy_links)