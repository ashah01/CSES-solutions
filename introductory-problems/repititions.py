seq = input()

greatest_length = 1

counter = 1
for i in range(1, len(seq)):
    if seq[i] == seq[i-1]:
        counter += 1
        if greatest_length < counter:
            greatest_length = counter
    else:
        if greatest_length < counter:
            greatest_length = counter
        counter = 1
    
print(greatest_length)