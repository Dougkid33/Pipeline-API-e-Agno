# 🔁 Pipeline ETL com Python — API de Bitcoin + Agente AI Agno

Este projeto é um exemplo prático de **Pipeline ETL (Extração, Transformação e Carga)** construído do zero em Python. Utiliza dados da **API de Bitcoin**, passa por um processo de limpeza e transformação, calcula **KPIs importantes** e entrega uma visualização interativa com **Streamlit**. O pipeline é assistido pelo **Agente AI da Agno**, otimizando e documentando partes do processo.

## 📌 Tecnologias utilizadas

- 🐍 Python 3.10+
- 📡 API Pública de Criptomoedas (Bitcoin)
- 🤖 Agno Agent AI (assistente para automação e documentação)
- 🧮 Pandas & SQL
- 📊 Streamlit
- 💾 SQLite (ou outro backend de dados)

## 🚀 Funcionalidades

- Coleta automatizada de dados de cotação via API
- Limpeza e transformação de dados com Pandas
- Cálculo de métricas como:
  - Variação diária
  - Média móvel
  - Percentual de oscilação
- Visualização dinâmica com Streamlit
- Registro de histórico no banco de dados


## 📊 KPIs e Visualizações

O dashboard do Streamlit permite explorar os seguintes KPIs e visualizações:

* [Ex: Preço histórico do Bitcoin]
* [Ex: Variação diária]
* [Ex: Volume de negociação]
* [Ex: Média móvel de preços]
* [Ex: Insights gerados pelo Agno AI, se aplicável]

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e novas funcionalidades.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.

## 📦 Instalação

```bash
git clone https://github.com/Dougkid33/Pipeline-API-e-Agno.git
cd Pipeline-API-e-Agno
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
pip install -r requirements.txt
streamlit run app.py
