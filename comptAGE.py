somme = 0
condition = False

while condition == False:
	nouv_prix = input('')
	if nouv_prix == 0:
		condition = True
	else:
		somme += nouv_prix

print somme
