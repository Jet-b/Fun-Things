
def star(l = 6):
    ret = ""
    for i in range(1, l, 2):
        ret += " " * ((l-i)//2) +  i*"*" + "\n"
    for i in range(l-1, 0, -2):
        ret += " " * ((l-i)//2) +  i*"*" + "\n"
    ret = ret[:-1]
    return ret

print(star(10))