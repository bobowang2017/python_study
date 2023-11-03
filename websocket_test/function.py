import random


def random_loc(x, y):
    action = {"up", "down", "left", "right"}
    if x == 0:
        action.remove("left")
    if x == 1000:
        action.remove("right")
    if y == 0:
        action.remove("down")
    if y == 1000:
        action.remove("up")

    do_action = random.sample(action, 1)[0]
    if do_action == "up":
        return x, y + 1
    elif do_action == "down":
        return x, y - 1
    elif do_action == "left":
        return x - 1, y
    else:
        return x + 1, y


if __name__ == "__main__":
    x = 500
    y = 500
    print(f"-->({x}, {y})", end="")
    for i in range(2000):
        x1, y1 = random_loc(x, y)
        print(f"-->({x1}, {y1})", end="")
        x, y = random_loc(x1, y1)
        print(f"-->({x}, {y})", end="")