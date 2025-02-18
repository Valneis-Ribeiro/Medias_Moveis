def prever_direcao(precos):
      # Médias móveis com pesos diferentes
      media_curta = np.average(precos[-3:], weights=[1, 2, 3])  # Dá mais peso ao preço mais recente
      media_longa = np.average(precos[-5:], weights=[1, 2, 3, 4, 5])
  
      # Verifica a tendência recente
      tendencia = precos[-1] - precos[-3]  # Diferença entre o preço atual e 3 velas atrás
  
      # Sinal de compra (CALL) se média curta acima da longa e tendência de alta
      if media_curta > media_longa and tendencia > 0:
          return "call"
      # Sinal de venda (PUT) se média curta abaixo da longa e tendência de baixa
      elif media_curta < media_longa and tendencia < 0:
          return "put"
      else:
          return None  # Evita operar em mercado lateralizado
