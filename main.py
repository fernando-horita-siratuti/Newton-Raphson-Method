# Importa a biblioteca sympy para lidar com expressões matemáticas
import sympy as sp

# Importa a biblioteca math para utilizar a função log(10)
import math

# Importa a função calcula_raiz do módulo functions
from functions import calcula_raiz

# Cria um símbolo para representar a variável x
x = sp.symbols('x')

# Pede ao usuário que informe a função f(x)
f = input('Informe a função f(x): ')

# Converte a string informada pelo usuário em uma expressão matemática
f = sp.sympify(f)

# Calcula a derivada da função f em relação a x
derivada = sp.diff(f, x)

# Pede ao usuário que informe o valor inicial de x
x_inicial = float(input('Informe o valor inicial de x: '))

# Pede ao usuário que informe o valor de epsilon
epsilon = float(input('Informe o valor de epsilon: '))

# Calcula o número de casas decimais necessárias para manter o mesmo padrão para todas variáveis
casas_decimais = math.ceil(-math.log10(epsilon))

# Pede ao usuário que informe o número máximo de iterações
max_iter = int(input('Informe o número máximo de iterações: '))

# Chama a função calcula_raiz para calcular a raiz da função f em x_inicial
# com o erro epsilon e o número máximo de iterações max_iter
calcula_raiz(f, derivada, x_inicial, epsilon, max_iter, casas_decimais)