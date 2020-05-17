# text

text1 = '''Instagram is a free photo and video sharing app available on Apple iOS, Android and Windows Phone. People can upload photos or videos to our service and share them with their followers or with a select group of friends. They can also view, comment and like posts shared by their friends on Instagram. Anyone 13 and older can create an account by registering an email address and selecting a username.'''
text2 = '''Instagram is a free, online photo-sharing application and social network platform that was acquired by Facebook in 2012.Instagram allows users to edit and upload photos and short videos through a mobile app. Users can add a caption to each of their posts and use hashtags and location-based geotags to index these posts and make them searchable by other users within the app. Each post by a user appears on their followers' Instagram feeds and can also be viewed by the public when tagged using hashtags or geotags. Users also have the option of making their profile private so that only their followers can view their posts.'''

# tokenizing the text
t1 = text1.lower().split()
t2 = text2.lower().split()

# list of stopwords
stopwords = ['ourselves', 'hers', 'between', 'yourself', 'but','also', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

# removing stopwords from words_1
words_1 = []
for word in t1:
    if word not in stopwords:
        words_1.append(word)

# removing stopwords from words_2
words_2 = []
for word in t2:
    if word not in stopwords:
        words_2.append(word)

# list of punctuation marks that differ the same words
punctuation = [',','.','(',')','!',"'",'-','_']
'''
for word in words_1:
    for token in punctuation:
        if token in word:
            word = word.replace(token,'')
'''

# removing punctuation from words_1
for i in range(len(words_1)):
    for j in range(len(punctuation)):
        if punctuation[j] in words_1[i]:
            words_1[i] = words_1[i].replace(punctuation[j],'')

# removing punctuation from words_1
for i in range(len(words_2)):
    for j in range(len(punctuation)):
        if punctuation[j] in words_2[i]:
            words_2[i] = words_2[i].replace(punctuation[j],'')

# converting list to set for intersection and union
words_1 = set(words_1)
words_2 = set(words_2)


# jaccards distance
d = len(words_1.intersection(words_2)) / len(words_1.union(words_2))
print('Similarity score : ',d*100)
