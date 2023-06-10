import yfinance as yf
import matplotlib.pyplot as plt

lista_tickers = ['SANB11.SA', 'CSAN3.SA', 'VIVT3.SA', 'SAPR11.SA']

dados = yf.download(lista_tickers, start='2020-01-01')['Close']

# Imprime as primeiras linhas dos dados
print(dados.head())

# Plota os dados
dados.plot(figsize=(10, 7))
plt.show()
