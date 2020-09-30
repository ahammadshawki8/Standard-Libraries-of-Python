# Regular Expressions in Python
# in this module, we will learn how to use regex in Python using the built in re module.

# Regular Expressions also known as regex.
# they basically allows us to search for and match specific patterns of text. 
# they can look extreamly complicated thats because there is so much that we can do with them.
# we can create a regular expression just about any pattern of thinks that we can think of.

# lets look at some example
# first of all we need to import the re module
import re

# and the text we are going to search is this multiline string here.
text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \\ | ( )

ahammadshawki8.github.io

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
rat
bat
"""

sentence = "Start a sentence and then bring it an end"

# Before writing our first regular expression we need to know waht a raw string is
# because we rae going to use this a lot throuout this module.
# a raw string is python is just a string prefixed with an R
# and that tells Python not to handle back slashes in any special way.
# normally, backslashes are useful to specify tabs  or new lines and things like that.
# but a raw strng will just interpret the sting literally.

print(r"\tTAB")
# we can see the back slash is no longer handled in any special way.

# To find patterns, we are going to use the re.compile() method.
# It will allow us to separate our patterns into a variable 
# and also we'll be able to resuse the variable to perform multiple searches.

pattern = re.compile(r"abc")
# first lets specify a pattern that matches some literal character.
# we can searh for "abc"
# now that we have specified that pattern, now we will search through our text with that pattern.

matches = pattern.finditer(text_to_search)
# here we have pass our string variable which we want to search through.
# matches is a list containing all the matches.

# printing all the matches.
for match in matches:
    print(match)

# we can see that this finditer() method returns all an iterator that contains all the matches.
# we are going to look some other regular expression finding patterns methods in a moment.
# but finditer() is one of the best method for gathering all of the metches in an easy to read format.

# each of this matched objects shpws us the span and the match itself.
# the span is the beginning and the ending of the index.

# this span is useful because it enables us the string slicing functionality of python 
# where we can plug in the span as the index and grab the match from the string.
print(text_to_search[1:4]) 

# we can see that our search metched the small abc but it didn't match the capital ABC.
# thats because this is case sensitive.
# and this search right now is also looking for abc in that specific order.
# if we search for "cba" we dont have any mathes.
pattern = re.compile(r"cba")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# we can see in the text there are some metacharacters that need to be escaped.
# for example, if we want to search for a "."
pattern = re.compile(r".")
matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
# we can see that it matches with everything. because .(dot) is a metachracter.It matches with everything.

# so if we really want to search for a dot(.)
# we need to escape it with a backslash.
pattern = re.compile(r"\.")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# so we can see that they are actual dots. So, escaping goes for any of those metachracters.
# MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )

# One practical example of these might be a url.
# I have a url here called "ahammadshawki8.github.io"
# if we want to match that exact url, we need to escape the dot(.)
pattern = re.compile(r"ahammadshawki8\.github\.io")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# we did match the url.

# A literal search is not so much exiting because that is something that we probably know how to do it with Python.
# really, we want to use regular expression to search for patterns.
# And to do this we are going to use some of this meta characters that we were just escaping.

# we have some types of values where we can see the types of chaaracters that we can match.
    # .       - Any Character Except New Line
    # \d      - Digit (0-9)
    # \D      - Not a Digit (0-9)
    # \w      - Word Character (a-z, A-Z, 0-9, _)
    # \W      - Not a Word Character
    # \s      - Whitespace (space, tab, newline)
    # \S      - Not Whitespace (space, tab, newline)

    # \b      - Word Boundary
    # \B      - Not a Word Boundary
    # ^       - Beginning of a String
    # $       - End of a String

    # []      - Matches Characters in brackets
    # [^ ]    - Matches Characters NOT in brackets
    # |       - Either Or
    # ( )     - Group

    # Quantifiers:
    # *       - 0 or More
    # +       - 1 or More
    # ?       - 0 or One
    # {3}     - Exact Number
    # {3,4}   - Range of Numbers (Minimum, Maximum)

# Now, lets walk through each of these and see what we can do with the regular expressions.
# . matches any character except the new line we have seen that a bit ago.
# \d matches any digit between 0 and 9
pattern = re.compile(r"\d")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# \D matches anything that is not a digit between 0 and 9
# this is kind of common them with this special characters.
# Capital letters basically negate whatever the lowercase version means.
pattern = re.compile(r"\D")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# \w is for searching a word character.
# a word character is anything that is lowercase or uppercase letter, digits or an underscore _
pattern = re.compile(r"\w")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# \W is the opposite
pattern = re.compile(r"\W")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# \s matches any whitespace, that can be space, tab or newline.
pattern = re.compile(r"\s")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# \S is the opposite
pattern = re.compile(r"\S")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# the lower metacharacters are little different. 
# these are called "anchors".
# they dont actually match any chracters 
# but rather invisible positions before and after characters.
# and we can use this as conjuctin with other paterns for searching.

# \b means words boundary
# word boundaries are indicated by whitespaces or a non alphaneumeric character.
# we can see that we have 3 Ha in the text_to_search.
# lets say we want to match all of the Ha's that have a word boundary directly before.
# we can search that by,
pattern = re.compile(r"\bHa")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# we can see that it matches with two Ha, the first and the second.
# it doesn't matches the last one because it was in the middle of a word with no boundary.
# if we use the uppercase B instead of lowercase,
pattern = re.compile(r"\BHa")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# we only get the last Ha

# Now we have a ^ and a $ sign
# the ^ will match a positin that is a beginning of a string
# the $ will match a positin that is a end of a string
# we have created a small sentence variable that we are going to use to demonstrate this.
pattern = re.compile(r"^Start")
matches = pattern.finditer(sentence)
for match in matches:
    print(match)
# here we searched for the Start which is at the beginning of a string.
# we can do something simmilar using the $ sign for endinf of the sentence.
pattern = re.compile(r"$end")
matches = pattern.finditer(sentence)
for match in matches:
    print(match)


# Now lets say we wanted to match the phone numbers within the multi-lined string.
# we cant use the literal characters because they are differnt.
# but they have some patterns in common. So, we need to use the meta characters.
pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# we can see that it match both of our phone numbers.



# Now we are seeing this how can be these become powerful.
# we have a data.txt file here we have bunch of fake names, addresses, mobile numbers and emails
# so lets open this file in python and lets see if we can parse the phone number from this files using regex.
with open("data.txt","r") as f:
    contents = f.read()
    pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)


# Now lets say that we only want to match a phone number if it only have a dash- or a dot.
# right now this pattern will match any separator that is here because we used .
# to only match a dash or dot, we can use something called character set.
# character set uses the square brackets [] for the characters we want to match.
pattern = re.compile(r"\d\d\d[-.]\d\d\d[-.]\d\d\d\d")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# we can see that we aren't matching that number which has a * as a separator.
# Also we didn't need to escape our - and . within the character set.
# thats because character set have slightly different rules.
# we can escape them if we lke but they will then become hard to read.

# even we have a - in character set, it only matches a single - or . as a separator.
# if we have multiple -- then, it wont going to match.
# so BE CAREFUL about this
# Character set may have multiple elements in it, but t only matches with a single character.

# No lets us just match the 800 or 900 numbers.
pattern = re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d\d")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# we can perform the same search in our data.
with open("data.txt","r") as f:
    contents = f.read()
    pattern = re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d\d")
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)
# we can see that works

# Within a character set the dash is actually a special character as well.
# when it is put in the beginning or the end, it will just match the literal - character
# but when it placed between values it can specify a range of values
# for example, it we want any digit between 1 and 5 then,
pattern = re.compile(r"[1-5]") # this is going to spcify a range
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# we can use this ranges for letters as well
# if we want to match from a to h, then we can
pattern = re.compile(r"[a-h]")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# if we want to match both the lowercase and the upercase, 
# then we need to use the ranges back to back in the character set.
pattern = re.compile(r"[a-hA-H]")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# we can keep adding to that, we can add digits there.

# Another special character in the character set is the ^ (carat)
# outside of a character set it matches the beginning of a string.
# but within a character set it negates the set and matches everything that is not in the character set.
# it actually makes the character set opposite
pattern = re.compile(r"[^a-zA-Z]")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# it will match everything that is not a lower and uppercase letter.

# lets say now we want to match all the 3 letters word that ends ith "at"
# but we dont want to match for bat
pattern = re.compile(r"[^b]at")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# Everything we have looked at has involved single character so far.
# we can use "qauntifiers" to match more han one character at once.
pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# here we are matching all of our digits one character at a time.
# and its easy to make mistake when we have lots of these type.
# but we can use quantifiers to match multiple character at a time.

# * will match 0 or more of the pattern we are looking for.
# + will match 1 or more
# ? will match 0 or 1
# if we use the curly braces with a single number that will match the exact number {3}
# if we have two numbers in it separated by a comma {3,7}
# then it matches with a range of numebrs from the minimum to tha maximum.

# for our phone number we can use the {} with single number.
pattern = re.compile(r"\d{3}.\d{3}.\d{4}")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# we can see that we are still getting the same result.

# sometimes we dont know the exact numbers and use these other quantifiers.
# for example, in the text_to_search we have some names.
# some start with the prefix Mr, some with Ms, some with Mrs.
# lets say we want to write a pattern that will match these prefixes and the name afterwards.

# if we want to match the name which starts with Mr,
pattern = re.compile(r"Mr\.?\s[A-Z]\w*")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# here . is optional, so we need either 0. or 1., so we will use ?
# then we have a space so we will use \s
# then we have uppercase so we need to use a character set A-Z
# now we want to match any word charcter after the uppercase and we can do that by \w*

# How would we do the Mrs. and the Ms.
# the better solution is to use a group.
# Groups allow us to match several different patterns,
# to create a group we use parenthesis ()
# within this parenthesis we can match some patterns.
pattern = re.compile(r"M(r|rs|s)\.?\s[A-Z]\w*")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
# we can use vertical bar character which is basically or.

# we can do it with little more clearer.
pattern = re.compile(r"(Mr|Mrs|Ms)\.?\s[A-Z]\w*")
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)



# These groups can actually be used to capture sections of your matched regular expression.
# we wil look at in just a bit.

# But now lets do some real-word examples to quicly recap what we have learned so far.

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# here we have 3 different email addresses within this emails string.
# lets try to write a regular expression that will match all of these emails.
# first lets match the first email address.
pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
matches = pattern.finditer(emails)
for match in matches:
    print(match)
# first we have a uppercase or lowercase letters so we used [a-zA-Z]
# and then we want to match 1 or more of them, so we used + until we read the @ symble
# then we have the email host name, so we used [a-zA-Z]+
# finally we need to match the .com so we need to add \.com

# Now we matched the first email
# Now lets matach the second email
pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')
matches = pattern.finditer(emails)
for match in matches:
    print(match)
# we need to allow a . in the first part of the email.
# we can add that just by adding a . in the character set.
# and we need a .edu as well as .com, we can use a group

# Now we need tomatch our final address
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
matches = pattern.finditer(emails)
for match in matches:
    print(match)
# we need to allow - and digits in the first part, we can do that by [a-zA-Z0-9.-]
# we also have a - in the email hosting name.
# and lastly we need to add net with a vertical bar in the group |net

# Something like email addresses can be pretty tough to write from scratch of our own.
# there are lot of these regex available online.
# and once we earn how to write regular expressions, 
# then we should be able to read them and figure out what they match.

# so lets try to understand what other people's regular expression matches.
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# here first we have a character set that matches 
    # all lowercase letters
    # all uppercase letters
    # all digits
    # a _
    # a .
    # a +
    # a -
# then we have + sign that will match one or more of any of those charcters in the character set.
# it matches all the way upto it hits @ symbol
# after the @ sign, we have another character set, it matches
    # all lowercase letters
    # all uppercase letters
    # all digits
    # a -
# then again we have + sign that will match one or more of any of those charcters in the character set.
# it matches all the way upto it hits . symbol which is escaped by \,
# then we have another character set which matches,
    # all lowercase letters
    # all uppercase letters
    # all digits
    # a -
    # a .
# then again we have + sign that will match one or more of any of those charcters in the character set.

# this pattern may be hard to understand.
# but if we walk through bit b bit then we should be able to understand any pattern just like this.



# The last concept we will look at is to how to capture information from groups.
# to show an example of this we will take a urls multiline variable.
urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

# Some of this urls start with http and some of them start with https
# some of them have www. for domain and some of them dont
# they are pretty inconsistant

# lets say, for each of the urls we want to grab the domain name followed by he top-level domain 

# first lets make a pattern that actually matches this urls.
pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
matches = pattern.finditer(urls)
for match in matches:
    print(match)
# here first we need http, and then a optional s, so we write https?
# then we need to match ://
# here we have optional www. , here we can use a group and that entire group is optional
# remember we have to escape the .
# now we can match any word character 1 or more \w+
# we want to make all the way up to . We need to escape that \.
# then we match the top level domain
# so we will match 1 or more word characters \w+

# now we can see that we are matching all the urls
# now lets capture the domain name and the top-level domain
# to capture those sections we can put them in a group
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match)

# since we add groups in an existing expression, it shouldn't actually change our results.
# But now we have three different groups
# number 1 group is optinal www.
# number 2 group is the domain name
# number 3 group us the top-level domain
# there is a group 0, and it is everything that we captured so it is the entire url.

# to show the groups, our match object has a group() method and we can pass in the index of the group to see them.
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(0))
    # group 0 is the entire url

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(1))
    # this is optional www.
    # we can see that the urls that dont have a www. they return None

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(2))
    # group 2 is the domain name

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(3))
    # group 2 is the top-level domain name


# Now we can use something called a back reference to reference our captured group
# its basically a shorthand for accessing this groups indexes
# so the re module has a sub() method that we can use for substitution.

# we can create a variable
subbed_urls = pattern.sub(r'\2\3',urls)
# here we have to pass in the substitutions
# we want to substitute the whole url with the domain name and the top-level domain
# domain name was group2 and top-level-domain was group3
# for back reference we need to use \ before the group index like this \2\3 

# now we need to pass in the text that we want to replace.
print(subbed_urls)
# we can see that it returns a new string with those substituted urls.
# so, if we have a large document of thing that we want to reformate like this,
# then learning how to do this with regular expression will allow you to save ton of times.



# We should now have a pretty good understanding about working with the regular expresions in Python.
# But we are using this finditer() method throughout this module,
# because it does the best job to find all the matches and showing their locations.
# but there are other methods that we can use for different purpose.
# so, first lets look at the findall() method.
# finditer() return the found matches with extra infos whereas findall() just return the found objects within a list.
pattern = re.compile(r"(Mr|Mrs|Ms)\.?\s[A-Z]\w*")
matches = pattern.findall(text_to_search)
for match in matches:
    print(match)
# we can see that it only prints out the firt group.
# if there are multiple groups then it will return a list of tuples.
# if there are no groups then it will return all of the matches as strings.
# lets change our pattern here.
pattern = re.compile(r"\d{3}.\d{3}.\d{4}")
matches = pattern.findall(text_to_search)
for match in matches:
    print(match)
# so thats another way to print out all of the matches.
# but finditer() method is recommanded for extra functionailies.


# next we have the match() method.
# match() will determine if the regex matches at the beginningof the string.
# lets say we want to search in the sentence variable.
pattern = re.compile(r"Start")
matches = pattern.match(sentence)
# for match in matches:
#     print(match)

# We will get a error because match doesn't return iterable.
print(matches)

# this only matches at the beginning of the string
# if we search for something else that is not in the beginning,
pattern = re.compile(r"and")
matches = pattern.match(sentence)
print(matches)
# then it will give us None.

# if we want to search for matches in the entire string then we can use the search() method.
pattern = re.compile(r"and")
matches = pattern.search(sentence)
print(matches)
# it will print out the first match it finds
# if we search for something that doesn't match then this will return None as well



# the very last thing we will learn is "flags"
# we can use flags to make our life little easier to work with regular expressions.
# for example, we want to match a word.
# but match it whether it was in uppercase or lowercase or mixture of both.
# for example, if we want to match the word "Start" in our sentence
# but each letter can be uppercase or lowercase, then normally we can create a pattern like this,
pattern = re.compile(r"[Ss][Tt][Aa][Rr][Tt]")
matches = pattern.search(sentence)
print(matches)
# but this is kind of pain, instead we can just search for the lowercase
# and then we can add a flag to our pattern here.
# for this we need to pass an arguement of IGNORECASE attribute
pattern = re.compile(r"start", re.IGNORECASE)
matches = pattern.search(sentence)
print(matches)
# we can see that works
# there is short form of this flags as well, we can write I instead of IGNORECASE
pattern = re.compile(r"start", re.I)
matches = pattern.search(sentence)
print(matches)

# there are several different flags but we wont go over them all.
# there is a MULTILINE (M) flag which allow us to use the ^ and the $ 
# to match the beginning and the ending of each line of a multilne string 
# rather than the beginning and ending of a string

# there is a VERBOSE (V) flag that allow us to add comments and whitespaces within our patterns
# which help us to break the complicated patterns into easy-to-understand segments.

# there are lots of advanced features that we can go with regular expressions in Python.
# we will learn that later.

# But hopefully, we are now prett comfortable to read and write regular expressions.
