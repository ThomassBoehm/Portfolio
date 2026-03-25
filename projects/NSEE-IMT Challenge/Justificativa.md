### Justificativas do Pré-Processamento para Modelagem Preditiva

Após a execução das etapas de preparação e limpeza inicial dos dados do Registro Hospitalar de Câncer (RHC/SP), o conjunto resultante passou por um pipeline de pré-processamento estruturado. O objetivo foi garantir que todas as matrizes de dados estivessem adequadas para o consumo e treinamento de modelos de *Machine Learning*, baseando-se nas seguintes premissas de engenharia de *features*:

#### 1. Seleção de *Features* e Prevenção de *Data Leakage*
Além da exclusão das colunas explicitamente solicitadas no escopo do desafio, foram removidas variáveis de identificação única e textos livres não estruturados.
* **Variáveis removidas:** `INSTITU`, `IBGE`, `TELEFONE`, `CBO`, `DESCCBO`, `IBGEATEN` e `CIDADE_INST`.
* **Racional Técnico:** Manter identificadores em um modelo preditivo não agrega poder de generalização e introduz um alto risco de *overfitting*, induzindo o algoritmo a mapear ruídos específicos do banco de dados em vez de aprender os padrões reais associados à variável de saída.

#### 2. Tratamento de Dados Ausentes (Imputação)
Algoritmos matemáticos de otimização não processam valores nulos (`NaN`). Para evitar a perda massiva de dados por exclusão de linhas (listwise deletion), adotou-se a seguinte estratégia de imputação:
* **Variáveis Numéricas Contínuas (ex: `IDADE`):** Preenchimento utilizando a **mediana**. Diferente da média, a mediana é uma medida estatística robusta e resistente à distorção geométrica causada por possíveis *outliers* (valores atípicos) na base de saúde.
* **Variáveis Categóricas (ex: `DRS`):** Substituição dos nulos pela categoria sintética `'Desconhecido'`. Isso garante a integridade estrutural do *DataFrame* e permite que o modelo mapeie se a própria ausência de informação possui algum peso preditivo estatístico.

#### 3. Transformação de Variáveis Categóricas (*One-Hot Encoding*)
Para que as características qualitativas nominais pudessem ser processadas de forma vetorial, aplicou-se a técnica de *One-Hot Encoding*.
* **O Método:** Utilizou-se a função `pd.get_dummies()`, transformando categorias de texto puro em matrizes binárias isoladas (`0` e `1`).
* **Racional Técnico:** Essa abordagem evita o problema da falsa ordinalidade (onde o modelo interpreta erroneamente que uma categoria convertida para "3" tem mais peso matemático que uma categoria "1"). O parâmetro `drop_first=True` foi ativado para eliminar a primeira coluna gerada de cada categoria, prevenindo a multicolinearidade perfeita (*Dummy Variable Trap*), o que é vital para a estabilidade de modelos lineares.

#### 4. Padronização da Variável Alvo (*Target*)
A variável de saída `obito` foi isolada com sucesso a partir da coluna `ULTINFO`.
* **Mapeamento Binário:** As categorias indicativas de vida (1 e 2) foram convertidas para a classe majoritária `0`, e as categorias de óbito (3 e 4) para a classe de interesse `1`.
* **Resultado:** O conjunto de dados agora possui a matriz de *features* ($X$) estritamente numérica, tratada e separada do vetor alvo ($y$), estando pronto para consumo imediato pelo estimador.