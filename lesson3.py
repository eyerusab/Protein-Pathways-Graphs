#Lesson 3 
#file hangling 
#with open("states.txt", 'r') as states_file:
#	states = states_file.read()

#print states


#file handling most common syntax
#with open('states.txt', 'r') as states_file:
#	print states_file.read()
	#read will allow you read the file when its open
#print states 

with open("states.txt", "r") as states_file:
	states= states_file.read().split("\n")

#print states 

#lets try it out: csv files
for index, state in enumerate(states):
	states[index] = state.split('\t') 
	# print index, state.split('\t')
print states 


#exercise part one
statenames = []
statesabbr = []
for state in states:
	statesabbr.append(state [0])
	statenames.append(state [1])
print statesabbr
print statenames
#states_abbr, states.append([0:]) 

#exercise part two
with open('statesabbr.txt', 'w') as statesabbr_file:
	statesabbr_file.write(" ".join(statesabbr))

print statesabbr_file

with open('statenames.txt', 'w') as statenames_file:
	statenames_file.write(" ".join(statenames))
	#statesabbr_file.write(statesabbr)


#dictionaries 
hmc_github= [['Sarah','sarahberlin']
,['Laura', 'lwrbel'], ['Emily', 'emeeks']]

phonebook = {'Shannon': '202-555-1234', 'Bridgeit': '703-555-9876', 'Christine': '410-555-1293'}
print phonebook['Bridgeit']
phonebook['Mel'] = '301-555-1111'
print phonebook



#Exercise
schools = {
    "geometry": {
        "coordinates": [
            -81.50572799999999, 
            39.21675500000001
        ], 
        "type": "Point"
    }, 
    "properties": {
        "address": "300 Campus Drive, Parkersburg, WV 26104", 
        "marker-color": "#3F3040", 
        "marker-symbol": "circle", 
        "name": "West Virginia University at Parkersburg"
    }, 
    "type": "Feature"
}

# Example Question: How could you "slice" the dictionary to print "Feature" from line 15?
# Answer: print schools["type"]

# Question 1: What slice will give you a dictionary 
#   with the key of "coordinates" and a value containing a list
#   of two decimal numbers?
print schools['geometry']['coordinates']

# Question 2: What slice will give you the address of the school?
print schools['properties']['address']
# Question 3: What slice will give you the name of the school?
print schools['properties']['name']
# Question 4: What slice will give you the latitude of the school? 
#   (Hint: the latitude is 39.216...)
print schools['geometry']['coordinates'][1]
# Question 5 (bonus): What slice will give you the marker-color 
#   without the hashtag in front?
print schools['properties']['marker-color'][1:]

#lists
#HMC3 = ['sarah', 'eyerusalem', 'nicky']

#for person in HMC3:
#	print person

#for index, person in enumerate(HMC3):
#	print index, person

#HMC3[0] = 'sarah is a person in this class'

#for index, perosn in enumerate(HMC3):
#	HMC3[index] = person + " is a person in this class"
#print HMC3  


#looping exercise 
contacts = {
    "Hear Me Code": {
        "twitter": "@hearmecode",
        "github": "https://github.com/hearmecode"
    },
    "Shannon Turner": {
        "twitter": "@svt827",
        "github": "https://github.com/shannonturner"
    },
}

# How to add a new item to an existing dictionary:
contacts["Aliya Rahman"] = {
    "twitter": "@AliyaRahman",
    "github": "https://github.com/aliyarahman"
}

# Exercise 1: Add a new dictionary item to contacts for each person at your table.
#   Rather than editing lines 1-10 above, add new entries to the contacts dictionary below.
#   Keep in mind some people may not have a twitter account, and that's okay!

contacts["Eyerusalem Abebe"] = {
    "twitter": "@eyerus_ab",
    "github": "https://github.com/eyerusab"
}

print contacts




for key in sorted(contacts.keys()):
	print contacts[key]['twitter']

print contacts.items()

#for key, value in contacts.items():
#	print key, '\t', value
#	for nested_key, nested_value in value.items():
#		print nested_key, nested_value

for key, value in contacts.items():
	print key
	for nested_key, nested_value in value.items():
		print nested_key, nested_value


# Exercise 2: Loop through the contacts dictionary to display everyone's contact information.
#   Your output should look like this:

#for nested_key, nested_value 
# Hear Me Code's info: 
#     twitter: @hearmecode
#     github: https://github.com/hearmecode
# Shannon Turner's info: 
#     twitter: @svt827
#     github: https://github.com/shannonturner