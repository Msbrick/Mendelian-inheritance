def m_genetic_trait(a,b) : # Function that takes the mother's traits as input 
  m_list = [] # List to contain traits
  if a == "R" or a == "r" : # if input R or r for the first element of the list
    m_list.append(a) # append the input a to the list
  if b == "R" or b == "r" : # Enter R or r for the second element of the list
    m_list.append(b) # append the input a to the list
    m_list.sort() # sort list
  result1 =  m_list #Save list to result1
  return result1 # return m_list

def f_genetic_trait(c,d) : # Function that takes the father's traits as input 
  f_list = [] # List to contain traits
  if c == "R" or c == "r" : # if input R or r for the first element of the list
    f_list.append(c) # append the input a to the list
  if d == "R" or d == "r" : # Enter R or r for the second element of the list
    f_list.append(d) # append the input a to the list
    f_list.sort() # sort list
  result2 =  f_list #Save list to result1
  return result2 # return m_list

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
