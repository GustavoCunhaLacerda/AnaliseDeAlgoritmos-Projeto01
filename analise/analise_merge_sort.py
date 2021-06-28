import sys
sys.path.append('../')
import timeit
from statistics import mean

from algoritmos.merge_sort import merge_sort

def melhor_caso():
  from dados.dados_merge_sort import melhor_caso_1e2, melhor_caso_1e3, melhor_caso_1e4, melhor_caso_1e5
  
  tempo_de_execucao1 = timeit.repeat(lambda: merge_sort(melhor_caso_1e2), number=1, repeat=10)
  tempo_de_execucao2 = timeit.repeat(lambda: merge_sort(melhor_caso_1e3), number=1, repeat=10)
  tempo_de_execucao3 = timeit.repeat(lambda: merge_sort(melhor_caso_1e4), number=1, repeat=10)
  tempo_de_execucao4 = timeit.repeat(lambda: merge_sort(melhor_caso_1e5), number=1, repeat=10)
  

  print("\nMelhor caso:")
  print(f"1e2->{mean(tempo_de_execucao1)}")
  print(f"1e3->{mean(tempo_de_execucao2)}")
  print(f"1e4->{mean(tempo_de_execucao3)}")
  print(f"1e5->{mean(tempo_de_execucao4)}")

def pior_caso():
  from dados.dados_merge_sort import pior_caso_1e2, pior_caso_1e3, pior_caso_1e4, pior_caso_1e5
  
  tempo_de_execucao1 = timeit.repeat(lambda: merge_sort(pior_caso_1e2), number=1, repeat=10)
  tempo_de_execucao2 = timeit.repeat(lambda: merge_sort(pior_caso_1e3), number=1, repeat=10)
  tempo_de_execucao3 = timeit.repeat(lambda: merge_sort(pior_caso_1e4), number=1, repeat=10)
  tempo_de_execucao4 = timeit.repeat(lambda: merge_sort(pior_caso_1e5), number=1, repeat=1)

  print("\nPior caso:")
  print(f"1e2->{mean(tempo_de_execucao1)}")
  print(f"1e3->{mean(tempo_de_execucao2)}")
  print(f"1e4->{mean(tempo_de_execucao3)}")
  print(f"1e5->{mean(tempo_de_execucao4)}")

def caso_aleatorio():
  from dados.dados_merge_sort import caso_aleatorio_1e2, caso_aleatorio_1e3, caso_aleatorio_1e4, caso_aleatorio_1e5
  
  tempo_de_execucao1 = timeit.repeat(lambda: merge_sort(caso_aleatorio_1e2), number=1, repeat=10)
  tempo_de_execucao2 = timeit.repeat(lambda: merge_sort(caso_aleatorio_1e3), number=1, repeat=10)
  tempo_de_execucao3 = timeit.repeat(lambda: merge_sort(caso_aleatorio_1e4), number=1, repeat=10)
  tempo_de_execucao4 = timeit.repeat(lambda: merge_sort(caso_aleatorio_1e5), number=1, repeat=10)

  print("\nCaso aleatório:")
  print(f"1e2->{mean(tempo_de_execucao1)}")
  print(f"1e3->{mean(tempo_de_execucao2)}")
  print(f"1e4->{mean(tempo_de_execucao3)}")
  print(f"1e5->{mean(tempo_de_execucao4)}")

if __name__ == '__main__':
  print("MergeSort:")
  melhor_caso()
  pior_caso()
  caso_aleatorio()