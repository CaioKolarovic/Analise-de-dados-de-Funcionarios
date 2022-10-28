from multiprocessing.heap import Arena
import pandas as pd
import matplotlib.pyplot as plt

# Cria os dataframes a partir das planilhas
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')
# servicos_df.info()
# print(servicos_df)
clientes_df = pd.read_csv('CadastroClientes.csv', sep = ';')
# print(clientes_df)
# clientes_df.info()  
funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep = ';', decimal = ',')
# print(funcionarios_df)
# funcionarios_df.info()

# 1 - Soma de gastos total com funcionarios
salario = funcionarios_df['Salario Base'].sum()
impostos = funcionarios_df['Impostos'].sum()
beneficios = funcionarios_df['Beneficios'].sum()
vt = funcionarios_df['VT'].sum()
vr = funcionarios_df['VR'].sum()
gastos_pessoal = salario + impostos + beneficios + vt + vr
gastos_pessoal = '{:,.2f}'.format(gastos_pessoal)
print(f'O gasto com folha de sálarios foi de: R${gastos_pessoal}')

# 2 - Faturamento da empresa
faturamento_df = servicos_df.merge(clientes_df, on='ID Cliente')
faturamento_df['Faturamento Total'] = faturamento_df['Tempo Total de Contrato (Meses)'] * faturamento_df['Valor Contrato Mensal']
faturamento_total = faturamento_df['Faturamento Total'].sum()
faturamento_total = '{:,.2f}'.format(faturamento_total)
print(f"O faturamento foi de: R${faturamento_total} ")

# 3 - Porcentagem de funcionarios com contrato
unicos_contrato = servicos_df['ID Funcionário'].unique()
quant_func = funcionarios_df['ID Funcionário'].count()
porcentagem_contrato = '{:.2%}'.format((len(unicos_contrato)/quant_func))
print(f'{porcentagem_contrato} de funcionarios possuem contrato')


# 4 - Total de contratos que cada área fechou
contratos_df = servicos_df.merge(funcionarios_df, on ='ID Funcionário')
contratos_df = contratos_df[['ID Funcionário','Area']]
# print(contratos_df)
quantidade_contratos_df = contratos_df['Area'].value_counts()
print(quantidade_contratos_df)
quantidade_contratos_df.plot(kind='bar')
plt.show()

# 5 - Total de funcionários por área
total_func_area_df = funcionarios_df['Area'].value_counts()
print(total_func_area_df)
total_func_area_df.plot(kind='bar')
plt.show()

# 6 - Ticket Médio Mensal
ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
ticket_medio = 'R${:,.2f}'.format(ticket_medio)
print(f'O ticket médio mensal é de {ticket_medio}')