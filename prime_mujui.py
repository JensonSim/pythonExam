def is_prime(x):
	if x<2 or x==0:
		print '1'
		return False
	elif x==2:
		return True
	else:
	    for n in range(2, x):
			if x%n==0:
				print x,"/",n, x,"is False"
				a = False
				return a
			else:
				print x, "/", n, x, "is True"

	return True





