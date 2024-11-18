from sklearn.metrics import confusion_matrix
def explicar_mconf(y_teste, pred, texto_rotulos=None):
    if texto_rotulos is None:
        texto_rotulos = list(range(len(set(y_teste))))
    else:
        assert len(texto_rotulos) == len(set(y_teste)), "texto_rotulos deve conter um valor para cada classe"
        
    mc = confusion_matrix(y_teste, pred)
    acertos = 0
    total = 0
    saida = ""
    for i, linha in enumerate(mc):
        for j, n in enumerate(linha):
            if i != j and n > 0:
                if n == 1:
                    fmt = "%d exemplo  da classe %s foi   classificado  como classe %s\n"
                else:
                    fmt = "%d exemplos da classe %s foram classificados como classe %s\n"
                saida += (fmt % (n, str(texto_rotulos[i]), str(texto_rotulos[j])))
            else:
                acertos += n
            total+=n
    saida += ("%d/%d exemplos foram classificados corretamente (acurácia: %.2f%%)\n" % (acertos, total, acertos/total*100))

    return saida
