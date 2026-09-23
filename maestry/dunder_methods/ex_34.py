from ex_33 import Produto

class Produto_extended(Produto):

    def __eq__(self, other):
    
            if isinstance(other, Produto_extended):
                return self.preco == other.preco
    
            return False

    def __lt__(self, other):

        if isinstance(other, Produto_extended):
            return self.preco < other.preco

        return None
    

p1 = Produto_extended("Camiseta", 27.50)
p2 = Produto_extended("Blusinha", 27.50)

print(p1 == p2)

p3 = Produto_extended("cueca", 10)
p4 = Produto_extended("Calcinha", 12)

produtos = [p1,p2,p3, p4]

print(sorted(produtos))