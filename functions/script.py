from scipy.stats import ks_2samp
from scipy.stats import pearsonr
from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy import stats
import fileinput, sys
import numpy as np
import pymysql
import re

lista1 = []
lista2 = []

file = open("C:\\wamp\\www\\ProjetoFinal\\functions\\Resultados.txt", "w")

# Connect to the database
db = pymysql.connect(host='localhost', port=3306, user='root', db = 't1_beta')
cur = db.cursor()

#Shapiro-Wilk tests to verify if data sets are normal
#file.write("Comparação entre DC e MARVEL \n")
#file.write("\n")
#file.write("Os dados são normais? \n")

#file.write("\n")


#Average
#IMDB MARVEL vs IMDB DC
cur.execute("SELECT imdb_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT imdb_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)

#file.write("O resultado do teste de normalização Shapiro-Wilk para IMDB MARVEL é:\n")
auxSTR = str(shapiro(lista1))
auxSTR = auxSTR[1:]

aux = "(Shapiro-Wilk, MARVEL, IMDB, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)
#file.write("Logo, os dados são normais\n")

#file.write("O resultado do teste de normalização Shapiro-Wilk para IMDB DC é:\n")
auxSTR = str(shapiro(lista2))
auxSTR = auxSTR[1:]
aux = "(Shapiro-Wilk, DC, IMDB, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)
#file.write("Logo, os dados são normais\n")

lista1 = []
lista2 = []
#file.write("\n")

#Rottentomatoes MARVEL vs Rottentomatoes DC
cur.execute("SELECT rottentomatoes_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT rottentomatoes_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)


#file.write("O resultado do teste de normalização Shapiro-Wilk para Rottentomatoes MARVEL é:\n")
auxSTR = str(shapiro(lista1))
auxSTR = auxSTR[1:]

aux = "(Shapiro-Wilk, MARVEL, Rottentomatoes, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)
#file.write("Logo, os dados são normais\n")

#file.write("O resultado do teste de normalização Shapiro-Wilk para Rottentomatoes DC é:\n")
auxSTR = str(shapiro(lista2))
auxSTR = auxSTR[1:]


aux = "(Shapiro-Wilk, DC, Rottentomatoes, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)
#file.write("Logo, os dados são normais\n")

lista1 = []
lista2 = []
#file.write("\n")

#Metacritic MARVEL vs metacritic DC
cur.execute("SELECT metacritic_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT metacritic_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)


#file.write("O resultado do teste de normalização Shapiro-Wilk para IMDB MARVEL é:\n")
auxSTR = str(shapiro(lista1))
auxSTR = auxSTR[1:]

aux = "(Shapiro-Wilk, MARVEL, Metacritic, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)
#file.write("Logo, os dados são normais\n")

#file.write("O resultado do teste de normalização Shapiro-Wilk para IMDB MARVEL é:\n")
auxSTR = str(shapiro(lista2))
auxSTR = auxSTR[1:]

aux = "(Shapiro-Wilk, DC, Metacritic, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)
#file.write("Logo, os dados são normais\n")

lista1 = []
lista2 = []

#file.write("\n")

#World wide income MARVEL vs World wide incom DC
cur.execute("SELECT ww_income FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT ww_income FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)


#file.write("O resultado do teste de normalização Shapiro-Wilk para Renda Mundial MARVEL é:\n")
auxSTR = str(shapiro(lista1))
auxSTR = auxSTR[1:]

aux = "(Shapiro-Wilk, MARVEL, Renda Mundial, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)
#file.write("Logo, os dados são normais\n")

#file.write("O resultado do teste de normalização Shapiro-Wilk para Renda Mundial DC é:\n")
auxSTR = str(shapiro(lista2))
auxSTR = auxSTR[1:]

aux = "(Shapiro-Wilk, DC, Renda Mundial, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)
#file.write("Logo, os dados são normais\n")

lista1 = []
lista2 = []

#file.write("\n")

#Marvel
#IMDB rating vs Metacritic rating
#Getting de data from the first list
#file.write("MARVEL \n")

cur.execute("SELECT imdb_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT metacritic_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)


#file.write("Resultados do teste t-student em relação IMDB vs Metacritic na Marvel\n")
auxSTR = str(stats.ttest_ind(lista1,lista2))
auxSTR =  auxSTR.replace("statistic=", "")
auxSTR =  auxSTR.replace("pvalue=", "")
auxSTR =  auxSTR.replace("Ttest_indResult", "")
auxSTR = auxSTR[1:]

aux = "(t-student, MARVEL, IMDB vs Metacritic, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)


#file.write("\n")
lista1 = []
lista2 = []

#IMDB rating vs RottenTomatoes rating
#Getting de data from the first list
cur.execute("SELECT imdb_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT rottentomatoes_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)

#Executing the t-student test
ks_test = ks_2samp(lista1, lista2)


#file.write("Resultados do teste t-student em relação IMDB vs Rottentomatoes na Marvel\n")
auxSTR = str(stats.ttest_ind(lista1,lista2))
auxSTR =  auxSTR.replace("statistic=", "")
auxSTR =  auxSTR.replace("pvalue=", "")
auxSTR =  auxSTR.replace("Ttest_indResult", "")
auxSTR = auxSTR[1:]

aux = "(t-student, MARVEL, IMDB vs Rottentomatoes, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)

#file.write("\n")
lista1 = []
lista2 = []

#Metacritic rating vs RottenTomatoes rating
#Getting de data from the first list
cur.execute("SELECT rottentomatoes_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT metacritic_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)

#Executing the t-student test
ks_test = ks_2samp(lista1, lista2)

#file.write("Resultados do teste t-student em relação Rottentomatoes vs Metacritic na Marvel\n")
auxSTR = str(stats.ttest_ind(lista1,lista2))
auxSTR =  auxSTR.replace("statistic=", "")
auxSTR =  auxSTR.replace("pvalue=", "")
auxSTR =  auxSTR.replace("Ttest_indResult", "")
auxSTR = auxSTR[1:]

aux = "(t-student, MARVEL, Metacritic vs Rottentomatoes, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)

#file.write("\n")
lista1 = []
lista2 = []

#------------------------------------------------------------------------------------------------------------------------------------

#DC
#IMDB rating vs Metacritic rating
#Getting de data from the first list
#file.write("DC \n")

cur.execute("SELECT imdb_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT metacritic_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)

#Executing the t-student test
ks_test = ks_2samp(lista1, lista2)

#file.write("Resultados do teste t-student em relação IMDB vs Metacritic na DC\n")
auxSTR = str(stats.ttest_ind(lista1,lista2))
auxSTR =  auxSTR.replace("statistic=", "")
auxSTR =  auxSTR.replace("pvalue=", "")
auxSTR =  auxSTR.replace("Ttest_indResult", "")
auxSTR = auxSTR[1:]

aux = "(t-student, DC, IMDB vs Metacritic, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)

#file.write("\n")
lista1 = []
lista2 = []

#IMDB rating vs RottenTomatoes rating
#Getting de data from the first list
cur.execute("SELECT imdb_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT rottentomatoes_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)

#Executing the t-student test
ks_test = ks_2samp(lista1, lista2)


#file.write("Resultados do teste t-student em relação IMDB vs Rottentomatoes na DC\n")
auxSTR = str(stats.ttest_ind(lista1,lista2))
auxSTR =  auxSTR.replace("statistic=", "")
auxSTR =  auxSTR.replace("pvalue=", "")
auxSTR =  auxSTR.replace("Ttest_indResult", "")
auxSTR = auxSTR[1:]

aux = "(t-student, DC, IMDB vs Rottentomatoes, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)


#file.write("\n")
lista1 = []
lista2 = []

#Metacritic rating vs RottenTomatoes rating
#Getting de data from the first list
cur.execute("SELECT rottentomatoes_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT metacritic_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)

#Executing the t-student test
ks_test = ks_2samp(lista1, lista2)


#file.write("Resultados do teste t-student em relação Rottentomatoes vs Metacritic na DC\n")
auxSTR = str(stats.ttest_ind(lista1,lista2))
auxSTR =  auxSTR.replace("statistic=", "")
auxSTR =  auxSTR.replace("pvalue=", "")
auxSTR =  auxSTR.replace("Ttest_indResult", "")
auxSTR = auxSTR[1:]

aux = "(t-student, DC, Metacritic vs Rottentomatoes, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)

#file.write("\n")
lista1 = []
lista2 = []

#-------------------------------------------------------------------------------------------------------------
#Pearson
#file.write("Correlação de Pearson \n")
#file.write("MARVEL \n")


#Marvel

#Pearson IMDB vs World Wilde Income
cur.execute("SELECT imdb_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT ww_income FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)


#Executing the Pearson test
pearson = pearsonr(lista1, lista2)

#file.write("O resultado da correlação de Pearson entre a avaliação IMDB e a renda mundial da MARVEL\n")
auxSTR = str(pearson)
auxSTR = auxSTR[1:]

aux = "(Pearson, MARVEL, IMDB, Renda Mundial, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)


#file.write("\n")
lista1 = []
lista2 = []

#Pearson Metacritic vs WW Income

#Pearson IMDB vs World Wilde Income
cur.execute("SELECT metacritic_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT ww_income FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)


#Executing the Pearson test
pearson = pearsonr(lista1, lista2)


#file.write("O resultado da correlação de Pearson entre a avaliação metacritic e a renda mundial da MARVEL\n")
auxSTR = str(pearson)
auxSTR = auxSTR[1:]

aux = "(Pearson, MARVEL, Metacritic, Renda Mundial, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)

#file.write("\n")
lista1 = []
lista2 = []

#Pearson Rottentomatoes vs WW Income

#Pearson IMDB vs World Wilde Income
cur.execute("SELECT rottentomatoes_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT ww_income FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)


#Executing the Pearson test
pearson = pearsonr(lista1, lista2)


#file.write("O resultado da correlação de Pearson entre a avaliação Rottentomatoes e a renda mundial da MARVEL\n")
auxSTR = str(pearson)
auxSTR = auxSTR[1:]

aux = "(Pearson, MARVEL, Rottentomatoes, Renda Mundial, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)

#file.write("\n")
lista1 = []
lista2 = []


#DC
#file.write("DC \n")

#Pearson IMDB vs World Wilde Income
cur.execute("SELECT imdb_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT ww_income FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)


#Executing the Pearson test
pearson = pearsonr(lista1, lista2)

#file.write("O resultado da correlação de Pearson entre a avaliação IMDB e a renda mundial da DC\n")
auxSTR = str(pearson)
auxSTR = auxSTR[1:]

aux = "(Pearson, DC, IMDB, Renda Mundial, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)


#file.write("\n")
lista1 = []
lista2 = []

#Pearson Metacritic vs WW Income

#Pearson IMDB vs World Wilde Income
cur.execute("SELECT metacritic_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT ww_income FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)


#Executing the Pearson test
pearson = pearsonr(lista1, lista2)


#file.write("O resultado da correlação de Pearson entre a avaliação metacritic e a renda mundial da DC\n")
auxSTR = str(pearson)
auxSTR = auxSTR[1:]

aux = "(Pearson, DC, Metacritic, Renda Mundial, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)

#file.write("\n")
lista1 = []
lista2 = []

#Pearson Rottentomatoes vs WW Income

#Pearson IMDB vs World Wilde Income
cur.execute("SELECT rottentomatoes_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT ww_income FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)


#Executing the Pearson test
pearson = pearsonr(lista1, lista2)

#file.write("O resultado da correlação de Pearson entre a avaliação Rottentomatoes e a renda mundial da DC\n")
auxSTR = str(pearson)
auxSTR = auxSTR[1:]

aux = "(Pearson, DC, Rottentomatoes, Renda Mundial, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)


#file.write("\n")
lista1 = []
lista2 = []




#-------------------------------------------------------------------------------------------------------------
#DC vs MARVEL

#file.write("Teste t-student IMDB:\n")
#Executing the t-student one tailed test
cur.execute("SELECT imdb_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT imdb_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)

#file.write("O resultado do teste t-student do IMDB MARVEL vs DC é:\n")
#file.write(str(stats.ttest_ind(lista1,lista2)) + "\n")

auxSTR = str(stats.ttest_ind(lista1,lista2))
auxSTR =  auxSTR.replace("statistic=", "")
auxSTR =  auxSTR.replace("pvalue=", "")
auxSTR =  auxSTR.replace("Ttest_indResult", "")
auxSTR = auxSTR[1:]

aux = "(t-student, MARVEL vs DC, IMDB, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)
lista1 = []
lista2 = []


#Executing the t-student one tailed test
#file.write("Teste t-student Metacritic:\n")
cur.execute("SELECT metacritic_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT metacritic_rating  FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)


#file.write("O resultado do teste t-student do Metacritic MARVEL vs DC é:\n")
auxSTR = str(stats.ttest_ind(lista1,lista2))
auxSTR =  auxSTR.replace("statistic=", "")
auxSTR =  auxSTR.replace("pvalue=", "")
auxSTR =  auxSTR.replace("Ttest_indResult", "")
auxSTR = auxSTR[1:]

aux = "(t-student, MARVEL vs DC, Metacritic, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)

#file.write("\n")

lista1 = []
lista2 = []


#Executing the t-student one tailed test
#file.write("Teste t-student Rottentomatoes:\n")
cur.execute("SELECT rottentomatoes_rating FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT rottentomatoes_rating FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)


#file.write("O resultado do teste t-student do Rottentomatoes MARVEL vs DC é:\n")
auxSTR = str(stats.ttest_ind(lista1,lista2))
auxSTR =  auxSTR.replace("statistic=", "")
auxSTR =  auxSTR.replace("pvalue=", "")
auxSTR =  auxSTR.replace("Ttest_indResult", "")
auxSTR = auxSTR[1:]

aux = "(t-student, MARVEL vs DC, Rottentomatoes, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)

#file.write("\n")
lista1 = []
lista2 = []


#Executing the t-student one tailed test
#file.write("Teste t-student da renda:\n")
cur.execute("SELECT ww_income FROM `filmes2` WHERE franquia = 'MARVEL'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista1.append(dadoINT)

#Getting de data from the second list
cur.execute("SELECT ww_income FROM `filmes2` WHERE franquia = 'DC'")
for row in cur:
	dadoSTR = str(row)
	dadoSTR = dadoSTR[1:]
	dadoSTR = dadoSTR.rstrip(')')
	dadoSTR = dadoSTR.rstrip(',')
	dadoINT = int(dadoSTR)
	lista2.append(dadoINT)


#file.write("O resultado do teste t-student para renda mundial MARVEL vs DC é:\n")
auxSTR = str(stats.ttest_ind(lista1,lista2))
auxSTR =  auxSTR.replace("statistic=", "")
auxSTR =  auxSTR.replace("pvalue=", "")
auxSTR =  auxSTR.replace("Ttest_indResult", "")
auxSTR = auxSTR[1:]

aux = "(t-student, MARVEL vs DC, Renda Mundial, " + auxSTR + "\n"
aux = aux[1:]
aux = aux.replace(')', '')
file.write(aux)



#file.write("\n")

lista1 = []
lista2 = []
file.close