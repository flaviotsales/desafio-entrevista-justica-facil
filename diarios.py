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

    p = re.compile(r'chamarCaptcha\(\d+')
    matches = p.findall(html)
    if len(matches) == 0:
        return None
    else:
        id = matches[0].replace('chamarCaptcha(', '')
        return id

def __getFileNameFromHeader(headers):
    return headers['Content-Disposition']\
        .replace('attachment;filename="', '')\
        .replace('"', '')\
        .replace('/', '_')

def baixaDiarioPorId(id, nomeArquivo = None):
    url = 'http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/diario.do?action=downloadDiario'
    response = requests.post(
        url,
        {
            'captchaValidacao': 'ok',
            'id': id,
            'tribunal': 'TSE'
        }
    )

    if (response.status_code == 200 and response.headers['Content-Type'] == 'application/octet-stream'):
        response.headers['Content-Type']
        if nomeArquivo == None:
            nomeArquivo = __getFileNameFromHeader(response.headers)

        with open(nomeArquivo, 'wb') as f:
            f.write(response.content)