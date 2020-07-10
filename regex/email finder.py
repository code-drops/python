import re

''' tony.stark@avengers.com '''
email = re.compile(r'([a-zA-z0-9._-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,4})')

text = "An email address identifies an email box to which email +91-1234567898 messages are delivered. A wide variety  of formats were used in early email systems, but only a single format is used today, following the specifications[a] developed for Internet mail systems since the 1980s. This article uses the term email address to refer to the addr-spec defined in RFC 5322, not to the address that is commonly used; the difference is that an address may contain a display name, a comment, or both.An email address such as John.Smith@example.com is made up of a local-part, an @ symbol, then a case-insensitive domain. Although the standard requires[1] the local part to be case-sensitive, it also urges that receiving hosts deliver messages in a case-independent fashion,[2] e.g., that the mail system at example.com treat John.Smith as equivalent to john.smith; some mail systems even treat them as equivalent to johnsmith.[3] Mail systems often limit their users' choice of name to a subset of the technically valid characters, and in some cases also limit which addresses it is possible to send mail to.With the introduction of internationalized domain names, efforts are progressing to permit non-ASCII characters in email addresses"

matches = []

# It will find all the patterns in the text and then returns a list
# the element at index represents the largest string matched(largest/outer group)
for match in email.findall(text):
    matches.append(match)

print(matches)