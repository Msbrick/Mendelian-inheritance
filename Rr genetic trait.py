import single_gene_inheritance

m_list = m_genetic_trait(input(), input())
f_list = f_genetic_trait(input(), input())

a_c_list = []
a = a_c_list
for i in m_list:
  for j in f_list:
    b = i + j
    f = j +i
    a.append(f)
print(a)

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

print(percentage)
print("%")
