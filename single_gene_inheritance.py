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

def p_genetic_trait_a_i(phenotype_m, phenotype_f) :
    dominate = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #우성 리스트
    recessive = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #열성 리스트
    m_list = list(phenotype_m) # 모계 유전자 삽입
    f_list = list(phenotype_f) # 부계 유전자 삽입
    m_p_list = list()
    f_p_list = list()
    L = len(f_list)
    a_p_list = list()
    a_c_list = list()
    p_f_list = list()
    nny_list = list()
    for idx in range(0, len(m_list), 2): # 14 ~ 17행 리스트를 2개씩 분할
        m_p_list.append([m_list[idx], m_list[idx+1]])
        f_p_list.append([f_list[idx], f_list[idx+1]])
        L = len(m_p_list)
        for jdx in range(0,L): #18 ~ 22 m_p_list와 f_p_list를 조합하여 만들 수 있는 모든 경우의 수를 구함
            for mdx in m_p_list[jdx]:
                for fdx in f_p_list[jdx]:
                    a_p_list.append(mdx + fdx)
                    L2 = len(a_p_list) -1 # L2는 a_p_list의 길이 -1
        nny_list = list(range(0,L,1)) # 22 ~ 25 a_p_list의 반복되는 부분을 잘라서 문자 종류 중복없는 a_c_list 만들기
        print(nny_list)
        a = sum(nny_list) # a + q 이후엔 중복이 안나오기 시작해서 a앞에서 잘름
        a_c_list = a_p_list[a*4: L2 + 1]
        print(a_c_list)
    result = a_c_list
    return result

def c_genetic_trait_a_i(phenotype) :
    c_s_p_list = list()
    dominate = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    recessive = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    c_list = list(phenotype)
    c_p_list = list()
    for idx in range(0, len(c_list), 2):
        c_p_list.append(c_list[idx] + c_list[idx+1])

    result = c_p_list
    return result
