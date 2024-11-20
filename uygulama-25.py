# bir cümlede kaç tane a harfi olduğunu sayan kod.
# . yı görünce dur.
sayac=0
for x in "bir cümlede kaç tane a harfi olduğunu sayan kod. bir cümlede kaç tane a harfi olduğunu sayan kod.":
  if x=="r":
    sayac+=1
  if x==".":
    break
print (sayac, "defa")
