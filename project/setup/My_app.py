def func_one():
    z = 0
    info_list = []
    while z <= 5:
        z += 1
        y = input("input here : ")
        info_list.append(y)
    return info_list


def func_two(vals):
    for i in vals:
        return i


if __name__ == '__main__':
    print(func_one())
    print(func_two(func_one()))
