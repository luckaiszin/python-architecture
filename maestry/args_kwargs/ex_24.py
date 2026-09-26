# Unpacking Operator

def media(*args):

    if not args:
        return 0

    sum = 0
    for x in args:
        sum += x
    return sum/len(args)

if __name__ == "__main__":
    notas = [7.2, 8.3, 6.4]
    #print(notas)
    #print(*notas)
    print(f"Media: {media(*notas)}")