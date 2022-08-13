class Human:

	def __init__(self, name, surname, birthday, sex):
		self.name = name
		self.surname = surname
		self.birthday = birthday
		self.sex = sex
		self.energy = 100

	def eating(self):
		self.energy += 5
		print('Human is eating')

	def sleeping(self):
		self.energy += 10
		print('Human is sleeping')

	def speaking(self):
		self.energy += 5
		print('Human is speaking')

	def walking(self):
		self.energy -= 10
		print('Human is walking')

	def doing_home_work(self):
		self.energy -= 90
		print('Human is doing home work')


man_1 = Human('Oleg', 'Korolev', '31.07.2000', 'male')
man_1.walking()
man_1.sleeping()
man_1.speaking()
print(man_1.energy)

man_2 = Human('Dima', 'Shevchenko', '23.04.2002', 'male')
man_2.doing_home_work()
man_2.eating()
man_2.walking()
print(man_2.energy)

man_3 = Human('Kirill', 'Varagen', '23.01.1999', 'male')
man_3.eating()
man_3.walking()
print(man_3.energy)

woman_1 = Human('Anya', 'Frolova', '11.09.1992', 'female')
woman_1.doing_home_work()
woman_1.speaking()
print(woman_1.energy)

woman_2 = Human('Elena', 'Kabarova', '23.02.1995', 'female')
woman_2.doing_home_work()
woman_2.speaking()
woman_2.walking()
woman_2.sleeping()
woman_2.speaking()
print(woman_2.energy)

max_energy_among_human = max(man_1.energy, man_2.energy, man_3.energy, woman_1.energy, woman_2.energy)
print(f"Самая большая енергия {max_energy_among_human} ")
