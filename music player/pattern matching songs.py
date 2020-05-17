import os
import glob

os.chdir("E:\Music")
pattern = input("Enter starting alphabet")
pattern = pattern.lower()
l = len(pattern)
length = l
for i in range(1, l * 2, 2):
    pattern = pattern[0:i] + "*" + pattern[i:]
pattern = "*" + pattern + ".mp3"
songs = glob.glob(pattern)
print(songs)
