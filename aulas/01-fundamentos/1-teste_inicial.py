# Exemplo básico
print('Olá Mundo')

# Quebra de linha com caractere especial
print('\nPara salvar de forma automática o arquivo .py')

# Usando aspas duplas
print("Clique em [ File > Auto Save ]")

# Misturando aspas (útil para evitar erro de sintaxe)
print('Clique em Extension > Code Runner "ícone - engrenagem" > Settings > Code Runner: Run In terminal')

# Texto multilinha (aspas triplas)
print("""Passos:
- File > Auto Save
- Extension > Code Runner
- Ativar: Run In Terminal
""")

print("Tipos de delimitação de strings e usos\n")

print("Nº | Símbolo            | Nome                | Para que serve")
print("---|--------------------|---------------------|--------------------------------------------------------------")

print("1  | ' '                | Aspas simples       | Usadas para definir textos (strings). Ideal quando não há aspas simples dentro do texto.")
print('2  | " "                | Aspas duplas        | Também definem textos. Útil quando o texto contém aspas simples internamente.')
print("3  | ` `                | Crase (backtick)    | Não é usada para strings em Python moderno. Em versões antigas (Python 2), era usada para representação (repr). Hoje é obsoleta.")
print("4  | ''' ''' ou \"\"\" \"\"\" | Aspas triplas       | Usadas para textos multilinha + (strings longas ou documentação).")

print('\nPoderiamos formatar isso com tabulate ou alinhar dinamicamente com format() / f-strings mas é assunto futuro\n')
print('têm o papel principal de definir strings, mas o uso prático vai além de “apenas texto simples”.')
print("""1 - Definição de mensagens e dados
           -| nome = "João"
            | mensagem = \'Bem-vindo ao sistema\'""")
print("""2 - Evitar conflito de aspas (uso estratégico)
           -| frase = "Ele disse: \'Olá\'" 
            |        OU 
            |frase = \'Ele disse: "Olá"\'
            
            Aqui você escolhe o delimitador para evitar escape (\\).""")
print("""3 - Strings multilinha (documentação e blocos)
           -| texto = \"\"\"Linha 1
                Linha 2
                Linha 3\"\"\"
            | Usados para: textos longos, SQL queries, HTML, JSON embutido""")
print("""4 - Docstrings (documentação de código)  
    def somar(a, b): 
        \"\"\" Retorna a soma de dois números. \"\"\" 
        return_ a + b 
        
    Isso não é só texto — o Python armazena isso em __doc__.
    """)
print("""5 - Templates e formatação
          -|nome = "Maria"
           |print(f"Olá, {nome}!") 
           
           Aqui entra outro conceito: f-strings, mas ainda usando aspas como delimitador.""")
print("""6 - Strings com caracteres especiais
           -|caminho = "C:\\Users\\Admin"
            |quebra = "Linha 1\nLinha 2" """)
print("""7 - Sobre a crase ( )
    - Não tem função em Python moderno
    - Era usada no Python 2 como atalho para repr()
    - Hoje: evite completamente 
    - 
    - Crase ` `
        -- Obsoleta (não usar) """)