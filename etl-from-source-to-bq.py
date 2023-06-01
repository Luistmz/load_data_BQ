from os import path, getenv
from dotenv import load_dotenv
import pandas as pd
from google.oauth2 import service_account
# from pandas.io.json._normalize import nested_to_record
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


def main(extract_date, table, type_file, file):
    #Extact data
    print(f"extracting data day {extract_date}...")
    if type_file == 'csv':
        df = pd.read_csv(file)
    elif type_file == 'xls':
        df = pd.read_excel(file)
    else:
        return (print('tipo de arquivo não suportado'))

    #Transform data

    # df["extract_at_p"] = df["extract_at"]
    print(df.columns)
    # df["extract_at_p"] = pd.to_datetime(df["extract_at_p"])

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

    # p = extract_date.strftime("%Y%m%d")

        # Include target partition in the table id:
    # table_id = f"soma-dl-refined-online.farm_global_europa_raw.{table}${p}"
    table_id = 'voltaic-country-384616.Dataset_raw.dados_csv'

    job = client.load_table_from_dataframe(
            df, table_id, job_config=job_config
        )  # Make an API request

    job.result()  # Wait for job to finish


if __name__ == "__main__":


    extract_date = datetime.fromisoformat("2023-02-24")  # T00:00:00-04:00')
    table = 'dados_csv'
    type_file = 'csv'
    file = 'Reviews.csv'
   
    # print(f"Starting {path.splitext(path.basename(__file__))[0]}...")
    main(extract_date, table)
    # print(f"Ended {path.splitext(path.basename(__file__))[0]}.")
