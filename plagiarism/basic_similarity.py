# text
text1 = '''Instagram is a free photo and video sharing app available on Apple iOS, Android and Windows Phone. People can upload photos or videos to our service and share them with their followers or with a select group of friends. They can also view, comment and like posts shared by their friends on Instagram. Anyone 13 and older can create an account by registering an email address and selecting a username.'''
text2 = '''Instagram is a free, online photo-sharing application and social network platform that was acquired by Facebook in 2012.Instagram allows users to edit and upload photos and short videos through a mobile app. Users can add a caption to each of their posts and use hashtags and location-based geotags to index these posts and make them searchable by other users within the app. Each post by a user appears on their followers' Instagram feeds and can also be viewed by the public when tagged using hashtags or geotags. Users also have the option of making their profile private so that only their followers can view their posts.'''

# converting it to lower and then to set that able to find intersection and union between them easily
t1 = set(text1.lower().split())
t2 = set(text2.lower().split())

# calculating the jaccards distance
d = len(t1.intersection(t2))/len(t1.union(t2))
print(d*100)

# Problem : 
# It has problem of NLP .
# NLP has four steps :
# 1) Tokenization : splitting the terms
# 2) remove stopwords : removing words like is,am,are,like,how,which,etc. that are necessary to use make sentences
# 3) stemming : converting verbs to normal forms like go , went , gone are same
# 4) vectors : frequency of words