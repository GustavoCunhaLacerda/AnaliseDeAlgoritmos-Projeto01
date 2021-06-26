from typing import List


def bubble_sort(vetor: List[int]) -> List[int]:
    n: int = len(vetor)
    for passnum in range(n-1, 0, -1):
        for i in range(passnum):
            if vetor[i] > vetor[i+1]:
                temp: int = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = temp