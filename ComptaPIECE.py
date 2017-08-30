pieces = [2, 1, 0.5, 0.2, 0.1]
amout_bypiece = []
montant = 0

for element in pieces:
	new_amount = input('Nombre de pieces de %.2f EURO: '%element) 
	temp_amount = new_amount*element
	amout_bypiece.append(temp_amount)
	montant += temp_amount

print str(montant) + ' EURO.\n'

i = 0
for element in amout_bypiece:
	print '%.2f en piece de %.2f EURO.'%(element, pieces[i])
	i += 1