def is_prime(x):
	if x<2|x==0:
		return False
	elif x==2:
		return True
	else:
	    for n in range(2, x-1):
			if x%n==0:
				print x,"/",n, x,"is False"
				return False
			else:
				pass

		print x, "/", n, x, "is True"
		return True
	

print is_prime(7)
print is_prime(7)
print is_prime(14)
print is_prime(3)
print is_prime(9)
print is_prime(12)
print is_prime(21)
print is_prime(0)

