def m_genetic_trait(a,b) :
  m_list = []
  if a == "R" or a == "r" :
    m_list.append(a)
  if b == "R" or b == "r" :
    m_list.append(b)
    m_list.sort()
  result1 =  m_list
  return result1

def f_genetic_trait(c,d) :
  f_list = []
  if c == "R" or c == "r" :
    f_list.append(c)
  if d == "R" or d == "r" :
    f_list.append(d)
    f_list.sort()
  result2 =  f_list
  return result2

def c_genetic_trait(e,f) :
  i_c_list = []
  if e == "R" or e == "r" :
    i_c_list.append(e)
  if f == "R" or f == "r" :
    i_c_list.append(f)
  result3 =  e + f
  return result3
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