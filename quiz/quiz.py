'''
create quiz for 35 students with 50 ques each
'''

import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for numquiz in range(35):
    # quiz file
    quizfile = open('C:/Users/dell/PycharmProjects/test/venv/Lib/quiz/quiz'+str(numquiz+1)+".txt",'w')

    # answers file
    answerskeyfile = open('C:/Users/dell/PycharmProjects/test/venv/Lib/quiz/quizanswers'+str(numquiz+1)+".txt",'w')

    # headers for file
    quizfile.write("Name : \n\nDate : \n\nPeriod : \n\n")
    quizfile.write(' '*10 + "State capital quiz(Form "+str(numquiz+1)+")\n\n")
    
    # list of states
    states = list(capitals.keys())
    random.shuffle(states)

    for ques in range(50):
        
        # creating options
        right = capitals[states[ques]]
        wrong = list(capitals.values())
        wrong.remove(right)
        wrong = random.sample(wrong,3)
        options = [right] + wrong
        random.shuffle(options)

        # writing into file
        quizfile.write(str(ques+1)+'. What is the capital of '+str(states[ques])+" ?\n")
        for i in range(4):
            quizfile.write(' %s. %s\n' % ('ABCD'[i], options[i]))
        quizfile.write('\n')

        answerskeyfile.write('%s. %s\n' % (ques + 1, 'ABCD'[options.index(right)]))

# closing file
quizfile.close()
answerskeyfile.close()
