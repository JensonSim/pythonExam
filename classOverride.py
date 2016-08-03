class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00



class PartTimeEmployee(Employee):
	"""docstring for PartTimeEmployee"""

	def __init__(self, employee_name):
		super(Employee, self).__init__()

	def calculate_wage(self, hours):
		self.hours = hours
		return hours * 12.00

	def full_time_wage(self, hours):
		return super(PartTimeEmployee, self).calculate_wage(hours)
		""
milton = PartTimeEmployee("milton")
print milton.full_time_wage(10) """슈퍼파워로 모클래스 메소드 호출"""
print milton.calculate_wage(10)	"""노말하게 소속 클래스 메소드 호출"""
