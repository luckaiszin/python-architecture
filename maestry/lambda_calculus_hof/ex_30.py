precos = [120, 45, 200, 89, 15, 300]

if __name__ == "__main__":

    precos_f = filter(lambda x: x>100,precos)
    print(list(precos_f))