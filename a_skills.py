import json
import os.path
from os import path

def prompt_0():
	print("*** *** *** *** *** *** *** *** *** *** *** ")
	print("")
	print("Welcome to the Skills Tracking Program!")
	print("")
	print("Here are your options:")
	print("Press 1 to view current skills being tracked -- ")
	print("Press 2 to enter new skills -- ")
	print("Press 3 to delete a skill(s) -- ")
	print("Press 4 to exit this program")
	print("")
	print("Thanks!\n")

	
def prompt_1(data):
	print("Current Skills")
	for key in data:
		print(f"{key}: {data[key]} Hours")
	i = input("Do you want to continue? Y/n? ")
	if i == 'Y' or 'y':
		pass
	else: 
		prompt_4()


		
def prompt_2(data):
	for i in range(0, 20):
		print("-------------Enter New Skill-----------------")
		skill = input("Input Skill (or type 'menu'): ")
		if skill == "menu":
			prompt_0()
			break
		time = input("How many hours have you worked on this skill: ")
		if skill == "":
			pass
		data[skill] = time

	

	
	
def prompt_3(data):
	del_skill = input("What skill would you like to delete: ")
	del data[del_skill]
	i = input("Do you want to continue? Y/n? ")
	if i == 'Y' or 'y':
		pass
	else: 
		prompt_4()

	
def prompt_4():
	print("END ********************************\n\n")
	running = False # What's happening here? 
	exit()






def main():
	skill = "New Skill"
	time = 0
	skill_dictionary = {}

	if path.exists("skills_json"):
		with open("skills_json", "r") as f:
			data = json.load(f)
			#print(data)
	else:
		with open("skills_json", "w") as f:
			data = skill_dictionary


	running = True

	#while running:
		
	# REPL
	# Prompt for view, add, delete, quit
	# Make a dictionary that references the functions
	# Make a function for each option
	# try dict[i]()
	# except keyerror: . . .
	# All within a while loop, quit() running = to false, etc. 


		
	prompt_dict = {0:prompt_0, 1:prompt_1, 2:prompt_2, 3:prompt_3, 4:prompt_4}
		
	while running: # I can get into prompt_1 and prompt_2 and prompt_3 and prompt_4
		prompt_0()
		try:
			i = int(input())
			if i == -1:
				break
			prompt_dict[i](data)
			with open("skills_json", "w") as outfile:
				json.dump(data, outfile)
		except KeyError:
			print("Invalid input . . . ")

		

	# [ ] clean up the look: add new lines, etc. 
	# [ ] pause on each menu instead of automatically going back to the main menu
	# [ ] create a main function

main()

