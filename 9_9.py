grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(grades):
	avr_result = grades_average(grades)
	sq_diff = 0
	for n in grades:
		sq_diff += (avr_result - n)**2
	var_result = sq_diff / float(len(grades))
	return var_result


def grades_std_deviation(variance):
	return variance**0.5


variances = grades_variance(grades)



print "All of grades"
print_grades(grades)

print "Sum of grades"
print grades_sum(grades)

print "average"
print grades_average(grades)

print "variance"
print grades_variance(grades)

print "Standad variance"
print grades_std_deviation(variances)

