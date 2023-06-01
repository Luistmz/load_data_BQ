# Carregamento de dados no BigQuery a partir de diferentes fontes


Este guia fornece um passo a passo para o carregamento de dados em tabelas do BigQuery a partir de diferentes fontes, como arquivos CSV, bancos de dados relacionais, planilhas Excel (XLSX) e outros. Siga as instruções abaixo para realizar o processo de carregamento de dados de forma eficiente.

## Credenciais

Crie uma conta no [Google Cloud Platform (GCP)](https://l1nk.dev/8R5l8).
Após criar a conta, acesse a página "APIs e Serviços" e crie uma credencial vinculada à sua conta. Essa credencial será necessária para o carregamento de bases de dados no BigQuery. Vale ressaltar que o upload de arquivos diretamente pela plataforma do GCP possui um limite máximo de tamanho de arquivo de 100 MB.

## BigQuery

Acesse a plataforma do GCP e vá para o serviço do BigQuery.
Selecione um projeto padrão existente ou crie um novo projeto.
No BigQuery, crie um dataset onde as bases de dados serão carregadas e atualizadas. É nesse dataset que você irá criar as tabelas correspondentes aos seus arquivos de dados.
Tenha em mente que cada upload e consulta feita no BigQuery será cobrado. No entanto, o GCP oferece uma quantidade limitada de créditos gratuitos para uso inicial, geralmente entre 90 e 300 dólares.

## Upload

A seguir, serão apresentados códigos em Python para realizar o upload de bases de dados no BigQuery, abrangendo diferentes tipos de arquivos. Além disso, serão apresentadas as configurações necessárias para a organização dos repositórios.

## Bibliotecas utilizadas:

#### [Python](https://www.python.org/)

```
from google.oauth2 import service_account  # Autenticação das credenciais
from google.cloud import bigquery  # Carregamento dos dados no BigQuery
```

O primeiro script principal do projeto é responsável pelo carregamento de bases de dados a partir de arquivos, como CSV ou XLSX. Os argumentos que devem ser passados para esse script são:

`table`: uma string com o nome da tabela que será atualizada ou criada no BigQuery.

`type_file`: uma string indicando o tipo de arquivo sendo carregado.

`file`: uma string com o caminho do arquivo a ser carregado.


>Importante
Além da credencial do GCP, existem algumas variáveis essenciais que devem ser definidas no arquivo `.env`:

`BIGQUERY_DATASET_RAW`: nome do dataset criado no BigQuery onde os dados serão carregados.

`GOOGLE_APPLICATION_CREDENTIALS`: caminho para o arquivo JSON contendo as credenciais criadas no GCP.

`PROJECT`: o projeto utilizado no BigQuery.
Certifique-se de definir corretamente essas variáveis antes de executar o processo de carregamento de dados no BigQuery.

>Observação: As credenciais do autor não estão incluídas neste guia por questões de segurança. Certifique-se de substituí-las pelas suas próprias credenciais ao executar o código.