def single_factor_inheritance_m(a_s, *phenotype1) :
  m_list = [phenotype1]
  M = m_list
  a_m_list = []
  A_m_list = []
  if a_s == "autosomal" :
    for i in phenotype1 :
      for j in phenotype1 :
        if ord(i) - ord(j) == 0 or ord(i) - ord(j) == 32 or ord(i) - ord(j) == -32 :
          k = i + j
          a_m_list.append(k)
          print(a_m_list)
          L = len(a_m_list)
    for i in range(0, L):
      i = 0
      i = i + 1
      if i % 4 == 0 :
        S = a_m_list[i:i+4]
        print(S)
        for x in S:
          for y in S:
            for z in S:
              A_m_list.append(x)
              A_m_list.append(y)
              A_m_list.append(z)
           
  result = A_m_list
  return result


print(single_factor_inheritance_m('autosomal', input(), input(),input(), input(), input(), input()))
