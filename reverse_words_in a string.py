def reverse_words_in_a_string(s):
	splited_list = s.split()
	reversed_list_iter = reversed(splited_list)
	return " ".join(reversed_list_iter)


print(reverse_words_in_a_string("My name is wanggang.")) # ['My', 'name', 'is', 'wanggang']



def reverse_string(s):
	a = s.split()
	print(a)  # ['my', 'name', 'is', 'wangang.']
	b = a[::-1] 
	print(b)  # ['wangang.', 'is', 'name', 'my']
	return ' '.join(b)

print(reverse_string("my name is wangang.")) # wangang. is name my