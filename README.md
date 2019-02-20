# Desafio Justiça Fácil

## Como usar

```python
import diarios

#funcionalidade principal
listMd5 = diarios.getMd5TodosTribunais('19/02/2019')

#os valores válidos para parâmetros 'tribunal' estão na lista tribunais neste mesmo módulo

#outras funções
id = diarios.getIdDiarioPorData('12/02/2019', 'TSE')
diarios.baixaDiarioPorId(id, 'TSE', 'diario.pdf')
md5 = diarios.getDiarioMd5PorData('12/02/2019', 'MG')
```

## Testes
```bash
$ python tests.py
```

# Desenvolvimento

### Tarefa 1: Procurar pelo código que exibia o captcha e descobrir o que era feito depois.
Ao analisar o código html da página, notei que o formulário de busca e selação estava carregado num iframe (que inclusive está incluso neste repositório), e ao analisar o código javascript que continha descrobri como o processo do captcha era feito, e no fim das contas ele só era validado no cliente e o formulário enviado para baixar o arquivo não precisa enviar os dados do captcha mostrado. Para conseguir os ids dos diarios, foi nessessário usar regex para pegar o id em um html retornado.

### Tarefa 2: Procurar uma biblioteca para requisições
Uma rápida pesquisa no google me levou direto à pagina da biblioteca requests, e decidir testar. Gostei da usabilidade desta e pesquisei por comparações com outras bibliotecas, e não me pareceu que havia alguma outra superior para o que precisei fazer.

### Tarefa 3: Como fazer testes de unidade em Python
Ao pesquisar 'python tests' no Google, fui levado diretamente à pagina de documentação do pacote unittest, que testei e foi muito simples de configurar e usar. Também pesquisei por 'python unit test naming convention' para nomear devidamente os métodos.

### Tarefa 4: Hash dos arquivos
Uma pesquisa me levou à essa página: https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file, que resolveu de forma simples o hash.

### Requisições lentas
Tentei algumas formas de fazer as requisições de forma assíncrona, mas não obtive sucesso da forma que gostaria. Tentei uasr a biblioteca multiprocessing e tive problemas para compartilhamento de dados 'Processos' diferentes. Até consegui fazer as requisições de forma assíncrona, mas o código resultante ficou muito complicado mesmo depois de alguma refatoração.