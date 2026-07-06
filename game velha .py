# Criação do tabuleiro
tabuleiro = [[" " for _ in range (3) ] 

# Função para exibir o tabuleiro
def mostrar_tabuleiro
  print("\nTabuleiro:\n\n")
  for i in range(3):
    print(" | ". join(tabuleiro[i]))
    if i < 2:
  print()

# Função para verificar vitória
def verificar_vitória (jogador):
  # linhas
  for linha in tabuleiro:
    if all  (celula == jogador for lin in range
      return Ture
# Colunas
for col in range (3):
  if all(tabuleiro[lin] [col] == for lin in range(3))
    return Tuere

return False
