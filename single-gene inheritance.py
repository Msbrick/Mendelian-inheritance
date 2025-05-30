def mother_phenotype(*phenotype) :
  phenotype = [phenotype]
  dominate = ["A", "B", "C", "D", "E", "F","G","H","I","J","K","L","N","M","O","P","Q","R","T","U","V","W","X","Y","Z"]
  recessive = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  for i in range(0:L)
    for j in range(0:L1):
      i = 0
      j = i + 1
      a = phenotype[i: j]
      b = "phenotype{j}"
      c = c[0] + c[1]
      all_phenotype = [c]
   result = all_phenotype
   return result

def father_phenotype(*phenotype) :
  dominate = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "N", "M", "O", "P", "Q", "R", "T", "U", "V", "W", "X", "Y", "Z"]
  recessive = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  phenotype = [phenotype]
  L = len(phenotype)
  L1 = L - 1
  for i in range(0:L):
    for j in range(0:L1):
      i = 0
      j = i + 1
      a = phenotype[i: j]
      b = "phenotype{j}"
      c = c[0] + c[1]
      all_phenotype = [c]
      result = all_phenotype
      return result
dominate = ["A", "B", "C", "D", "E", "F","G","H","I","J","K","L","N","M","O","P","Q","R","T","U","V","W","X","Y","Z"]
recessive = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

all_phenotype = list(zip(["A", "B", "C", "D", "E", "F","G","H","I","J","K","L","N","M","O","P","Q","R","T","U","V","W","X","Y","Z"], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']))

    
      
    
v = input()
h = input()

if v != h and v == "R" or h == "r" :
    e = [v + h, h + v]
elif v == h and v == "R" or h == "r" :
    e = [h + v]
if v != h:
  percentage = (a_c_list.count(h + v) + a_c_list.count(v + h)) / len(a_c_list) * 100 #c_genetic_trait에서 입력받은 형질 / 나올 수 있는 전체형질
elif v == h:
  percentage = a_c_list.count(h + v) / len(a_c_list) * 100


  




      




      




