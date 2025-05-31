word = input()
lst_word = list(word)
count = 0

while True:
	for i in range(len(lst_word)-1):
		if (lst_word[i] == "a"):
			if (lst_word[i+1] == "b"):
				lst_word[i] = "bb"
				lst_word[i+1] = "a"
				break
	
	result_word = ""
	for ix in lst_word:
		result_word += ix

	if "ab" not in result_word:
		break

	count += (1 % 1000000007)
	lst_word = list(result_word)

print(count + 1)