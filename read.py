data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 10000 == 0:
			print(len(data)) # find the length(count of items) of list
print('loading complete, total ', len(data), ' rows of record')

# print(data[0])
# print('----------------')
# print(data[1])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('On average the length of comment is ', sum_len/len(data))
