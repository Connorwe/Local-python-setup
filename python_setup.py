print("Hello from inside a file!")


def hello():
    print("greetings user")


hello()


def pack(clothes, toothbrush, pillow):
    return [clothes, toothbrush, pillow]


print(pack("shirt", "red toothbrush", "favorite pillow"))


def eat_lunch(lunch):
    if len(lunch) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat " + lunch[0])
        for i in range(1, len(lunch)):
            print("Next I eat " + lunch[i])


eat_lunch(["pecan pie", "stawberries", "lettuce"])
