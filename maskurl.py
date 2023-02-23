nimport requests
import random
import os
os.system("rm $HOME/maskphish")
l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
os.system("clear")
url=input("Digite o Link para encurtar: ")
print("Você quer costumizar o seu link?\n1-Sim\n2-Não")
op=input(":")
if op=="1":
   nome=input("Digite o nome costumizado: ")
   r=requests.get(f'https://encurta.net/api?api=9ac0a3261fd4bd6cf495d56ec4034a914d5c05f7&url={url}&alias={nome}')
   p=r.json()
   print(p["shortenedUrl"])
elif op=="2":
   h=random.choice(l)+random.choice(l)+random.choice(l)+random.choice(l)+random.choice(l)+random.choice(l)
   r=requests.get(f'https://encurta.net/api?api=9ac0a3261fd4bd6cf495d56ec4034a914d5c05f7&url={url}&alias={h}')
   p=r.json()
   print(p["shortenedUrl"])
else:
   print("Opção inválida")
print("Programa finalizado\n\n\nTenha um bom dia.")
exit()

