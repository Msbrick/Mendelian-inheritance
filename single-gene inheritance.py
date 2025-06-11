def p_genetic_trait_a_i(phenotype_m, phenotype_f) :
    dominate = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    recessive = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    m_list = list(phenotype_m)
    f_list = list(phenotype_f)
    print(m_list)
    p_list = m_list + f_list
    m_p_list = list()
    f_p_list = list()
    L = len(f_list)
    a_p_list = list()
    a_c_list = list()
    p_f_list = list()
    nny_list = list()
    L1 = len(m_list) *2
    for idx in range(0
                     , len(m_list), 2):
        m_p_list.append([m_list[idx], m_list[idx+1]])
        f_p_list.append([f_list[idx], f_list[idx+1]])
        L = len(m_p_list)
        for jdx in range(0,L):
            for mdx in m_p_list[jdx]:
                for fdx in f_p_list[jdx]:
                    a_p_list.append(mdx + fdx)
                    L2 = len(a_p_list) -1
        nny_list = list(range(0,L,1))
        a = sum(nny_list)
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

  




      




      




