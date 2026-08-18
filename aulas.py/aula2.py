

#A ordem das condições

#busaum = True
#trenzin = True

#venho_pra_aula = busaum or trenzin
#print(venho_pra_aula)


locomocao = "Corsinha"
choveu = True

if choveu and locomocao == 'moto':
    resultado = "Tô todo molhado :("

elif not choveu and locomocao == 'moto':
    resultado = "Vento na cara e motor ligado!"
elif locomocao == 'Corsinha':
    resultado = "Tô de Corsinha, o ar-condicionado geladinho clima de montanha mas não me molho!"

elif locomocao == 'busaum' and choveu:
    resultado = "Janelas fechadas e tudo abafado no ônibus :("

elif locomocao == 'trenzin':
    resultado = "Partiu pegar o trem!"

else:
    resultado = "Tô seco :) (Fui a pé ou de outro jeito)"

print(resultado)











