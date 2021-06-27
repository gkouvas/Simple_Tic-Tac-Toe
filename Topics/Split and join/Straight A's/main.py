# put your python code here
string = input()
new_string = string.split()
a_counter = 0
for i, i_string in enumerate(new_string):
    if i_string == "A":
        a_counter += 1
print(round(a_counter / len(new_string), 2))
