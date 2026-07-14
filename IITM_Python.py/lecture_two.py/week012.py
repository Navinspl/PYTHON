word = input()
start = int(input())
end = int(input())

substring = word[start : end+1]
min_rep = len(word)
substring = substring * min_rep
print(substring)