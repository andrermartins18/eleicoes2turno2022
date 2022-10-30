
import requests
import json
import pandas as pd

posicao = []
candidato = []
votos = []
porcentagem = []

requisicao = requests.get('https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')
requisicao_dic = requisicao.json()

for dado_json in requisicao_dic['cand']:

    if dado_json['seq'] in ['1', '2']:
        posicao.append(dado_json['seq'])
        candidato.append(dado_json['nm'])
        votos.append(dado_json['vap'])
        porcentagem.append(dado_json['pvap'])
    
lista =  pd.DataFrame(list(zip(posicao, candidato, votos, porcentagem)), columns = ['Posicao', 'Candidato', 'Votos Válidos', 'Porcentagem'])

print(lista)
