import pedigree analysis

p = p_genetic_trait_a_i(input(),input())
c = c_genetic_trait_a_i(input())
aus = 0
percentage_list = []
for idx in c:
    percentage = p.count(idx) / 4
    percentage_list.append(percentage)
    print(percentage_list)
    L = len(percentage_list)
ans = 1
for n in percentage_list:
	ans *= n
print(ans)
