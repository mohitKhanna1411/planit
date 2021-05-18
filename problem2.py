string = "PlanitTestingProblem"
string = string.lower()
freq_dict = {}
max_key = None
for i in string:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1
if bool(freq_dict):
    max_key = max(freq_dict, key=freq_dict.get)
print(max_key)
