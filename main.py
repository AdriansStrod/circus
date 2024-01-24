# Specifikācijan Adrians Strods
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git


#Adrians Strods
la1=1
la2=1
ka=1-6
p1 =1
p2 =1
choice=25
#spele divi cilveki, viņi izvelas kus bus pirmais un otrais
while True:
  print("player which doing move")
  print("1.player first ")
  print("2.player second")
  choice = input("Enter your choice (1-2): ")
  if la1=100
  print ("player first win!!!!!")
  elif la2=100
  print ("player second win!!!!!")
  
  #kad izvelejas 1 speletaju viņš met kauliņu un parvietojas no 1-6 lauciņiem
  if choice == '1':
   print("mest kauliņu")
   import random
   
   print(random.randint(1,6))
  random=ka
  ka+=la1
  #kods lai katram speletajam bija tikai 25 kauliņu mešanas ja bus vairak tad bus neizškirts
  if choice>='25' or choice=='25':
  print("beidzas raundi - neizšķirts")
  #kad izvelejas 2 speletaju viņš met kauliņu un parvietojas no 1-6 lauciņiem
  if choice == '1':
    print("mest kauliņu")
    import random
 
    print(random.randint(1,6))
    random=ka
    ka+=la2
    #kods kur speletaji ies uzpriekšu vai atpakaļ uz kapnem.
  if la1==18 or la2==18:
    print ("jus ejat atpakaļ uz 7 lauciņu")
  la1-=11 or la2-=11
  elif la1=67 or la2=67 
  print ("jus ejat atpakaļ uz 18 lauciņu")
  la1-=18 or la2-=18:
  pass
