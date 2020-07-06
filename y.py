angle1 = int(input("Enter angle one:   "))
angle2 = int(input("Enter angle two:   "))
angle3 = int(input("Enter angle three:   "))
angletotal = angle1+angle2+angle3
if angletotal == 180:
	if angle1 == 60 and angle2 == 60 and angle3 == 60:
		print("equilateral")
	elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
		print("isoceles")
	else:
		print("scalene")
else:
	print("Not triangle")

#month = str(input("Enter month  "))
#if month == "1" or month == "january":
#	print("31")
#elif month == "2" or month == "february":
#	print("29")
#elif month == "3" or month == "march":
#	print("31")
#elif month == "4" or month == "april":
#	print("30")
#elif month == "5" or month == "may":
#	print("31")
#elif month == "6" or month == "june":
#	Print("30")
#elif month == "7" or month == "july":
#	print("31")
#elif month == "8" or month == "august":
#	print("31")
#elif month == "9" or month == "september":
#	print("30")
#elif month == "10" or month == "october":
#	print("31")
#elif month == "11" or month == "november":
#	print("30")
#elif month == "12" or month == "december":
#	print("31")
#
#




#c = input("Enter the charecter  ")
#print(c.isnumeric())
#if c isnumeric() == true:
#	print("Number")
#elif c.isalpha() == true:
#	print("Aphabet")
#else:
#	print("Charecter")
