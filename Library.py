def single_factor_inheritance_m(a_s, *phenotype1) :
  m_list = [phenotype1]
  M = m_list
  a_m_list = []
  if a_s == "autosomal" :
      for i in phenotype1 :
        for j in phenotype1 :
          if ord(i) - ord(j) == 0 :
            k = i + j   
            a_m_list.append(k)
          elif ord(i) - ord(j) ==32 :
            k = i + j
            N = j + i
            a_m_list.append(k)
            a_m_list.append(N)
  result = a_m_list
  return result

def single_factor_inheritance_f(a_s, *phenotype2) :
  f_list = [phenotype2]
  F= f_list
  a_f_list = []
  if a_s == "autosomal" :
      for i in phenotype2 :
        for j in phenotype2 :
          if ord(i) - ord(j) == 0 :
            k = i + j   
            a_f_list.append(k)
          elif ord(i) - ord(j) ==32 :
            k = i + j
            N = j + i
            a_f_list.append(k)
            a_f_list.append(N)
  result = a_f_list
  return result

