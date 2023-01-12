
s1 = "ACTGAGCABAAA"
s2 = "ACCACGGACAAA"


match = 2
mismatch = -1
gap_open = -5
gap_extend = -1

matrix = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

#%%
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i-1] == s2[j-1]:
            score = match
        else:
            score = mismatch
        matrix[i][j] = max(matrix[i-1][j-1] + score, matrix[i-1][j] + gap_open + gap_extend, matrix[i][j-1] + gap_open + gap_extend,0)

print(matrix)
#%%
a1 = ""
a2 = ""
i = len(s1)
j = len(s2)

while i > 0 and j > 0:
    if matrix[i][j] == matrix[i-1][j-1] + score:
        a1 = s1[i-1] + a1
        a2 = s2[j-1] + a2
        i -= 1
        j -= 1
    elif matrix[i][j] == matrix[i-1][j] + gap_open + gap_extend:
        a1 = s1[i-1] + a1
        a2 = "-" + a2
        i -= 1
    elif matrix[i][j] == matrix[i][j-1] + gap_open + gap_extend:
        a1 = "-" + a1
        a2 = s2[j-1] + a2
        j -= 1
    else:
        break


print(a1)
print(a2)

