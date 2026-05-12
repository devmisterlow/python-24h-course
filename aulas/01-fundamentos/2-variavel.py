# ==========================================
# ESTUDO DE VARIÁVEIS E TIPOS DE DADOS
# ==========================================

# Variáveis do usuário
nome_usuario = "Programador Dev"

print(f"Welcome - Bem-vindo, caro usuário: {nome_usuario}")

# ==========================================
# VARIÁVEIS NUMÉRICAS
# ==========================================

media = 0.0

nota1 = nota2 = nota3 = nota4 = 0.0

# ==========================================
# VARIÁVEIS DE TEXTO E BOOLEANAS
# ==========================================

nome = "DEV"
idade = 47
booleano = True

# ==========================================
# FUNÇÃO type()
# ==========================================

print("\n========== FUNÇÃO TYPE() ==========")

print(f"Tipo da variável media: {type(media)}")
print(f"Tipo da variável nota2: {type(nota2)}")
print(f"Tipo da variável nome: {type(nome)}")
print(f"Tipo do número complexo: {type(1 + 2j)}")

# ==========================================
# FUNÇÃO isinstance()
# ==========================================

print("\n========== FUNÇÃO ISINSTANCE() ==========")

valor_inteiro = 10
texto = "Sol"

print(f"valor_inteiro é int? {isinstance(valor_inteiro, int)}")
print(f"valor_inteiro é float? {isinstance(valor_inteiro, float)}")
print(
    f"valor_inteiro é int ou float? "
    f"{isinstance(valor_inteiro, (int, float))}"
)

# ==========================================
# OPERAÇÃO MATEMÁTICA
# ==========================================

numero1 = 50
numero2 = 2

resultado = numero1 * numero2

print("\n========== OPERAÇÃO MATEMÁTICA ==========")

print(f"Operação: {numero1} * {numero2}")
print(f"Resultado da multiplicação: {resultado}")