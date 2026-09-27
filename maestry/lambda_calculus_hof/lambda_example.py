def power_2(n):
    return n*n

p_2 = lambda x: x**2

p_t = lambda x,y: x**y

if __name__ == "__main__":
    
    a = power_2(6)
    print(a)
    print(p_2(7))
    print(p_t(3,4))