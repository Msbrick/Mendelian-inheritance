def single-factor inheritance_2_a.m(a,b):
  m_list = []
  if ord(a) - ord(b) == 32 or ord(a) - ord(b) == -32 or ord(a) - ord(b) == 0 :
    c = a + b
    m_list.append(c)
  result = m_list
  return result

def single-factor inheritance_2_a.f(c,d):
  m_list = []
  if ord(a) - ord(b) == 32 or ord(a) - ord(b) == -32 or ord(a) - ord(b) == 0 :
    c = a + b
    m_list.append(c)
  result = m_list
  return result

def single_factor_inheritance_m(a_s, *phenotype) :
  m_list = [phenotype]
  M = m_list
  a_m_list = []
  if a_s == "autosomal" :
      for i in phenotype :
        for j in phenotype :
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

def single_factor_inheritance_f(a_s, *phenotype) :
  f_list = [phenotype]
  F= f_list
  a_f_list = []
  if a_s == "autosomal" :
      for i in phenotype :
        for j in phenotype :
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

