from random import randint

melhor_caso_1e2 = [x for x in range(int(1e2))]
melhor_caso_1e3 = [x for x in range(int(1e3))]
melhor_caso_1e4 = [x for x in range(int(1e4))]
melhor_caso_1e5 = [x for x in range(int(1e5))]

pior_caso_1e2 = [int(1e2)-x-1 for x in range(int(1e2))]
pior_caso_1e3 = [int(1e3)-x-1 for x in range(int(1e3))]
pior_caso_1e4 = [int(1e4)-x-1 for x in range(int(1e4))]
pior_caso_1e5 = [int(1e5)-x-1 for x in range(int(1e5))]

caso_aleatorio_1e2 = [randint(0, int(1e2)) for p in range(0, int(1e2))]
caso_aleatorio_1e3 = [randint(0, int(1e3)) for p in range(0, int(1e3))]
caso_aleatorio_1e4 = [randint(0, int(1e4)) for p in range(0, int(1e4))]
caso_aleatorio_1e5 = [randint(0, int(1e5)) for p in range(0, int(1e5))]