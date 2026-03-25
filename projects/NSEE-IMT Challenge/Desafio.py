import pandas as pd
import numpy as np
from dbfread import DBF

path = 'RHC_2000_2025_GERAL.DBF' #Caso forem testar colocar a base de dados na mesma pasta que o código
tabela_dbf = DBF(path, encoding='latin1', load=False)
#-------------------------- ETAPAS 1 A 7 -----------------------------------
filtered_registers = []

for r in tabela_dbf:
 
    cond1 = (r['TOPOGRUP'] == 'C34') and (r['UFRESID'] == 'SP')

    cond2 = (r['BASEDIAG'] == 3)
    
    cond3 = r['ECGRUP'] not in ['0', 'X', 'Y']
    
    cond4 = not (r['HORMONIO'] == 1 and r['TMO'] == 1)
    
    try:
        cond5 = (int(r['ANODIAG']) <= 2019) and (int(r['IDADE']) >= 20)
    except (ValueError, TypeError):
        cond5 = False 


    if cond1 and cond2 and cond3 and cond4 and cond5:
        filtered_registers.append(r)

df = pd.DataFrame(filtered_registers)
print(f"Total de registros após Etapas 1 a 7: {len(df)}\n")

#-------------------------- ETAPA 8 -----------------------------------

df['DTCONSULT'] = pd.to_datetime(df['DTCONSULT'], format='%d/%m/%Y', errors='coerce')
df['DTDIAG'] = pd.to_datetime(df['DTDIAG'], format='%d/%m/%Y', errors='coerce')
df['DTTRAT'] = pd.to_datetime(df['DTTRAT'], format='%d/%m/%Y', errors='coerce')


calc_diagtrat = (df['DTTRAT'] - df['DTDIAG']).dt.days
calc_tratcons = (df['DTTRAT'] - df['DTCONSULT']).dt.days
calc_consdiag = (df['DTDIAG'] - df['DTCONSULT']).dt.days

condicoes_consdiag = [
    calc_consdiag < 0,
    calc_consdiag <= 30,
    (calc_consdiag > 30) & (calc_consdiag <= 60),
    calc_consdiag > 60
]

# 0 = até 30 dias; 1 = entre 31 e 60 dias; 2 = mais de 60 dias; 3 = negativas 
valores_consdiag = [3, 0, 1, 2] 

df['CONSDIAG'] = np.select(condicoes_consdiag, valores_consdiag, default=np.nan)



condicoes_diagtrat = [
    df['DTTRAT'].isna(),  
    calc_diagtrat <= 60,
    (calc_diagtrat > 60) & (calc_diagtrat <= 90),
    calc_diagtrat > 90
]
valores_diagtrat = [3, 0, 1, 2]
# 0 = até 60 dias; 1 = entre 61 e 90 dias; 2 = mais de 90 dias; 3 = Não tratou 


df['DIAGTRAT'] = np.select(condicoes_diagtrat, valores_diagtrat, default=np.nan)



condicoes_tratcons = [
    df['DTTRAT'].isna(),  
    calc_tratcons <= 60,
    (calc_tratcons > 60) & (calc_tratcons <= 90),
    calc_tratcons > 90
]
valores_tratcons = [3, 0, 1, 2]
# 0 = até 60 dias; 1 = entre 61 e 90 dias; 2 = mais de 90 dias; 3 = Não tratou 


df['TRATCONS'] = np.select(condicoes_tratcons, valores_tratcons, default=np.nan)


#--------------------------------- ETAPA 9 -------------------------------------------- 



df['DRS'] = df['DRS'].str.extract(r'(\d+)')
df['DRS_INST'] = df['DRS_INST'].str.extract(r'(\d+)')

#--------------------------------- ETAPA 10 -------------------------------------------- 

df['ULTINFO'] = pd.to_numeric(df['ULTINFO'], errors='coerce')


df['obito'] = np.where(df['ULTINFO'].isin([3, 4]), 1, 0)


print(df['obito'].value_counts())
print()

#--------------------------------- ETAPA 11 -------------------------------------------- 


colunas_para_remover = [
    'UFNASC', 'UFRESID', 'CIDADE', 'DTCONSULT', 'CLINICA', 'DTDIAG', 
    'BASEDIAG', 'TOPOGRUP', 'DESCTOPO', 'DESCMORFO', 'T', 'N', 'M', 'PT', 
    'PN', 'PM', 'S', 'G', 'PSA', 'GLEASON', 'LOCALTNM', 'IDMITOTIC', 
    'OUTRACLA', 'META01', 'META02', 'META03', 'META04', 'DTTRAT', 'NAOTRAT', 
    'TRATAMENTO', 'TRATHOSP', 'TRATFANTES', 'TRATFAPOS', 'HORMONIO', 
    'NENHUMANT', 'CIRURANT', 'RADIOANT', 'QUIMIOANT', 'HORMOANT', 
    'TMOANT', 'IMUNOANT', 'OUTROANT', 'DTULTINFO', 'CICI', 'CICIGRUP', 
    'CICISUBGRU', 'FAIXAETAR', 'LATERALI', 'INSTORIG', 'PERDASEG', 'ERRO', 
    'DTRECIDIVA', 'RECNENHUM', 'RECLOCAL', 'RECREGIO', 'RECDIST', 'REC01', 
    'REC02', 'REC03', 'REC04', 'CIDO', 'DESCIDO', 'HABILIT', 'HABIT11', 
    'HABILIT1', 'CIDADEH', 'CIDADE_INS', 'TMO', 'MORFO', 'EC', 
    'NENHUMAPOS', 'CIRURAPOS', 'RADIOAPOS', 'QUIMIOAPOS', 'HORMOAPOS', 
    'TMOAPOS', 'IMUNOAPOS', 'OUTROAPOS', 'ULTINFO', 'DSCINST', 'RACACOR', 
    'ESTADOCIVI', 'HISTORICOB', 'HISTORICOT', 'HISTORICOC', 'RECESTROG', 
    'RECEPROG', 'RECHER2', 'P16IHQ'
]

df = df.drop(columns=colunas_para_remover, errors='ignore')

#----------------------------------PRÉ-PROCESSAMENTO--------------------------------------

# Retirando informações de identificação do paciente (LGPD)
colunas_identificacao = ['INSTITU', 'IBGE', 'TELEFONE', 'CBO', 'DESCCBO', 'IBGEATEN', 'CIDADE_INST']
df = df.drop(columns=colunas_identificacao, errors='ignore')

# Tratamento de Valores Nulos 
colunas_numericas = df.select_dtypes(include=['float64', 'int64', 'int32']).columns
colunas_categoricas = df.select_dtypes(include=['object', 'category']).columns

for col in colunas_numericas:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].median())

for col in colunas_categoricas:
    if df[col].isnull().any():
        df[col] = df[col].fillna('Desconhecido')

# --- 3. One-Hot Encoding (A transformação binária) ---
# Converte todas as colunas de texto em matrizes de 0 e 1 automaticamente
# drop_first=True evita a "Dummy Variable Trap" (multicolinearidade matemática)
df_processado = pd.get_dummies(df, drop_first=True)

# --- 4. Separação Final para o Modelo ---
# X = Features (variáveis preditivas)
# y = Target (variável alvo)
X = df_processado.drop(columns=['obito'])
y = df_processado['obito']

print(f"Formato final das features (X): {X.shape}")