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

with open('haberman.data', 'r') as f:
	for linha in f.readlines():
		atrib = linha.replace('\n', '').split(',')

		#atrib[0] - Age of patient
		#atrib[1] - Patient's year
		#atrib[2] - Number of positive axillary nodes detected
		#atrib[3] - Survival status (class attribute)
		amostras.append([int(atrib[0]),int(atrib[1]),int(atrib[2]),int(atrib[3])])

print(amostras)