
# Encontro perfeito
busaum = True
trenzin = True
Corsinha = True

# encontro deu bom
encontro_namorada_ = busaum or trenzin
# print(sera que deu certo)

# Condições de locomoção
locomocao = "Corsinha" 
choveu = True

# Estrutura de decisão (IF / ELIF / ELSE)
if choveu and locomocao == 'moto':
    resultado = "⛈️ Ficamos Tô todo molhado ela prefiria de carro 🚗:("
elif not choveu and locomocao == 'moto':
    resultado = " 🌬️ Vento na cara e motor ligado ela reclamando pois era maior temporal ⛈️⛈️!"
elif locomocao == 'Corsinha':
    resultado = "Tô de Corsinha, o ar-condicionado geladinho clima de montanha 🏔️🏔️ chegamos no shopping 🛍️ tranquilo 😊😊!"
elif locomocao == 'busaum' and choveu:
    resultado = "Janelas fechadas e maior calor ☀️ tava um cheiro desagradável no ônibus 😒, e ela reclamando poderiamos te ido de uber 🚗:("
elif locomocao == 'trenzin':
    resultado = "Vamos de trenzin 🚈🚈 chegaremos rapido no shopping, claro amor 😍"
else:
    resultado = "Tô molhado :) (Fomos a pé ou de outro jeito)"

print(resultado)



















