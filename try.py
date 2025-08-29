from rapidfuzz import fuzz

s1 = "k VP impeach trial set for Aug. 6"
s2 = "VP impeach trial setfor _"

res = fuzz.partial_ratio_alignment(s1, s2)
print(fuzz.partial_token_sort_ratio(s1,s2))
print(fuzz.ratio(s1, s2))            # 83
print(res) # 100
new_res = s1[res.src_start:res.src_end]
print(new_res)
print(f"New String: {s1.replace(new_res, "")}")

# first_list = list(s1)
# second_list = list(s2)

# print([x for x in first_list if x not in second_list])
# def equal_str_chker(string1,string2):
#     pass