# "":{"action","adult","animated","army","comedy","crime","disaster","emotional","fantasy","horror","real","romance","sci fi","series","space","sports","survival","thriller","war"},

import random
database ={
    "1920 evil returns":{"adult","emotional","horror","romance","thriller"},
    "2012":{"disaster","fantasy","survival","thriller"},
    "3 idiots":{"adult","comedy","emotional","romance"},

    "aashiqui 2":{"adult","emotional","romance"},
    "ae dil hai mushkil":{"adult","comedy","emotional","romance"},
    "aiyaary":{"action","army","comedy","crime","emotional","romance","thriller"},
    "ajab prem ki ghazab kahani":{"action","comedy","emotional","romance"},
    "american pie":{"adult","comedy","fantasy","romance","series"},
    "anabelle":{"horror","series","thriller"},
    "angrezi medium":{"comedy","crime","emotional"},
    "anjaana anjaani":{"adult","comedy","emotional","romance"},
    "attacks of 26/11":{"action","adult","army","crime","disaster","emotional","real","survival","thriller"},
    "avatar":{"action","animated","fantasy","sci fi","war"},
    "avengers":{"action","comedy","disaster","emotional","fantasy","sci fi","series","space","war"},
    "a gentleman":{"action","adult","comedy","crime","romance","thriller"},

    "baby":{"action","army","crime","thriller"},
    "bang bang":{"action","adult","army","comedy","crime","emotional","romance"},
    "barfi":{"adult","comedy","emotional","romance"},
    "bareilly Ki barfi":{"comedy","emotional","romance"},
    "batla house":{"action","army","crime","emotional","real","thriller","war"},
    "bhaag milkha bhaag":{"adult","comedy","emotional","real","romance","sports"},
    "bhagam bhaag":{"comedy","emotional","romance"},
    "bhool bhulaiya":{"adult","comedy","emotional","horror","romance","thriller"},
    "boss baby":{"animated","comedy","emotional","fantasy"},
    "brochara":{"adult","comedy","emotional","romance"},

    "chak de india":{"comedy","emotional","real","sports","thriller"},
    "chandni chowk to china":{"action","comedy","emotional","romance"},
    "chennai express":{"action","comedy","emotional","romance"},
    "chichhore":{"adult","comedy","emotional","romance"},
    "college romance":{"adult","comedy","emotional","romance","series"},
    "commando":{"action","army","crime"},
    "conjuring":{"horror","series","thriller"},
    "crew":{"disaster","emotional","space","survival","thriller"},
    "cubicles":{"adult","comedy","emotional","romance","series"},

    "dabangg":{"action","army","comedy","emotional","romance","series"},
    "dangal":{"comedy","emotional","real","sports","thriller"},
    "de dana dhan":{"comedy","romance"},
    "desi boyz":{"adult","comedy","emotional","romance"},
    "dhamaal":{"comedy","crime"},
    "dhan dhana dhan goal":{"comedy","emotional","romance","sports"},
    "dhoom":{"action","adult","army","comedy","crime","emotional","romance","sci fi","series","survival","thriller"},
    "dilwale":{"action","comedy","crime","emotional","romance"},
    "don":{"action","adult","comedy","crime","romance","sci fi","series","thriller"},
    "dostana":{"adult","comedy","emotional","romance"},
    "do lafzon ki kahani":{"action","adult","comedy","crime","emotional","romance","sports","survival","thriller"},
    
    "drishyam":{"crime","emotional","thriller"},
    
    "ek villian":{"action","comedy","crime","emotional","romance","thriller"},
    "ek tha tiger":{"action","comedy","crime","emotional","romance"},
    "edge of tomorrow":{"action","army","comedy","disaster","sci fi","war"},
    
    "fashion":{"adult","comedy","emotional","romance","survival"},
    "flames":{"adult","comedy","emotional","romance"},
    "force":{"action","adult","army","comedy","crime","emotional","romance","series"},
    "fukrey":{"adult","comedy","crime","emotional","romance","series"},
    
    "gabbar is back":{"action","army","comedy","crime","emotional","romance","thriller"},
    "galaktic football":{"action","animated","comedy","emotional","sports"},
    "garam masala":{"adult","comedy","emotional","romance"},
    "golmaal":{"adult","comedy","emotional","romance","series"},
    "good newwz":{"adult","comedy","emotional","romance"},
    "grand masti":{"adult","comedy","emotional","romance","series"},
    "gully boy":{"adult","comedy","emotional","real","romance"},
   
    "hasee to phasee":{"adult","comedy","emotional","romance"},
    "happy new year":{"action","comedy","crime","emotional","romance"},
    "harry potter":{"action","crime","emotional","fantasy","series","thriller","war"},
    "hera pheri":{"comedy","emotional","series"},
    "heyy babyy":{"adult","comedy","emotional","romance"},
    "holiday":{"action","army","comedy","crime","romance","thriller"},
    "home alone":{"comedy","crime","emotional","series","survival"},
    "hostages":{"action","adult","army","crime","emotional","romance","series","survival","thriller"},
    "how to train your dragon":{"action","animated","comedy","emotional","fantasy","series","war"},
    
    "immature":{"adult","comedy","emotional","romance","series"},
    "IT":{"emotional","fantasy","horror","series","survival","thriller"},
    
    "jab we met":{"adult","comedy","emotional","romance"},
    "jai ho":{"action","army","comedy","emotional","romance"},
    "jawaani janeman":{"adult","comedy","emotional","romance"},
    
    "kaabil":{"action","adult","comedy","crime","emotional","romance","thriller"},
    "kabir singh":{"action","adult","comedy","emotional","romance"},
    "kapoor and sons":{"comedy","emotional","romance"},
    "karate kid":{"action","comedy","emotional","romance","sports","survival"},
    "kesari":{"action","adult","army","comedy","emotional","real","romance","war"},
    "kgf":{"action","comedy","crime","emotional","romance","survival"},
    "kis kis ko pyaar karu":{"adult","comedy","emotional","romance"},
    "kota factory":{"comedy","emotional","romance","series"},
    "kung fu hustle":{"action","comedy","emotional","romance","survival","war"},
    
    "london has fallen":{"action","army","crime","disaster","series","thriller","war"},
    "luka chupi":{"adult","comedy","emotional","romance"},
    
    "mad max":{"action","adult","survival","war"},
    "madras cafe":{"action","army","survival","thriller"},
    "main tera hero":{"action","comedy","romance"},
    "martian":{"disaster","sci fi","space","survival","thriller"},
    "mission mangal":{"comedy","emotional","real","sci fi","space"},
    "ms dhoni":{"comedy","emotional","real","romance","sports"},
    "munnabhai mbbs":{"adult","comedy","emotional","romance","series"},
    "murder":{"action","adult","army","comedy","crime","emotional","romance","series"},
    "my name is khan":{"adult","comedy","disaster","emotional","romance","survival"},
    
    "namaste london":{"adult","comedy","emotional","romance"},
    "now you see me":{"comedy","crime","fantasy","thriller"},
    
    "omg":{"comedy","emotional"},
    "olympus has fallen":{"action","army","crime","disaster","emotional","survival","thriller","war"},
            
    "padmaavat":{"action","adult","army","comedy","crime","emotional","real","romance","thriller","war"},
    "partner":{"adult","comedy","romance"},
    "players":{"action","adult","comedy","crime","emotional","romance","sci fi"},
    "pyaar ka punchnama":{"adult","comedy","emotional","romance","series"},
    "pyaar lafzon me kahan":{"comedy","emotional","romance","series"},
    
    "quiet place":{"action","horror","series","survival","thriller"},

    "raazi":{"adult","army","crime","emotional","romance","survival","thriller"},
    "rajkumar":{"action","adult","comedy","romance"},
    "ramaiya vastavaiya":{"comedy","emotional","romance"},
    "rang de basanti":{"action","comedy","crime","disaster","emotional","real","romance","war"},
    "ready":{"action","comedy","romance"},
    "real steel":{"action","fantasy","sci fi"},
    "resident evil":{"action","adult","disaster","fantasy","series","survival","war"},
    "redline":{"action","adult","comedy","crime","romance","series","sports"},
    "roar of the lion":{"crime","emotional","real","series","sports","thriller"},
    "rockstar":{"action","adult","comedy","crime","emotional","romance"},
    "rocky handsome":{"action","crime","emotional","survival"},
    "rowdy rathore":{"action","adult","army","comedy","emotional","romance"},
    "rustom":{"action","adult","army","comedy","crime","emotional","real","romance","thriller"},

    "salt":{"action","adult","crime","survival"},
    "sanju":{"adult","comedy","crime","emotional","real","romance"},
    "satyamev jayate":{"action","adult","army","comedy","crime","emotional","romance"},
    "shaolin soccer":{"comedy","emotional","fantasy","sports"},
    "simmba":{"action","adult","army","comedy","crime","emotional","romance"},
    "singham":{"action","army","comedy","crime","emotional"},
    "special 26":{"army","comedy","crime","emotional","real","romance","thriller"},
    "sonu ke titu ki sweety":{"adult","comedy","emotional","romance"},
    "shoot em up":{"action","adult","comedy","crime","survival"},
    "sultan":{"action","comedy","emotional","romance"},
    
    "tamasha":{"comedy","emotional","romance"},

    "underworld":{"action","adult","crime","emotional","fantasy","romance","sci fi","series","survival","thriller","war"},
    "uri":{"action","army","crime","disaster","emotional","real","survival","thriller","war"},
    
    "veer":{"action","comedy","emotional","romance","war"},
    "venom":{"action","comedy","crime","sci fi"},
    
    "wanted":{"action","adult","army","comedy","crime","emotional","romance"},
    "wednesday":{"army","crime","disaster","emotional","thriller"},
    "welcome":{"comedy","romance","series"},
    
    "ye jawaani hai deewani":{"adult","comedy","emotional","romance"},
    
    "znmd":{"adult","comedy","emotional","romance"},
}

flag = False
movies = set()

for movie in database:
    movies.add(movie)

inc_genre = input("Included genres : " )

# to split it into list
genres = list(inc_genre.split(","))
print(genres)

for genre in genres:
    temp = set()
    for movie in database:
        if genre in database[movie]:
            temp.add(movie)
    movies = movies & temp

exc_genre = input("Excluded genres : " )

# to split it into list
genres = list(exc_genre.split(","))
print(genres)

for genre in genres:
    temp = set()
    for movie in database:
        if genre in database[movie]:
            temp.add(movie)
    movies = movies - temp

for i in range(5):
    print(random.choice(list(movies)))
