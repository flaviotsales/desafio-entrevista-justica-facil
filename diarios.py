import requests
import re

def getDiarioMd5PorData(data: str):
    pass

def getIdDiarioPorData(data: str):
    url = 'http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/diarioTxt.do'

    response = requests.post(
        url,
        {
            'action': 'buscarDiarios',
            'voDiarioSearch.tribunal': 'TSE',
            'page': 'diarioPageTextualList.jsp',
            'voDiarioSearch.dataPubIni': data,
            'voDiarioSearch.dataPubFim': data
        }
    )
    
    html = str(response.content)

    p = re.compile('chamarCaptcha\(\d+')
    matches = p.findall(html)
    if len(matches) == 0:
        return None
    else:
        id = matches[0].replace('chamarCaptcha(', '')
        return id

def baixaDiarioPorId(id, nomeArquivo = None):
    pass