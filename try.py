from rapidfuzz import fuzz

s1 = "i-Float"
s2 = "Water aims to expand Project i-Float"

res = fuzz.partial_ratio_alignment(s1, s2)
print(fuzz.token_set_ratio(s1,s2))
print(fuzz.ratio(s1, s2))            # 83
print(res) # 100
new_res = s2[res.dest_start:res.dest_end]
print(new_res)
print(f"New String: {s2.replace(new_res, "")}")

# first_list = list(s1)
# second_list = list(s2)

# print([x for x in first_list if x not in second_list])
# def equal_str_chker(string1,string2):
#     pass

# mylist = [1,2,3]
# mylist[0] = 10

# print(mylist)