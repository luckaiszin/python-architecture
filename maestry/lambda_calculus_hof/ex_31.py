fahrenheit = [32, 68, 100, 212]

if __name__ == "__main__":

    celsius = list(map(lambda f:(f-32)*(5/9),fahrenheit))
    print(celsius)