import streamlit as st
import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt
import seaborn as sns

# Função para conectar ao MongoDB e recuperar os dados
def get_data():
    client = MongoClient("mongodb://root:example@localhost:27017/")
    db = client['student_scores']
    collection = db['scores']
    data = pd.DataFrame(list(collection.find()))
    return data

# Função para plotar a distribuição dos scores
def plot_score_distribution(data, score_type):
    plt.figure(figsize=(10, 4))
    sns.histplot(data[score_type], kde=True, color='skyblue')
    plt.title(f'Distribuição dos Scores de {score_type}')
    plt.xlabel('Score')
    plt.ylabel('Frequência')
    plt.grid(True)
    st.pyplot(plt)


# Streamlit interface
def main():
    st.title('Visualizações de Dados de Scores de Alunos')

    data = get_data()

    if not data.empty:
        st.subheader('Distribuição dos Scores de Matemática')
        plot_score_distribution(data, 'math_score')

        st.subheader('Distribuição dos Scores de Leitura')
        plot_score_distribution(data, 'reading_score')

        st.subheader('Distribuição dos Scores de Escrita')
        plot_score_distribution(data, 'writing_score')


    else:
        st.error("Não há dados disponíveis")

if __name__ == '__main__':
    main()
