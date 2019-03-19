import math

#Dataset: https://archive.ics.uci.edu/ml/datasets/Haberman's+Survival
#Data Set Information:

#The dataset contains cases from a study that was conducted between 1958 and 1970 at the University of Chicago's Billings Hospital on the survival of patients who had undergone surgery for breast cancer.


#Attribute Information:

#1. Age of patient at time of operation (numerical) 
#2. Patient's year of operation (year - 1900, numerical) 
#3. Number of positive axillary nodes detected (numerical) 
#4. Survival status (class attribute) 
#-- 1 = the patient survived 5 years or longer 
#-- 2 = the patient died within 5 year

amostras = []

# Function print information of dataset
def info_dataset(amostras, verbose=True):
	if verbose:
		print('Total de Amostras: %d' % len(amostras))
	
	rotulo1, rotulo2 = 0, 0	
	for amostra in amostras:
		if amostra[-1] == 1:
			rotulo1 += 1
		else:
			rotulo2 += 1

	if verbose:
		print('Total Rotulos 1: %d' % rotulo1)
		print('Total Rotulos 2: %d' % rotulo2)

	return [len(amostras), rotulo1, rotulo2]

# Function to calculate the distance euclidiana
def dist_euclidiana(p, q):
	dim = len(p)
	soma = 0
   
	for i in range(dim-1):
		soma += math.pow(p[i] - q[i], 2)
	return math.sqrt(soma)

# Code Implementation KNN
def knn(treinamento, nova_amostra, K):
	dists = {}
	tam_treino = len(treinamento)

	# calcula a distância euclidiana da nova amostra para
	# todos od outros exemplos do conjunto de treinamento

	for i in range(tam_treino):
		d = dist_euclidiana(treinamento[i], nova_amostra)
		dists[i] = d

	# obtém as chaves (índices) dos k-vizinhos mais próximos
	k_vizinhos = sorted(dists, key=dists.get)[:K]

	# votação majoritária
	qtd_rotulo1, qtd_rotulo2 = 0, 0

	for indice in k_vizinhos:
		if treinamento[indice][-1] == 1:
			qtd_rotulo1 += 1
		else:
			qtd_rotulo2 += 1

	if qtd_rotulo1 > qtd_rotulo2:
		return 1
	else:
		return 2

with open('haberman.data', 'r') as f:
	for linha in f.readlines():
		atrib = linha.replace('\n', '').split(',')

		#atrib[0] - Age of patient
		#atrib[1] - Patient's year
		#atrib[2] - Number of positive axillary nodes detected
		#atrib[3] - Survival status (class attribute)
		amostras.append([int(atrib[0]),int(atrib[1]),int(atrib[2]),int(atrib[3])])

p = 0.6
_, rotulo1, rotulo2 = info_dataset(amostras, verbose=False)

treinamento, teste = [], []
max_rotulo1, max_rotulo2 = int(p* rotulo1), int(p*rotulo2)
total_rotulo1, total_rotulo2 = 0, 0

for amostra in amostras:
	if (total_rotulo1 + total_rotulo2) < (max_rotulo1 + max_rotulo2):
		treinamento.append(amostra)
		if amostra[-1] == 1 and total_rotulo1 < max_rotulo1:
			total_rotulo1 += 1
		else:
			total_rotulo2 += 1
	else:
		teste.append(amostra)


print(teste[10])
print(knn(treinamento, teste[10], K=13))