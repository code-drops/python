database = {
    "action":["robot","force","kick","kabir singh","baaghi","ek tha  tiger","rowdy rathore","dhoom","dabangg","wanted","singham","krish"],
    "horror":["pari","alone","raaz","stree","horror story","1920","1921","conjuring","insidious"],
    "space":["first man","martian","interstellar","mangal mission","gravity","star trek","avatar"],
    "biopic":["ms dhoni","bhaag milkha bhaag","mary kom","sanju","lincoln","dangal","modi"],
    "comedy":["dhamaal","golmaal","fukrey","housefull","3 idiots","de dana dan","welcome","hera pheri"]
}

user= {"robot","kick","kabir singh","rowdy rathore","dhoom","dabangg","wanted","singham","1920","1921","conjuring","insidious","martian","avatar","ms dhoni","bhaag milkha bhaag","sanju","de dana dan","welcome","hera pheri"}


# count the number of movies shown
score = {}
for key in database:
    s=len(user.intersection(database[key]))
    score[key]=s
print(score)

score = {}
# calculating the similarity score
for key in database:
    s = len(user.intersection(database[key]))/len(user.union(database[key]))
    score[key] = round(s*100,2)
print(score)

cat = max(score.items(),key=lambda i: i[1])[0]
for movie in database[cat]:
    if movie not in user:
        print("Suggested movie : ",movie)