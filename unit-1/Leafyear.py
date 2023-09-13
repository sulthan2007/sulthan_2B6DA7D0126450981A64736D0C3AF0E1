def leafyear(year):
	if (year%4  and year%100!=0) or year%400==0:
		return True 
	else:
		return False
	
year=int(input("enter  a year : "))
if leafyear(year):
	print("%d is leaf year"%(year))
else:
	print("%d is not  leaf year"%(year))