from os import path, getenv
from dotenv import load_dotenv
import pandas as pd
from google.oauth2 import service_account
from argparse import ArgumentParser
from dateutil.parser import parse
from google.cloud import bigquery
from datetime import datetime

load_dotenv()

BIGQUERY_DATASET_RAW = getenv("BIGQUERY_DATASET_RAW").rstrip("\n")
GOOGLE_APPLICATION_CREDENTIALS = getenv("GOOGLE_APPLICATION_CREDENTIALS")
PROJECT = getenv('PROJECT')

credentials = service_account.Credentials.from_service_account_file(
    GOOGLE_APPLICATION_CREDENTIALS
)
client = bigquery.Client(credentials=credentials, project=PROJECT)


def main( table, type_file, file):
    #Extact data
    print(f"verifiando type_file...")
    if type_file == 'csv':
        df = pd.read_csv(file)
    elif type_file == 'xls':
        df = pd.read_excel(file)
    else:
        return (print('tipo de arquivo não suportado'))

    #Transform data


    print(df.columns)
    

    print(f"Saving {BIGQUERY_DATASET_RAW}.{table} in BigQuery...")

    #Load data
    job_config = bigquery.LoadJobConfig(
            # Especifica a ação que ocorre se a tabela de destino já existir.
            write_disposition="WRITE_APPEND",
            # Ignore valores extras não representados no esquema da tabela.
            ignore_unknown_values=True,
            # Configurações do particionamento. Granularidade: dia | Campo utilizado para o particionamento: extract_at (datetime)
            # time_partitioning=bigquery.table.TimePartitioning(
            #     type_="DAY", field="extract_at_p"),
        )
    table_id = f'{PROJECT}.{BIGQUERY_DATASET_RAW}.{table}'

    job = client.load_table_from_dataframe(
            df, table_id, job_config=job_config
        )  # Make an API request

    job.result()  # Wait for job to finish
    print(f"Finished etl-from-source-to-bq...")

if __name__ == "__main__":

    parser = ArgumentParser()

    parser.add_argument("-t",
                        "--table",
                        help="Nome da tabela no bq",
                        default='dados_csv')
        
    parser.add_argument("-tf",
                        "--type_file",
                        help="tipo de arquivo para ser carregado",
                        default='csv')
    
    parser.add_argument("-f",
                        "--file",
                        help="Nome do arquivo para ser carregado",
                        default='Reviews.csv')
    
args = parser.parse_args()
try:
    table = parse(args.table)
    type_file = parse(args.type_file)
    file = parse(args.file)
except ValueError:
        print(f"O formato esta incorreto")
        exit(1)
   
    
main(table, type_file, file)
