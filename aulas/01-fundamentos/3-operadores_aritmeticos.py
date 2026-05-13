# =========================================================
# ESTUDO DE OPERADORES ARITMÉTICOS EM PYTHON
# =========================================================

# ---------------------------------------------------------
# REPL - READ EVAL PRINT LOOP
# ---------------------------------------------------------
# Terminal interativo do Python:
#
# python3
#
# Símbolo do terminal interativo:
# >>>
#
# Para sair:
# exit()
# ou CTRL + D
# ---------------------------------------------------------

# =========================================================
# OPERADORES ARITMÉTICOS
# =========================================================

# +   -> Soma
# -   -> Subtração
# *   -> Multiplicação
# /   -> Divisão float
# //  -> Divisão inteira
# %   -> Módulo (resto da divisão)
# **  -> Potenciação

# =========================================================
# ORDEM DE PRECEDÊNCIA
# =========================================================

# 1. Parênteses ()
# 2. Potenciação **
# 3. Multiplicação, divisão, divisão inteira e módulo
# 4. Soma e subtração
# 5. Execução da esquerda para direita

# =========================================================
# EXEMPLOS NO TERMINAL PYTHON (REPL)
# =========================================================

# >>> numero1 = 10
# >>> numero2 = 5
#
# >>> numero1 + numero2
# 15
#
# >>> numero1 - numero2
# 5
#
# >>> numero1 / numero2
# 2.0
#
# >>> numero1 // numero2
# 2
#
# >>> numero1 % numero2
# 0
#
# >>> numero1 ** numero2
# 100000

# =========================================================
# ENTRADA DE DADOS
# =========================================================

print("\n========== CALCULADORA DE SOMA ==========")

# input() sempre retorna string (str)
# Por isso usamos int() para converter os valores - Tecnica de CASTING

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

# =========================================================
# PROCESSAMENTO
# =========================================================

resultado_soma = primeiro_numero + segundo_numero

# =========================================================
# SAÍDA DE DADOS
# =========================================================

print("\n========== RESULTADO ==========")

print(
    f"A soma entre "
    f"{primeiro_numero} + {segundo_numero} "
    f"é igual a {resultado_soma}"
)