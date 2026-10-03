from typing import Union

def calcular_area(largura: float | int, altura: Union[int,float]) -> float:
    return float(largura*altura)

if __name__ == "__main__":
    area1 = calcular_area(5, 6.2)
    print(area1)