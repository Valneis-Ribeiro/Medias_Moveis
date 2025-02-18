def prever_direcao(precos):
        media_curta = np.mean(precos[-3:])
        media_longa = np.mean(precos[-5:])
        return "call" if media_curta > media_longa else "put"
