# load_data_BQ
Passo a passo para carregamento de dados em tabelas do bigquery de diferentes fonte, csv, banco relacional, xlsx e etc

# Credencias
O primeiro passo será criar uma conta no GCP, após a sua conta criada vá "APIs e Serviços/credencias" e cria sua credencial vinculada a sua conta. Essa credencial permitirá você carregar suas bases de dados no Bigquey, já que fazer o upload pelo própria plataforma do GCP limita o carregamentos de arquivos de no maxímo 100MB

# Bigquery
O segundo passo ainda na plataforma do GCP, vá para Bigquery. Já existe um projeto padrão que você pode usar, ou pode optar em criar um novo. Mas independente do projeto que for usar, você terá que criar um dataset onde suas bases de dados serão carregadas e atualizadas. Cada upload, consulta feita no Bigquery será cobrada, porém o GCP fornece 90 ou 300 dolares gratuitos para serem usados no inicio.

# Upload
Aqui estarão os códigos criados em pythom para fazer o upload das bases no bigquery. Tota a configuração do organização dos repositórios também estão aqui. Não serão incluidas as credencias do autor por motivos de segurança. 
O foco estão nas principais bibliotecas para o carregamento dos dados, como: 

 - from google.oauth2 import service_account [ Autenticação das credenciais ]
-  from google.cloud import bigquery [ Caregamento dos dados no bigquery ]

# Importante 
Algumas variaveis além da credencial também são muito importantes. Essas variaveis devem ficar alocadas no arquivo .env 
BIGQUERY_DATASET_RAW [Nome do seu dataset criado no bigquery]
GOOGLE_APPLICATION_CREDENTIALS [o json da credencial criada no GCP]
PROJECT [O projeto usado no bigquery]
