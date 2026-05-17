frutas = ['apple', 'watermelon','orange']

for indice,fruta in enumerate(frutas):
    print(f"Fruta n°{indice+ 1 }: {fruta}")

print(enumerate(frutas))

"Em comparação com C/C++ para saber o indice do elemento precisariamos saber o tamanho do vetor de forma:"
"""
include <stdio.h>

int main() {
    char *frutas[] = {"maçã", "banana", "uva"};
    int tamanho = sizeof(frutas) / sizeof(frutas[0]);

    // O próprio 'i' funciona como o enumerate do Python
    for (int i = 0; i < tamanho; i++) {
        printf("Índice: %d, Fruta: %s\n", i, frutas[i]);
    }

    return 0;
}
"""

