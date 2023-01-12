
#pip install plot_likert

# Inicilização

# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import plot_likert

Create dir to save graphs
script_dir = os.path.dirname(__file__)
graphs_dir = os.path.join(script_dir, 'graphs/')

if not os.path.exists(graphs_dir):
    os.makedirs(graphs_dir)

plt.rcParams.update({'font.size': 22, 'font.weight': 'bold'})
plt.rcParams["figure.autolayout"] = True
plt.rcParams['xtick.labelsize'] = 19
plt.rcParams['ytick.labelsize'] = 18

# Read file
data = pd.read_csv("permanencia.csv")

# Data Dataframe
df_data = pd.DataFrame(data)

# Likert Scale
likert_agreement = {
    1:"Discordo totalmente",
    2:"Discordo",
    3:"Nem discordo, nem concordo",
    4:"Concordo",
    5:"Concordo totalmente"
}

likert_frequency = [
    "Nunca",
    "Raramente",
    "Às vezes",
    "Sempre"
]

attendance = {
    1:"Eu não frequento aulas presenciais",
    2:"Menos de 25%",
    3:"Mais de 25% e menos de 50%",
    4:"Mais de 50% e menos de 75%",
    5:"Mais de 75% até 100%"
}

# Age Group Pie Graph----------------------------
have_options = []
for i in df_data['Faixa etária:']:
  if i not in have_options:
    have_options.append(i)


age_graph = df_data['Faixa etária:'].value_counts().to_dict()

y = np.array(list(age_graph.values()))
age_group_labels = np.array(list(age_graph.keys()))

plt.figure(figsize=(15,10))
plt.pie(y, labels = age_group_labels, autopct='%.1f%%')
plt.suptitle("Faixa Etária")
plt.savefig("graphs/grafico_pizza_faixa_etaria.jpg")


# Genre Pie Graph----------------------------
genres_qtt = df_data['Sexo:'].value_counts()

y = np.array([genres_qtt[0], genres_qtt[1], 0])
genre_labels = ["Masculino ({})".format(genres_qtt[0]), "Feminino ({})".format(genres_qtt[1]), "Prefiro não responder ({})".format(0)]

plt.figure(figsize=(15,10))
plt.pie(y, labels = genre_labels, autopct='%.1f%%')
plt.suptitle("Sexo")
plt.savefig("graphs/grafico_pizza_sexo.jpg")


# Income Graph ----------------------------
income_graph = df_data['Qual sua renda familiar?'].value_counts().to_dict()

income_label = []

for i in income_graph.keys() :
  income_label.append(i +' ({})'.format(income_graph[i]))

y = np.array(list(income_graph.values()))
income_group_labels = np.array(income_label)

#Pie Graph
plt.figure(figsize=(15,9))
plt.pie(y, labels = income_group_labels, autopct='%.1f%%')
plt.suptitle("Renda")
plt.savefig("graphs/grafico_pizza_renda.jpg")

#Bar Graph
plt.figure(figsize=(15,9))
plt.barh(income_label, list(income_graph.values()))
plt.suptitle("Renda")
plt.savefig("graphs/grafico_barra_renda.jpg")


# School Type Graph ----------------------------
school_graph = df_data['Qual tipo de escola frequentou no ensino médio?'].value_counts().to_dict()

y = np.array(list(school_graph.values()))

school_label = []

for i in school_graph.keys() :
  school_label.append(i +' ({})'.format(school_graph[i]))

school_group_labels = np.array(school_label)

#Pie Graph
plt.figure(figsize=(15,10))
plt.pie(y, labels = school_group_labels, autopct='%.1f%%')
plt.suptitle("Tipo de Escola")
plt.savefig("graphs/grafico_pizza_escola.jpg")

#Bar Graph
plt.figure(figsize=(15,10))
plt.barh(school_label, list(school_graph.values()))
plt.suptitle("Tipo de Escola")
plt.savefig("graphs/grafico_barra_escola.jpg")


# Scholarity Graph ----------------------------
schoolarity_graph = df_data['Qual a escolaridade dos seus pais ou responsáveis?'].value_counts().to_dict()

y = np.array(list(schoolarity_graph.values()))

schoolarity_label = []

for i in schoolarity_graph.keys() :
  schoolarity_label.append(i +' ({})'.format(schoolarity_graph[i]))

scholarity_group_labels = np.array(schoolarity_label)

#Pie Graph
plt.figure(figsize=(15,10))
plt.pie(y, labels = scholarity_group_labels, autopct='%.1f%%')
plt.suptitle("Escolaridade dos Pais")
plt.savefig("graphs/grafico_pizza_escolaridade_pais.jpg")

#Bar Graph
plt.figure(figsize=(15,10))
plt.barh(schoolarity_label, list(schoolarity_graph.values()))
plt.suptitle("Escolaridade dos Pais")
plt.savefig("graphs/grafico_barra_escolaridade_pais.jpg")


# Dependency Graph ----------------------------
dependency_graph = df_data['Você depende financeiramente de alguém?'].value_counts().to_dict()

y = np.array(list(dependency_graph.values()))

dependency_label = []

for i in dependency_graph.keys() :
  dependency_label.append(i +' ({})'.format(dependency_graph[i]))

dependency_group_labels = np.array(dependency_label)

#Pie Graph
plt.figure(figsize=(10,10))
plt.pie(y, labels = dependency_group_labels, autopct='%.1f%%')
plt.title("Dependência Financeira")
plt.savefig("graphs/grafico_pizza_depenciafinanceira.jpg")


# Marital Status Graph ----------------------------
marital_graph = df_data['Qual seu estado civil?'].value_counts().to_dict()

y = np.array(list(marital_graph.values()))

marital_label = []

for i in marital_graph.keys() :
  marital_label.append(i +' ({})'.format(marital_graph[i]))

marital_group_labels = np.array(marital_label)

#Pie Graph
plt.figure(figsize=(10,10))
plt.pie(y, labels = marital_group_labels, autopct='%.1f%%')
plt.title("Estado Civil")
plt.savefig("graphs/grafico_pizza_estadocivil.jpg")


# Sons Graph ----------------------------
sons_graph = df_data['Quantos filhos você tem?'].value_counts().to_dict()

y = np.array(list(sons_graph.values()))

sons_label = []

for i in sons_graph.keys() :
  sons_label.append(i +' ({})'.format(sons_graph[i]))

sons_group_labels = np.array(sons_label)

#Pie Graph
plt.figure(figsize=(10,10))
plt.pie(y, labels = sons_group_labels, autopct = '%.1f%%')
plt.title("Número de Filhos")
plt.savefig("graphs/grafico_pizza_filhos.jpg")


# Family Work Graph ----------------------------
familywork_graph = df_data['Algum familiar trabalha na área de TI?'].value_counts().to_dict()

y = np.array(list(familywork_graph.values()))

familywork_label = []

for i in familywork_graph.keys() :
  familywork_label.append(i +' ({})'.format(familywork_graph[i]))

familywork_group_labels = np.array(familywork_label)

#Pie Graph
plt.figure(figsize=(10,10))
plt.pie(y, labels = familywork_group_labels, autopct='%.1f%%')
plt.title("Algum familiar trabalha na área de TI?")
plt.savefig("graphs/grafico_pizza_trabalhofamilia.jpg")


# Breed Graph ----------------------------
breed_graph = df_data['Qual sua cor/raça?'].value_counts().to_dict()

y = np.array(list(breed_graph.values()))

breed_label = []

for i in breed_graph.keys() :
  breed_label.append(i +' ({})'.format(breed_graph[i]))

breed_group_labels = np.array(breed_label)

#Pie Graph
plt.figure(figsize=(10,10))
plt.pie(y, labels = breed_group_labels, autopct='%.1f%%')
plt.title("Qual Sua Cor/Raça?")
plt.savefig("graphs/grafico_pizza_cor.jpg")


# Working in TI Graph ----------------------------
workingTI_graph = df_data['Atualmente você está trabalhando na área de TI?'].value_counts().to_dict()

y = np.array(list(workingTI_graph.values()))

workingTI_label = []

for i in workingTI_graph.keys() :
  workingTI_label.append(i +' ({})'.format(workingTI_graph[i]))

workingTI_group_labels = np.array(workingTI_label)

#Pie Graph
plt.figure(figsize=(10,10))
plt.pie(y, labels = workingTI_group_labels, autopct='%.1f%%')
plt.title("Trabalha na Área de TI?")
plt.savefig("graphs/grafico_pizza_trabalhaTI.jpg")


# Period Graph ----------------------------
period_graph = df_data['Qual período letivo (ano/semestre) está cursando?'].value_counts().to_dict()

y = np.array(list(period_graph.values()))

period_label = []

for i in period_graph.keys() :
  period_label.append(i +' ({})'.format(period_graph[i]))

period_group_labels = np.array(period_label)

#Bar Graph
plt.figure(figsize=(15,8))
plt.barh(period_label, list(period_graph.values()))
plt.suptitle("Período Letivo")
plt.savefig("graphs/grafico_barra_periodoletivo.jpg")


# University Graph ----------------------------
university_graph = df_data['Qual sua universidade?'].value_counts().to_dict()

y = np.array(list(university_graph.values()))

university_label = []

for i in university_graph.keys() :
  university_label.append(i +' ({})'.format(university_graph[i]))

university_group_labels = np.array(university_label)

#Pie Graph
plt.figure(figsize=(10,10))
plt.pie(y, labels = university_group_labels, autopct='%.1f%%')
plt.title("Qual sua universidade?")
plt.savefig("graphs/grafico_pizza_universidade.jpg")


# Frequency Graph ----------------------------
frequency_graph = df_data['Qual sua frequência às aulas (porcentagem média de participação)?'].value_counts().to_dict()

for i in attendance.values():
  if i not in frequency_graph:
    frequency_graph[i] = 0

y = np.array(list(frequency_graph.values()))

frequency_label = []

for i in frequency_graph.keys() :
  frequency_label.append(i +' ({})'.format(frequency_graph[i]))

frequency_group_labels = np.array(frequency_label)

#Bar Graph
plt.figure(figsize=(15,8))
plt.barh(frequency_label, list(frequency_graph.values()))
plt.suptitle("Frequência às aulas")
plt.savefig("graphs/grafico_barra_frequencia.jpg")


# Laboratory Discipline Disapproved Graph ----------------------------
disapproved_graph = df_data['Quantas disciplinas práticas de laboratório você foi reprovado?'].value_counts().to_dict()

y = np.array(list(disapproved_graph.values()))
y = sorted(y)

disapproved_label = []

for i in disapproved_graph.keys() :
  disapproved_label.append(i)

disapproved_group_labels = np.array(disapproved_label)

#Bar Graph
plt.figure(figsize=(15,6))
plt.bar(disapproved_label, list(disapproved_graph.values()))
plt.xticks(fontsize=16)

plt.xlabel("Reprovações")
plt.suptitle("Reprovações em Disciplinas de Laboratório")
plt.savefig("graphs/grafico_barra_reprovadolaboratorio.jpg")


# Theoretical Discipline Disapproved Graph ---------------------------
disapproved_graph = df_data['Quantas disciplinas teóricas você foi reprovado?'].value_counts().to_dict()

y = np.array(list(disapproved_graph.values()))

disapproved_label = []

for i in disapproved_graph.keys() :
  disapproved_label.append(i)

disapproved_group_labels = np.array(disapproved_label)

#Bar Graph
plt.figure(figsize=(15, 6))
plt.bar(disapproved_label, list(disapproved_graph.values()))
plt.xticks(fontsize=16, weight='bold')
plt.tick_params(labelsize=12)

plt.xlabel("Reprovações")
plt.suptitle("Reprovações em Disciplinas Teóricas")
plt.savefig("graphs/grafico_barra_reprovadoteoricas.jpg")


# Disciplines in Semester Graph ---------------------------
disciplines_graph = df_data['Em média quantas disciplinas você se matricula por período letivo (ano/semestre)?'].value_counts().to_dict()

y = np.array(list(disciplines_graph.values()))

disciplines_label = []

for i in disciplines_graph.keys() :
  disciplines_label.append(str(i))

disciplines_group_labels = np.array(disciplines_label)

#Bar Graph
plt.figure(figsize=(10, 6))
plt.bar(disciplines_label, list(disciplines_graph.values()))
plt.xlabel("Quantidade de disciplinas")
plt.suptitle("Disciplinas por Período Letivo")
plt.savefig("graphs/grafico_barra_disciplinasporsemestre.jpg")


# Average Use Graph ----------------------------
average_graph = df_data['Qual sua média geral de aproveitamento do curso?'].value_counts().to_dict()

y = np.array(list(average_graph.values()))

average_label = []

for i in average_graph.keys() :
  average_label.append(i +' ({})'.format(average_graph[i]))

average_group_labels = np.array(average_label)

#Bar Graph
plt.figure(figsize=(10,7))
plt.barh(average_label, list(average_graph.values()))
plt.suptitle("Média Geral de Aproveitamento")
plt.savefig("graphs/grafico_barra_aproveitamento.jpg")


# Library Frequency Graph ----------------------------
library_graph = df_data['Você utiliza a biblioteca para apoiar seus estudos?'].value_counts().to_dict()

for i in likert_frequency:
  if i not in library_graph:
    library_graph[i] = 0

y = np.array(list(library_graph.values()))

library_label = []

for i in library_graph.keys() :
  library_label.append(i +' ({})'.format(library_graph[i]))

library_group_labels = np.array(library_label)

#Bar Graph
plt.figure(figsize=(15,8))
plt.barh(library_label, list(library_graph.values()))
plt.suptitle("Utiliza a biblioteca para apoiar os estudos?")
plt.savefig("graphs/grafico_barra_biblioteca.jpg")

#Likert Graph
axes = plot_likert.plot_likert(df_data['Você utiliza a biblioteca para apoiar seus estudos?'], likert_frequency, plot_percentage=True)
axes.get_figure().savefig('graphs/likert_biblioteca.jpg', dpi=100, bbox_inches='tight')



# Practical Lab Graph ----------------------------
practical_graph = df_data['Você realiza os trabalhos laboratoriais/práticos individuais?'].value_counts().to_dict()

for i in likert_frequency:
  if i not in practical_graph:
    practical_graph[i] = 0

y = np.array(list(practical_graph.values()))

practical_label = []

for i in practical_graph.keys() :
  practical_label.append(i +' ({})'.format(practical_graph[i]))

practical_group_labels = np.array(practical_label)

#Bar Graph
plt.figure(figsize=(15,8))
plt.barh(practical_label, list(practical_graph.values()))
plt.suptitle("Realiza os trabalhos laboratoriais/práticos individuais?")
plt.savefig("graphs/grafico_barra_laboratorioIndividual.jpg")

#Likert Graph
axes = plot_likert.plot_likert(df_data['Você realiza os trabalhos laboratoriais/práticos individuais?'], likert_frequency, plot_percentage=True)
axes.get_figure().savefig('graphs/likert_laboratorioIndividual.jpg', dpi=100, bbox_inches='tight')



# Participation Graph ----------------------------
practical_graph = df_data['Você participa ativamente nas discussões da aula?'].value_counts().to_dict()

for i in likert_frequency:
  if i not in practical_graph:
    practical_graph[i] = 0

y = np.array(list(practical_graph.values()))

practical_label = []

for i in practical_graph.keys() :
  practical_label.append(i +' ({})'.format(practical_graph[i]))

practical_group_labels = np.array(practical_label)

#Bar Graph
plt.figure(figsize=(15,8))
plt.barh(practical_label, list(practical_graph.values()))
plt.suptitle("Participa ativamente nas discussões da aula?")
plt.savefig("graphs/grafico_barra_discussoes.jpg")

#Likert Graph
axes = plot_likert.plot_likert(df_data['Você participa ativamente nas discussões da aula?'], likert_frequency, plot_percentage=True)
axes.get_figure().savefig('graphs/likert_discussoes.jpg', dpi=100, bbox_inches='tight')



# Group Work Graph ----------------------------
groupwork_graph = df_data['Você participa ativamente dos trabalhos em grupo?'].value_counts().to_dict()

for i in likert_frequency:
  if i not in groupwork_graph:
    groupwork_graph[i] = 0

y = np.array(list(groupwork_graph.values()))

groupwork_label = []

for i in groupwork_graph.keys() :
  groupwork_label.append(i +' ({})'.format(groupwork_graph[i]))

groupwork_group_labels = np.array(groupwork_label)

#Bar Graph
plt.figure(figsize=(15,8))
plt.barh(groupwork_label, list(groupwork_graph.values()))
plt.suptitle("Participa ativamente dos trabalhos em grupo?")
plt.savefig("graphs/grafico_barra_trabalhoGrupo.jpg")

#Likert Graph
axes = plot_likert.plot_likert(df_data['Você participa ativamente dos trabalhos em grupo?'], likert_frequency, label_max_width=20, plot_percentage=True)
axes.get_figure().savefig('graphs/likert_trabalhoGrupo.jpg', dpi=100, bbox_inches='tight')



# study time Graph ----------------------------
studytime_graph = df_data['Qual é o tempo gasto para estudo extra durante a semana?'].value_counts().to_dict()

y = np.array(list(studytime_graph.values()))

studytime_label = []

for i in studytime_graph.keys() :
  studytime_label.append(i +' ({})'.format(studytime_graph[i]))

studytime_group_labels = np.array(studytime_label)

#Bar Graph
plt.figure(figsize=(15,8))
plt.barh(studytime_label, list(studytime_graph.values()))
plt.suptitle("Tempo gasto para estudo extra durante a semana")
plt.savefig("graphs/grafico_barra_tempoEstudoExtra.jpg")


# Test Time Graph ----------------------------
testtime_graph = df_data['Qual é o tempo gasto de preparação para provas e exames?'].value_counts().to_dict()

y = np.array(list(testtime_graph.values()))

testtime_label = []

for i in testtime_graph.keys() :
  testtime_label.append(i +' ({})'.format(testtime_graph[i]))

testtime_group_labels = np.array(testtime_label)

#Bar Graph
plt.figure(figsize=(15,8))
plt.barh(testtime_label, list(testtime_graph.values()))
plt.suptitle("Tempo gasto de preparação para provas e exames")
plt.savefig("graphs/grafico_barra_tempoPreparacaoProva.jpg")

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update({'font.size': 20, 'font.weight': 'bold'})

# Ingress Likert Graph ----------------------------
likert_data = pd.DataFrame(df_data[['Quais fatores o motivam a ingressar no curso de SI? [Tenho interesse em computadores.]', 'Quais fatores o motivam a ingressar no curso de SI? [Tenho interesse em computadores.]',	'Quais fatores o motivam a ingressar no curso de SI? [Tenho interesse em jogos de computador.]',	'Quais fatores o motivam a ingressar no curso de SI? [Eu vou ter boas perspectivas no mercado de trabalho (oportunidades de trabalho suficientes).]',	'Quais fatores o motivam a ingressar no curso de SI? [Eu acho que a área de TI é promissora e necessária em diferentes áreas.]',	'Quais fatores o motivam a ingressar no curso de SI? [Eu acho que a área de TI oferece a possibilidade de alcançar auto-realização (Por exemplo: a chance de fazer algo grande).]',	'Quais fatores o motivam a ingressar no curso de SI? [Eu quero continuar meus estudos anteriores em TI (cursos).]',	'Quais fatores o motivam a ingressar no curso de SI? [Um professor me ensinou TI em um curso/projeto na escola.]',	'Quais fatores o motivam a ingressar no curso de SI? [Eu participei de grupos ou competições sobre TI (bootcamp, maratonas de programação).]',	'Quais fatores o motivam a ingressar no curso de SI? [Eu tenho interesse em ciências exatas]']])

#Rename Columns
column_headers = list(likert_data.columns.values)

i = 0
for header in column_headers:
  i += 1
  likert_data.rename(columns = {header:'Q{0}'.format(i)}, inplace = True)

# for header in column_headers:
#   e = header[header.find("[")+1:header.find("]")]
#   likert_data.rename(columns = {header:e}, inplace = True)

#Likert Graph
axes = plot_likert.plot_likert(likert_data, likert_agreement.values(), plot_percentage=True, figsize=(9,14), label_max_width=40, title = "Quais fatores o motivam a ingressar no curso de SI?")
axes.set_title(("Quais fatores o motivam a permanecer no curso de SI?"), fontsize=22, weight='bold')
axes.xaxis.set_label_text("Porcentagem das respostas")
axes.get_figure().savefig('graphs/likert_motivosIngressar.jpg', dpi=100, bbox_inches='tight')



# Permanency Likert Graph ----------------------------
likert_data2 = pd.DataFrame(df_data[['Quais fatores o motivam a permanecer no curso de SI?  [O docente explica o conteúdo do curso de maneira clara.]',	'Quais fatores o motivam a permanecer no curso de SI?  [A qualificação do corpo docente.]',	'Quais fatores o motivam a permanecer no curso de SI?  [Uma grade curricular atualizada.]',	'Quais fatores o motivam a permanecer no curso de SI?  [Minha atmosfera de aprendizagem (atitudes de outros estudantes e professores).]',	'Quais fatores o motivam a permanecer no curso de SI?  [Saber a importância dos conteúdos estudados na graduação para atuação profissional.]',	'Quais fatores o motivam a permanecer no curso de SI?  [A promoção de eventos esportivos, sociais e de jogos eletrônicos é um incentivo para sua permanência no curso.]',	'Quais fatores o motivam a permanecer no curso de SI?  [A importância de entender as regras de matrícula e do regimento de reingresso.]',	'Quais fatores o motivam a permanecer no curso de SI?  [Bolsas de mérito (monitoria, IC e extensão) são importantes]',	'Quais fatores o motivam a permanecer no curso de SI?  [Recursos de assistência (bolsa permanência, alimentação e moradia) aos discentes são importantes]',	'Quais fatores o motivam a permanecer no curso de SI?  [O restaurante universitário é importante para sua permanência.]',	'Quais fatores o motivam a permanecer no curso de SI?  [A disponibilidade de laboratórios para uso fora do período das aulas?]',	'Quais fatores o motivam a permanecer no curso de SI?  [Espaços de convivência e de estudos são importantes]',	'Quais fatores o motivam a permanecer no curso de SI?  [Transporte público adequado ao horário, valor e calendário acadêmico.]',	'Quais fatores o motivam a permanecer no curso de SI?  [A segurança no campus da universidade.]',	'Quais fatores o motivam a permanecer no curso de SI?  [A localização geográfica do campus.]']])

#Rename Columns
column_headers = list(likert_data2.columns.values)

i = 0
for header in column_headers:
  i += 1
  likert_data2.rename(columns = {header:'Q{0}'.format(i)}, inplace = True)

# for header in column_headers:
#   e = header[header.find("[")+1:header.find("]")]
#   likert_data2.rename(columns = {header:e}, inplace = True)

#Likert Graph
axes = plot_likert.plot_likert(likert_data2, likert_agreement.values(),  plot_percentage=True, figsize=(8,13), label_max_width=40)
axes.set_title(("Quais fatores o motivam a permanecer no curso de SI?"), fontsize=22, weight='bold')
axes.xaxis.set_label_text("Porcentagem das respostas")
axes.get_figure().savefig('graphs/likert_motivosPermanecer.jpg', dpi=100, bbox_inches='tight')

# <--------------------  RENAME AND SORT ------------------------>


# Laboratory Discipline Disapproved Graph ----------------------------
disapproved_graph = df_data['Quantas disciplinas práticas de laboratório você foi reprovado?'].value_counts().to_dict()

#Rename to 0
disapproved_graph['0'] = disapproved_graph.pop('Nunca reprovei')

#Values
y = np.array(list(disapproved_graph.values()))

#Sort
disapproved_graph = dict(sorted(disapproved_graph.items()))

#Bar Graph
plt.figure(figsize=(15,6))
plt.bar(disapproved_graph.keys(), disapproved_graph.values())
plt.xticks(fontsize=16)

plt.xlabel("Reprovações")
plt.suptitle("Reprovações em Disciplinas de Laboratório")
plt.savefig("graphs/grafico_barra_reprovadolaboratorio.pdf")



# Theoretical Discipline Disapproved Graph ---------------------------
disapproved_theoretical_graph = df_data['Quantas disciplinas teóricas você foi reprovado?'].value_counts().to_dict()

#Rename to 0
disapproved_theoretical_graph['0'] = disapproved_theoretical_graph.pop('Nunca reprovei')

#Values
y = np.array(list(disapproved_theoretical_graph.values()))

#Sort
disapproved_theoretical_graph = dict(sorted(disapproved_theoretical_graph.items()))

#Reorder to final
disapproved_theoretical_graph['10'] = disapproved_theoretical_graph.pop('10')
disapproved_theoretical_graph['Mais de 10'] = disapproved_theoretical_graph.pop('Mais de 10')

#Bar Graph
plt.figure(figsize=(15, 6))
plt.bar(disapproved_theoretical_graph.keys(), disapproved_theoretical_graph.values())
plt.xticks(fontsize=16, weight='bold')
plt.tick_params(labelsize=12)

plt.xlabel("Reprovações")
plt.suptitle("Reprovações em Disciplinas Teóricas")
plt.savefig("graphs/grafico_barra_reprovadoteoricas.pdf")



# Gráficos Finais -> Que irão para o texto

# FIGURA 1 - study time Graph ----------------------------
studytime_graph = df_data['Qual é o tempo gasto para estudo extra durante a semana?'].value_counts().to_dict()

y = np.array(list(studytime_graph.values()))

studytime_label = []

for i in studytime_graph.keys() :
  studytime_label.append(i +' ({})'.format(studytime_graph[i]))

studytime_group_labels = np.array(studytime_label)

#Bar Graph
plt.figure(figsize=(15,8))
plt.barh(studytime_label, list(studytime_graph.values()))
#plt.suptitle("Tempo gasto para estudo extra durante a semana")
plt.rcParams["figure.autolayout"] = True
plt.savefig("graphs/grafico_barra_tempoEstudoExtra.pdf")


# FIGURA 2 - Test Time Graph ----------------------------
testtime_graph = df_data['Qual é o tempo gasto de preparação para provas e exames?'].value_counts().to_dict()

y = np.array(list(testtime_graph.values()))

testtime_label = []

for i in testtime_graph.keys() :
  testtime_label.append(i +' ({})'.format(testtime_graph[i]))

testtime_group_labels = np.array(testtime_label)

#Bar Graph
plt.figure(figsize=(15,8))
plt.barh(testtime_label, list(testtime_graph.values()))
plt.xticks(fontsize=16, weight='bold')
#plt.suptitle("Tempo gasto de preparação para provas e exames")
plt.savefig("graphs/grafico_barra_tempoPreparacaoProva.pdf")


# <--------------------  RENAME AND SORT ------------------------>


# FIGURA 3 - Theoretical Discipline Disapproved Graph ---------------------------
disapproved_theoretical_graph = df_data['Quantas disciplinas teóricas você foi reprovado?'].value_counts().to_dict()

#Rename to 0
disapproved_theoretical_graph['0'] = disapproved_theoretical_graph.pop('Nunca reprovei')

#Values
y = np.array(list(disapproved_theoretical_graph.values()))

#Sort
disapproved_theoretical_graph = dict(sorted(disapproved_theoretical_graph.items()))

#Reorder to final
disapproved_theoretical_graph['10'] = disapproved_theoretical_graph.pop('10')
disapproved_theoretical_graph['Mais de 10'] = disapproved_theoretical_graph.pop('Mais de 10')

#Bar Graph
plt.figure(figsize=(15, 6))
plt.bar(disapproved_theoretical_graph.keys(), disapproved_theoretical_graph.values())
plt.xticks(fontsize=16, weight='bold')

#plt.xlabel("Reprovações")
#plt.suptitle("Reprovações em Disciplinas Teóricas")
plt.savefig("graphs/grafico_barra_reprovadoteoricas.pdf")



# FIGURA 4 - Laboratory Discipline Disapproved Graph ----------------------------
disapproved_graph = df_data['Quantas disciplinas práticas de laboratório você foi reprovado?'].value_counts().to_dict()

#Rename to 0
disapproved_graph['0'] = disapproved_graph.pop('Nunca reprovei')

#Values
y = np.array(list(disapproved_graph.values()))

#Sort
disapproved_graph = dict(sorted(disapproved_graph.items()))

#Bar Graph
plt.figure(figsize=(15,6))
plt.bar(disapproved_graph.keys(), disapproved_graph.values())
plt.xticks(fontsize=16)

#plt.xlabel("Reprovações")
#plt.suptitle("Reprovações em Disciplinas de Laboratório")
plt.savefig("graphs/grafico_barra_reprovadolaboratorio.pdf")


#<--------------------Likert Graphs------------------>

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update({'font.size': 20, 'font.weight': 'bold'})

# FIGURA 5 - Ingress Likert Graph ----------------------------
likert_data = pd.DataFrame(df_data[['Quais fatores o motivam a ingressar no curso de SI? [Tenho interesse em computadores.]',	'Quais fatores o motivam a ingressar no curso de SI? [Tenho interesse em jogos de computador.]',	'Quais fatores o motivam a ingressar no curso de SI? [Eu vou ter boas perspectivas no mercado de trabalho (oportunidades de trabalho suficientes).]',	'Quais fatores o motivam a ingressar no curso de SI? [Eu acho que a área de TI é promissora e necessária em diferentes áreas.]',	'Quais fatores o motivam a ingressar no curso de SI? [Eu acho que a área de TI oferece a possibilidade de alcançar auto-realização (Por exemplo: a chance de fazer algo grande).]',	'Quais fatores o motivam a ingressar no curso de SI? [Eu quero continuar meus estudos anteriores em TI (cursos).]',	'Quais fatores o motivam a ingressar no curso de SI? [Um professor me ensinou TI em um curso/projeto na escola.]',	'Quais fatores o motivam a ingressar no curso de SI? [Eu participei de grupos ou competições sobre TI (bootcamp, maratonas de programação).]',	'Quais fatores o motivam a ingressar no curso de SI? [Eu tenho interesse em ciências exatas]']])

#Rename Columns
column_headers = list(likert_data.columns.values)
print(column_headers)

i = 0
for header in column_headers:
  i += 1
  likert_data.rename(columns = {header:'Q{0}'.format(i)}, inplace = True)


#Likert Graph
axes = plot_likert.plot_likert(likert_data, likert_agreement.values(), plot_percentage=True, figsize=(9,14), label_max_width=40)
#axes.set_title(("Quais fatores o motivam a permanecer no curso de SI?"), fontsize=22, weight='bold')
axes.xaxis.set_label_text("Porcentagem das respostas")
axes.get_figure().savefig('graphs/likert_motivosIngressar.pdf', dpi=100, bbox_inches='tight')



# FIGURA 6 - Permanency Likert Graph ----------------------------
likert_data2 = pd.DataFrame(df_data[['Quais fatores o motivam a permanecer no curso de SI?  [O docente explica o conteúdo do curso de maneira clara.]',	'Quais fatores o motivam a permanecer no curso de SI?  [A qualificação do corpo docente.]',	'Quais fatores o motivam a permanecer no curso de SI?  [Uma grade curricular atualizada.]',	'Quais fatores o motivam a permanecer no curso de SI?  [Minha atmosfera de aprendizagem (atitudes de outros estudantes e professores).]',	'Quais fatores o motivam a permanecer no curso de SI?  [Saber a importância dos conteúdos estudados na graduação para atuação profissional.]',	'Quais fatores o motivam a permanecer no curso de SI?  [A promoção de eventos esportivos, sociais e de jogos eletrônicos é um incentivo para sua permanência no curso.]',	'Quais fatores o motivam a permanecer no curso de SI?  [A importância de entender as regras de matrícula e do regimento de reingresso.]',	'Quais fatores o motivam a permanecer no curso de SI?  [Bolsas de mérito (monitoria, IC e extensão) são importantes]',	'Quais fatores o motivam a permanecer no curso de SI?  [Recursos de assistência (bolsa permanência, alimentação e moradia) aos discentes são importantes]',	'Quais fatores o motivam a permanecer no curso de SI?  [O restaurante universitário é importante para sua permanência.]',	'Quais fatores o motivam a permanecer no curso de SI?  [A disponibilidade de laboratórios para uso fora do período das aulas?]',	'Quais fatores o motivam a permanecer no curso de SI?  [Espaços de convivência e de estudos são importantes]',	'Quais fatores o motivam a permanecer no curso de SI?  [Transporte público adequado ao horário, valor e calendário acadêmico.]',	'Quais fatores o motivam a permanecer no curso de SI?  [A segurança no campus da universidade.]',	'Quais fatores o motivam a permanecer no curso de SI?  [A localização geográfica do campus.]']])

#Rename Columns
column_headers = list(likert_data2.columns.values)

i = 0
for header in column_headers:
  i += 1
  likert_data2.rename(columns = {header:'Q{0}'.format(i)}, inplace = True)


#Likert Graph
axes = plot_likert.plot_likert(likert_data2, likert_agreement.values(),  plot_percentage=True, figsize=(8,13), label_max_width=40)
#axes.set_title(("Quais fatores o motivam a permanecer no curso de SI?"), fontsize=22, weight='bold')
axes.xaxis.set_label_text("Porcentagem das respostas")
axes.get_figure().savefig('graphs/likert_motivosPermanecer.pdf', dpi=100, bbox_inches='tight')

