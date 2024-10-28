first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(l) for  l in first_strings if len(l) >= 5]
print(first_result)

second_result = [(first_word, second_word)
                 for first_word in first_strings
                 for second_word in second_strings
                 if len(first_word) == len(second_word)]
print(second_result)

third_string = first_strings + second_strings
third_result = {x: len(x) for x in third_string if not len(x) % 2}
print(third_result)
