import json
from bs4 import BeautifulSoup
import mechanize
import time

print "Loading the Students Details..."
with open('students.json') as data_file:    
    students = json.load(data_file)

def get_cg(rollNo):
	url = 'https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno='+ rollNo.upper()
	br = mechanize.Browser()
	br.open(url)
	soup = BeautifulSoup(br.response().read().replace('&nbsp','').replace('<b>','<td>'))
	p = soup.findAll('td')
	temp = 1
	for i in range(0,len(p)):
		if(p[i].string==' CGPA'):
			temp+=1 
	temp = temp/2 + 1
	print ("Department: %s \nCGPA :"%(p[9].string))
	for j in range(0,len(p)):
		if(p[j].string==' CGPA'):
			if(p[j+1].string!=None and p[j+1].string != ' CGPA'):
				print("Semester %s --> %s"%(temp-1,p[j+1].string))
				temp-=1
				
def search_roll():
	roll = raw_input("\nEnter the Roll No you want to search :\n")
	for student in students:
		if roll == student["_aData"][1]:
			print "Following are the details of the student :"
			print "Name : " + student["_aData"][2]
			print "Hall : " + student["_aData"][3]
			print  "Room No : " +  student["_aData"][4]
			print "Current Status : " + student["_aData"][5]
			get_cg(student["_aData"][1])
			return
		else:
			continue
	print "No Student Found with that Roll No."

#Not a Full Working Function
def search_name():
	name = raw_input("\nEnter the Name of Student you want to search : \n")
	for student in students:
		if roll == student["_aData"][2]:
			print "Following are the details of the student :"
			print "Name : " + student["_aData"][2]
			print "Hall : " + student["_aData"][3]
			print  "Room No : " +  student["_aData"][4]
			print "Current Status : " + student["_aData"][5]
			get_cg(student["_aData"][1])
			return
		else:
			continue
	print "No Student Found with that Name."

#Initially Thought of implementing both search by Roll No and Name, but cannot finish it up. May be will develop it later.
# query = int(raw_input("How do you want to search the details : \n1) Roll No \n2) Name \n"))
# if query == 1:
# 	search_roll()
# elif query == 2:
# 	search_name()
# else:
# 	print "Please try later."

found = False
roll = raw_input("Enter the Roll No you want to search :\n")
for student in students:
	if roll == student["_aData"][1]:
		print "Following are the details of the student :"
		print "Name : " + student["_aData"][2]
		print "Hall : " + student["_aData"][3]
		print  "Room No : " +  student["_aData"][4]
		print "Current Status : " + student["_aData"][5]
		get_cg(student["_aData"][1])
		found = True
		break
	else:
		continue
if not found :
	print "No Student Found with that Roll No."


