vowels = 'aeiou'
# create your list here
input_string = list(input())
vowels_list = [x for x in input_string if x in set(vowels)]
print(vowels_list)
