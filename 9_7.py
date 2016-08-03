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
	print avr_result
	sq_diff = 0
	for n in grades:
		sq_diff += (avr_result - n)**2
		print sq_diff
	var_result = sq_diff / float(len(grades))
	print var_result
	return var_result

grades_variance(grades)



	




"""
Instructions
On line 18, define a new function called grades_variance() that accepts one argument, scores, a list.
First, create a variable average and store the result of calling grades_average(scores).
Next, create another variable variance and set it to zero. We will use this as a rolling sum.
for each score in scores: Compute its squared difference: (average - score) ** 2 and add that to variance.
Divide the total variance by the number of scores.
Then, return that result.
Finally, after your function code, print grades_variance(grades).
"""
