#!/usr/bin/env python
# coding: utf-8

# <img src="https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/media/logo/newebac_logo_black_half.png" alt="ebac-logo">
# 
# ---
# 
# # **Módulo** | Python: Programação Orientada a Objetos
# Caderno de **Exercícios**<br> 
# Professor [André Perez](https://www.linkedin.com/in/andremarcosperez/)
# 
# ---

# # **Tópicos**
# 
# <ol type="1">
#   <li>Um pouco de teoria;</li>
#   <li>Classes;</li>
#   <li>Objetos;</li>
#   <li>Herança.</li>
# </ol>

# ---

# # **Exercícios**

# ## 0\. Preparação do ambiente

# Neste exercício vamos trabalhar com os arquivos de csv e texto definidos abaixo. Execute cada uma das células de código para escrever os arquivos na sua máquina virtual.

# * **carros.csv**: arquivo csv com informações sobre carros (venda, manutenção, portas, etc.).

# In[1]:


get_ipython().run_cell_magic('writefile', 'carros.csv', 'id,valor_venda,valor_manutencao,portas,pessoas,porta_malas\n1,vhigh,med,2,2,small\n2,med,vhigh,2,2,small\n3,low,vhigh,2,2,small\n4,low,high,2,2,small\n5,low,high,2,2,small\n6,low,high,4,4,big\n7,low,high,4,4,big\n8,low,med,2,2,small\n9,low,med,2,2,small\n10,low,med,2,2,small\n11,low,med,4,4,big\n12,low,low,2,2,small\n13,low,low,4,4,small\n14,low,low,4,4,med\n')


# * **musica.txt**: arquivo texto com a letra da música Roda Viva do Chico Buarque.

# In[2]:


get_ipython().run_cell_magic('writefile', 'musica.txt', 'Roda Viva\nChico Buarque\n\nTem dias que a gente se sente\nComo quem partiu ou morreu\nA gente estancou de repente\nOu foi o mundo então que cresceu\nA gente quer ter voz ativa\nNo nosso destino mandar\nMas eis que chega a roda viva\nE carrega o destino pra lá\n\nRoda mundo, roda-gigante\nRoda moinho, roda pião\n\nO tempo rodou num instante\nNas voltas do meu coração\nA gente vai contra a corrente\nAté não poder resistir\nNa volta do barco é que sente\nO quanto deixou de cumprir\nFaz tempo que a gente cultiva\nA mais linda roseira que há\nMas eis que chega a roda viva\nE carrega a roseira pra lá\n\nRoda mundo, roda-gigante\nRoda moinho, roda pião\n')


# ---

# ## 1\. Classe para ler arquivos de texto

# Crie a classe `ArquivoTexto`. Ela deve conter os seguintes atributos:
# 
# *   `self.arquivo`: Atributo do tipo `str` com o nome do arquivo;
# *   `self.conteudo`: Atributo do tipo `list` onde cada elemento é uma linha do arquivo;
# 
# A classe também deve conter o seguinte método:
# 
# *   `self.extrair_conteudo`: Método que realiza a leitura do arquivo e retorna o conteúdo.
# 
# *   `self.extrair_linha`: Método que recebe como parâmetro o número da linha e retorna a linha do conteúdo.
# 

# In[3]:


class ArquivoTexto:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        with open(arquivo, 'r') as f:
            self.conteudo = f.readlines()

    def extrair_linha(self, numero_linha):
        return self.conteudo[numero_linha - 1]
class ArquivoTexto:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        with open(arquivo, 'r') as f:
            self.conteudo = f.readlines()

    def extrair_linha(self, numero_linha):
        return self.conteudo[numero_linha - 1]


# Utilize o código abaixo para testar sua classe.

# In[4]:


arquivo_texto = ArquivoTexto(arquivo='musica.txt')

numero_linha = 1

print(arquivo_texto.extrair_linha(numero_linha=numero_linha))

# Roda Viva

numero_linha = 10

print(arquivo_texto.extrair_linha(numero_linha=numero_linha))

# Mas eis que chega a roda viva



# ---

# ## 2\. Classe para ler arquivos de csv

# Crie a classe `ArquivoCSV`. Ela deve extender (herdar) a classe `ArquivoTexto` para reaproveitar os seus atributos (`self.arquivo` e `self.conteudo`). Além disso, adicione o seguinte atributo:
# 
# *   `self.colunas`: Atributo do tipo `list` onde os elementos são os nome das colunas;
# 
# A classe também deve conter o seguinte método:
# 
# *   `self.extrair_nome_colunas`: Método que retorna o nome das colunas do arquivo.
# 
# 
# *   `extrair_coluna`: Método que recebe como parâmetro o indice da coluna e retorna o valor em questão.

# In[5]:


import csv

class ArquivoCSV(ArquivoTexto):
    def __init__(self, arquivo):
        super().__init__(arquivo)
        with open(arquivo, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            self.colunas = next(reader)

    def extrair_nome_colunas(self):
        return self.colunas

    def extrair_coluna(self, indice):
        with open(self.arquivo, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(reader)
            coluna = []
            for row in reader:
                coluna.append(row[indice])
        return coluna



# Utilize o código abaixo para testar sua classe.

# In[7]:


arquivo_csv = ArquivoCSV(arquivo='carros.csv')

numero_linha = 1

print(arquivo_csv.extrair_linha(numero_linha=numero_linha))

# id,valor_venda,valor_manutencao,portas,pessoas,porta_malas

print(arquivo_csv.colunas)

# [

# 'id',

# 'valor_venda',

# 'valor_manutencao',

# 'portas',

# 'pessoas',

# 'porta_malas'

# ]

numero_linha = 10

print(arquivo_csv.extrair_linha(numero_linha=numero_linha))

# 9,low,med,2,2,small

numero_linha = 10

numero_coluna = 2

print(

arquivo_csv.extrair_coluna_da_linha(

numero_linha=numero_linha,

numero_coluna=numero_coluna

)

)

# low



# ---

# # Exercício bônus

# 1. Classe para ler o arquivo csv
# 
# Crie a classe `ArquivoCSV2`. Ela deve extender (herdar) a classe `ArquivoTexto` para reaproveitar o seu atributos `self.arquivo` e o método `self.extrair_linha`. 
# 
# 
# A classe também deve conter o seguinte método:
# 
# *   `self.extrair_coluna_da_linha`: Método que recebe como parâmetro o numero da linha e o indice da coluna e retorna o valor em questão.

# In[9]:


import csv

class ArquivoCSV2(ArquivoTexto):
    def __init__(self, arquivo):
        super().__init__(arquivo)

    def extrair_coluna_da_linha(self, numero_linha, indice_coluna):
        with open(self.arquivo, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for i, row in enumerate(reader):
                if i == numero_linha - 1:
                    return row[indice_coluna]


# In[10]:


arquivo_csv2 = ArquivoCSV2(arquivo='carros.csv')

numero_linha = 10
indice_coluna = 2
print(arquivo_csv2.extrair_coluna_da_linha(numero_linha=numero_linha, indice_coluna=indice_coluna)) # low


# In[ ]:




