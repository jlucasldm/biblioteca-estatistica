import math

# Função auxiliar para garantir que a entrada de dados do gráfico esteja
# ordenada pelos valores das características (keys)
def ordenar_dict(data):
    aux = {}
    for i in sorted(data.keys()):
        aux[i] = data[i]
    return aux


# Recebe o dicionário com os valores do gráfico
# Retorna uma lista com todos os valores das características ordenados crescentemente
def ordered_data(data):
    data = ordenar_dict(data)
    ordered_data = []
    for i in data:
        for j in range(data[i]):
            ordered_data.append(i)
    return ordered_data

# Recebe o dicionário com os valores do gráfico
# Retorna a frequência total
def frequencia_total(data):
    data = ordenar_dict(data)
    aux = 0
    for i in data:
        aux += data[i]
    return aux

# Recebe a lista com todos os valores ds características ordenados crescentemente
# Retorna o valor da mediana
def mediana(ordered_data):
    return ordered_data[int(math.floor(len(ordered_data)/2)) - 1]

# Recebe a frequência total e o dicionário com os valores do gráfico
# Retorna o valor da média das características
def media(frequencia_total, data):
    data = ordenar_dict(data)
    aux = 0
    for i in data:
        aux += i * data[i]
    aux /= frequencia_total
    return aux

# Recebe a frequência total, a média e o dicionário com os valores do gráfico
# Retorna a variância
def variancia(frequencia_total, media, data):
    data = ordenar_dict(data)
    aux = 0
    for i in data:
        aux += data[i] * ((i - media)**2)
    aux /= frequencia_total
    return aux

# Recebe a variância
# Retorna o desvio padrão
def desvio_padrao(variancia):
    return math.sqrt(variancia)


#############################################################
####################   SEMANA 3    ##########################
#############################################################

# Recebe os valores dos quartis 1, 2 e 3
# Retorna o coeficiente de bowley
def coef_bowley(q1, q2, q3):
    return float((q3 - 2*q2 + q1)/(q3 - q1))

# Recebe os valores dos quartis 1, 2 e 3
# Retorna, em texto, a assimetria do gráfico
def assimetria(q1, q2, q3):
    if (q2 - q1) < (q3 - q2):
        return 'assimetria a direita'
    elif (q2 - q1) > (q3 - q2):
        return 'assimetria a esquerda'
    else:
        return 'simetrica'

# Recebe a lista com todos os valores ds características ordenados crescentemente,
# o comprimento dessa lista e o número desejado do cálculo sobre o gráfico (como 
# 0.25, 0.50, 0.75)
# Retorna o valor do quartil
def quartil(ordered_data, len_ordered_data, qnt_quartil):
    aux = (len_ordered_data + 1) * qnt_quartil
    if aux % int(aux) == 0:
        return ordered_data[int(aux) - 1]
    else:
        low = int(math.floor(aux))
        high = int(math.ceil(aux))
        return (ordered_data[low - 1] + ordered_data[high - 1])/2