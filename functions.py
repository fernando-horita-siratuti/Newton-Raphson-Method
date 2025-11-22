def calcula_raiz(f, derivada, x_inicial, epsilon, max_iter, casas_decimais = 6):
    """
    Parâmetros:
    f (sympy.expression): A função cuja raiz deseja-se calcular.
    derivada (sympy.expression): A derivada da função f.
    x_inicial (float): O valor inicial de x.
    epsilon (float): O erro máximo permitido.
    max_iter (int): O número máximo de iterações.
    casas_decimais (int): O número de casas decimais necessárias para manter o mesmo padrão para todas variáveis.

    Retorna:
    x_novo (float): A raiz da função f em x_inicial.

    Raises:
    ValueError: Se a derivada for zero ou se o número máximo de iterações for atingido sem convergência.
    """
    x = x_inicial

    print('\n---------- Início do Método de Newton-Raphson ----------\n')
    for i in range(max_iter):
        # Calcula o valor de f(x)
        f_x = f.evalf(subs={f.free_symbols.pop(): x})

        # Calcula o valor da derivada de f(x)
        derivada_x = derivada.evalf(subs={derivada.free_symbols.pop(): x})

        # Verifica se a derivada é igual a zero
        if derivada_x == 0:
            raise ValueError("Derivada é zero. Método de Newton-Raphson falhou.")

        # Calcula o novo valor de x
        x_novo = x - f_x / derivada_x

        # Imprime o resultado da iteração atual
        print(f'Iteração {i}: x = {x:.{casas_decimais}f}, f(x) = {f.evalf(subs={f.free_symbols.pop(): x}):.{casas_decimais}f}, Erro estimado = {abs(x_novo - x):.{casas_decimais}f}\n')

        # Verifica se o erro estimado for menor que epsilon
        if abs(x_novo - x) < epsilon:
            # Se o erro for menor que epsilon, imprime a raiz encontrada e retorna
            print(f'Raiz encontrada: x = {x_novo:.{casas_decimais}f} após {i + 1} iterações.')
            return

        # Atualiza o valor de x ao fim de cada iteração
        x = x_novo

    # Se o número máximo de iterações for atingido sem convergência, levanta um ValueError
    raise ValueError("Número máximo de iterações atingido sem convergência.")