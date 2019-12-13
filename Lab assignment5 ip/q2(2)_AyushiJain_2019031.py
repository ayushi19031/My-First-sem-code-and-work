def DateMeRight(date):
	"""Returns the given date in DD-MMM-YYYY format, where MMM is the string of the first 3 Letters of the Month.
	Parameters:
	date: a String in DD.MM.YYYY format""" 
	s_index=date.find(".")
	e_index=date.rfind(".")
	month=date[s_index + 1:e_index] 
	month_str=""
	
	if(int(month)<=6):
		if(int(month)<3):
			if(month=="1"):
				month_str="Jan"
			elif(month=="2"):
				month_str="Feb"
					
		else:
			if(month=="3"):
				month_str="Mar"
			elif(month == "4"):			
				month_str="Apr"
			elif(month == "5"):
				month_str="May"
			else:
				month_str = "Jun"				
	else:
		if(int(month)>=9):
			if(int(month)==10):
				month_str="Oct"
			elif (month == "11"):					
				month_str="Nov"
			elif(month=="12"):
				month_str="Dec"
			elif (month == "9"):
				month_str = "Sep"	
		elif(int(month)<9):
			if(month=="6"):
				month_str="Jun"		
			elif(month=="7"):
				month_str="Jul"	
			else:
				month_str="Aug"		

	return date[0:s_index]+"-"+month_str+"-"+date[e_index+1:]


d="5.12.1533"
print(DateMeRight(d))