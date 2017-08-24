i = 1
fib = [1,2]
while True:
	if fib[i] <= 4000000:
		i += 1
		fib.append(fib[i - 1] + fib[i - 2])
	else:
		break
print sum([x for x in fib if x % 2 == 0])
