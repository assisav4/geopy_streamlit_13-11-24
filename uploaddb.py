import pandas as pd
from pymongo import MongoClient

# Conexão com o MongoDB
client = MongoClient("mongodb://root:example@localhost:27017/")
db = client['student_scores']  # Nome do banco de dados
collection = db['scores']  # Nome da coleção

# Lendo o arquivo CSV
data = pd.read_csv("Cleaned_Students_Performance.csv")  

# Convertendo DataFrame para formato dicionário
data_dict = data.to_dict("records")

# Inserindo dados no MongoDB
collection.insert_many(data_dict)

print("Dados inseridos com sucesso!")
