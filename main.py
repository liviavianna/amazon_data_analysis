import pandas as pd
import matplotlib.pyplot as plt

retail_orders = 'Retail.OrderHistory.1.csv'

df = pd.read_csv(retail_orders)

print(f'Você gastou o total de {sum(df['Unit Price'])} reais em compras na Amazon.')
print(f'Sua compra de valor mais alto foi {max(df['Unit Price'])} reais.')
print(f'Sua última compra foi {df['Product Name'][0]}.')


daily_orders = df.groupby('Order Date').sum()['Unit Price']
daily_orders.plot.bar(figsize=(15,5))
plt.show()