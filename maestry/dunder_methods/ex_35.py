class Carrinho:

    def __init__(self, *_data):
        self._data = list(_data)

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):

        if key >= len(self._data):
            diferenca = key - len(self._data) + 1
            self._data.extend([None] * diferenca)
        self._data[key] = value


c1 = Carrinho("danone","suco","café")

print(len(c1))
print("suco" in c1)
print(c1[2])
c1[3] = "papel higiênico"
print(c1[3])