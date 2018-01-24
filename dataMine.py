# dataMine.py
# 12/7/2016
# Python 3.4
# Program tells average of each month in a csv file.


myFile = open('table.csv')
previousYear = 2008
previousMonth = 9
sum = 0
counter = 0


for line in myFile:

	column = line.split(',')
	if column[0] == 'Date':
		continue
	
	date = column[0].split('-')
	currentYear = date[0]
	currentMonth = date[1]
	
			
	if previousYear == currentYear and previousMonth == currentMonth:
		
		sum = float(column[-1]) + sum
		counter = counter + 1
		
	elif counter > 0: 
		print("Year", currentYear, "Month", currentMonth, "Average", sum/counter)
		
	previousYear = currentYear
	previousMonth = currentMonth		
		

'''
Output:

Year 2008 Month 08 Average 436.8238461538461
Year 2008 Month 07 Average 467.2563636363637
Year 2008 Month 06 Average 484.56148148148134
Year 2008 Month 05 Average 504.35837837837835
Year 2008 Month 04 Average 519.4787234042553
Year 2008 Month 03 Average 514.8123478260869
Year 2008 Month 02 Average 504.2509701492539
Year 2008 Month 01 Average 504.4075816993465
Year 2007 Month 12 Average 517.0987283236994
Year 2007 Month 11 Average 534.7633333333333
Year 2007 Month 10 Average 548.043537735849
Year 2007 Month 09 Average 555.9496581196581
Year 2007 Month 08 Average 554.7343650793648
Year 2007 Month 07 Average 551.1091605839414
Year 2007 Month 06 Average 549.9183333333331
Year 2007 Month 05 Average 547.6711146496814
Year 2007 Month 04 Average 542.9165970149251
Year 2007 Month 03 Average 539.1402259887002
Year 2007 Month 02 Average 534.2974399999997
Year 2007 Month 01 Average 531.2702798982186
Year 2006 Month 12 Average 529.3673300970871
Year 2006 Month 11 Average 526.9345707656609
Year 2006 Month 10 Average 525.104811529933
Year 2006 Month 09 Average 521.2661864406776
Year 2006 Month 08 Average 516.450061099796
Year 2006 Month 07 Average 510.4707407407406
Year 2006 Month 06 Average 506.6834210526316
Year 2006 Month 05 Average 502.3423327305606
Year 2006 Month 04 Average 498.0261149825784
Year 2006 Month 03 Average 495.45748310810797
Year 2006 Month 02 Average 490.5127035830616
Year 2006 Month 01 Average 487.09207278480994
Year 2005 Month 12 Average 485.9044086021504
Year 2005 Month 11 Average 483.9149031296571
Year 2005 Month 10 Average 481.4527206946453
Year 2005 Month 09 Average 476.910787623066
Year 2005 Month 08 Average 472.16982216142264
Year 2005 Month 07 Average 466.7588047808764
Year 2005 Month 06 Average 462.62415803108803
Year 2005 Month 05 Average 457.9794451450189
Year 2005 Month 04 Average 452.5637638376382
Year 2005 Month 03 Average 446.45600240096013
Year 2005 Month 02 Average 439.93304449648673
Year 2005 Month 01 Average 434.88542431192633
Year 2004 Month 12 Average 429.7209764309761
Year 2004 Month 11 Average 423.99949561403486
Year 2004 Month 10 Average 418.7048927038624
Year 2004 Month 09 Average 413.08841386554593
Year 2004 Month 08 Average 406.9015843621397
'''
