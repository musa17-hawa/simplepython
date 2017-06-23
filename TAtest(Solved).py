#The code was written in python3 format

def count_characters(s):
    s = ''.join(s.split())
    s = s.lower()
    string_dict = {}
    L = list(s)
    for char in L:
        if char in string_dict:
            string_dict[char] += 1
        else:
            string_dict[char] = 1
    return string_dict
print(count_characters("test test TEST TEST this IS a TeSt"))

    '''
    INPUT: STRING
    OUTPUT: DICT (STRING => INT)

    Return a dictionary which contains a count of the number of times each
    character appears in the string.
    Characters which would have a count of 0 should not need to be included in
    your dictionary.
    '''
#-----------------------------------------------------------------------------

# first I splited the sentence into words in a list and then joind them all using the ''.join method
# then i lowercase the characters in order to count them the right way because computers
# will treat ("A") different than ("a"), then i listed the characters by using the command
# list() the a typical for loop in order to start counting the letters so inside the for loop
# there is an if statment which basically checks iff the character in the string dictionary
# "the output" so that if it is already there it would add 1 to the current counter, if not,
# it would just start the counter from the beginning with the value of 1, and the end of
# the function we need something to show us what we have done, and thats the print function.


#_____________________________________________________________________________

def invert_dictionary(d):
	result = {}
	for k, v in d.items():
		result.setdefault(v, []).append(k)
	print(result)
invert_dictionary({'a': 2, 'b': 4, 'c': 2})

    '''
    INPUT: DICT (STRING => INT)
    OUTPUT: DICT (INT => SET OF STRINGS)

    Given a dictionary d, return a new dictionary with d's values as keys and
    the value for a given key being the set of d's keys which have the same
    value.
    e.g. {'a': 2, 'b': 4, 'c': 2} => {2: ['a', 'c'], 4: ['b']}
    '''
#-----------------------------------------------------------------------------

# here i started with an empty dictionary as an output, and i can add things up to it afterwords
# to fill it up with what is needed, os here the main loop is a basic for loop which is for the key
# and value in the input dictionary and then inside that main for loop we start add things up to the
# empty dictionary which we started with and we are forming a default kind of view which is inside
# a dictionary that contains the value of the key and an empty list which we are adding the keys using
# append(k) function, after that we print the output dictionary which is "result" in order to see the
# output.

#_____________________________________________________________________________


def word_count(filename):
    num_lines = 0
    num_words = 0
    num_chars = 0
    with open(filename,"r") as file:
        for line in file:
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(line)
        final = (num_lines, num_words, num_chars)
        print(final)
word_count("filename.txt")
    '''
    INPUT: STRING
    OUTPUT: (INT, INT, INT)

    filename refers to a text file.
    Return a tuple containing these stats for the file in this order:
      1. number of lines
      2. number of words (broken by wordshitespace)
      3. number of characters

    '''
#-----------------------------------------------------------------------------

# We start with 3 simple counters one for each the lines and words and characters, then we open a file
# with read permission because we are only going to read things and not write anything and this file
# was opened with the name "file" so we can call it later for different purposes, then we do a for loop
# with the number of lines in the file we opened, after that we split the line into a list of words using the .split()
# function and then we add on the counters we made above, for the lines we just add 1 each new line,
# and for the words counter we add the lengh of the line, words are separated with spaces, and for the
# character counter we add up the lengh of the whole line which is basically how many characters you have
# in that line and finally we make a simple tuple which will output the three integers in order.

#_____________________________________________________________________________

def most_common_letters(sentence):
    from collections import Counter
    result = []
    sentence = sentence.lower()
    wl = sentence.split() #wl = world list
    i = 0
    for words in wl:
        nwl = Counter(wl[i]).most_common(1) # nwl = new world list
        i+=1
        result.append(nwl[0][0])
    print(result)#printing the information as a list
    print(' '.join(result)) #print out the information as a normal string
most_common_letters("Hello and WwWelcome, everybodyyy.")



    """
    INPUT: string
    OUTPUT: list of strings

    Given a sentence, give the most common letter for each word.
    You should lowercase the letters. If there's a tie, include any of them.

    example:
    INPUT: "Welcome to Zipfian Academy!"
    OUTPUT: 'e t i a'

    Hint: use Counter and the string join method
    (It is possible to do this in one line, but you might lose some
    readability)
    """
 #-----------------------------------------------------------------------------

# so here we are using a new modual whcih is called collections but we are using a small corner of it
# which is Counter, we started off with simple empty list as we did before and we will add things up to
# it in the future then we lowercase the sentence that we want to work on and we put the words of the
# sentence into a list using the .split() function and we make a little counter to help us, we started
# with the value of 0 and then a for loop using the number of words in the wordlist and we make a new
# wordlist which will contain the most common letter for each word, so we take each word from the worldlist
# and see what is the most common letter in that word and we carry on to the next word, and after we know
# what is the most common letter for that word we add it to the result list which contains the most common letters
# for each word separated and because the most_common function gives us also how many times that character showed up
# in the word, for us we dont need this kind of information so we only take the first thing the function gives us 
# which is the letter that we need, and we do that by result.append(nwl[0][0]), then we have two option, we either
# print out the information in a list or as a normal string.

 #_____________________________________________________________________________


def write_to_file(lst, f):
	file = open(f,"w")
	n = 1
	for char in lst:
		file.write(str(n) + " " + char + "\n")
		n+=1
	file.close()
write_to_file(["a", "b", "c", "d"],"file.txt")
    """
    INPUT: list, open file object
    OUTPUT: None

    Write the list to the file with line numbers, starting at 1.
    INPUT: ["a", "b", "c"]
    FILE CONTENTS:
    1 a
    2 b
    3 c

    Hint: Use enumerate for cleaner code
    """
#-----------------------------------------------------------------------------

# first of all we have to open the file with the "write" permission so that we can write to the file, then
# a little counter to have the numbers with each line ready, then a for loop with the number of characters
# in the list we write first of all the number and then a space between and after that the char in the list
# and then a new line "\n" and of course we need to close the file we opend.

#_____________________________________________________________________________


def merge_files(f1, f2, out):
    with open(f1) as f1:#the first input file
        with open(f2) as f2:#the second input file
            with open(out,"w") as of: #output file
                lines1 = f1.readlines() #reads the first file's lines
                lines2 = f2.readlines() #reads the second file's lines
                for i in range(len(lines1)):
                    newline = lines1[i].strip() + ',' + lines2[i]
                    of.write(newline)
merge_files("file1.txt","file2.txt","outfile.txt")


    """
    INPUT: open file, open file, open file
    OUTPUT: None

    f1 and f2 are two files with the same number of lines. Merge the contents
    together, separated with a comma.

    INPUT FILES:
    cat
    dog

    mouse
    rabbit

    OUTPUT FILE:
    cat,mouse
    dog,rabbit

    Hint: Use izip
    """
#-----------------------------------------------------------------------------

# first we open 3 files to wrok on, (two input and one output), we need "write" permission in the last file
# (the output file) so that we can write things to it, after that we read the first file's' line by the command
# .readlines() and do the same for the 2nd file then we do a for loop for how many lines we have in any of the files
# since both files have the same amount of lines and the newline in the output would be the first file's' line
# pluse the 2nd file's' line and a comma in between, the .readlines() reads the lines and put the in list, and that
# is why we used "lines1[i]" format, lastly we write the newline we made into the output file.

#_____________________________________________________________________________


def key_in_value(d):

    result = []
    for k, v in d.items():
        if k in v:
            result.append(k)
    print(result)

key_in_value({"a": ["b", "c", "a"], "b": ["a", "c"], "c": ["c"], "d": ["a", "d"]})

    """
    INPUT: dict
    OUTPUT: list

    Return the keys from the dictionary where the key is a member in the 
    associated value.

    example:
    INPUT: {"a": ["b", "c", "a"], "b": ["a", "c"], "c": ["c"]}
    OUTPUT: ["a", "c"]

    Hint: Use iteritems
    (Can be done on one line with a list comprehension)
    """

#-----------------------------------------------------------------------------

# we start off with an empty list so that we can add things up to it in the future, then a for loop for how
# many items in the "d" dictionary and we use the key and the value as variables to use, the key in the
# d dictionary is the letter that is first in the dictionary, for example in this ({"b": ["a", "c"]}) the key
# is the letter "b" and the valuse of this key are "a" and "c", so after the loop we simpley check if the key
# is in the valuses of the key or not, if yes then we add the key to our empty list, if not, nth happends,
# and of course we print out the result which is the list we created.

#_____________________________________________________________________________



def merge_dictionaries(d1, d2):
    result = {k : (d1.get(k, 0) + d2.get(k,0)) for k in set(d1.keys()) | set(d2.keys())}
    print (result)
merge_dictionaries({"a": 2, "b": 5, "c": 2}, {"a": 7, "c":10})

    """
    INPUT: dict (string => int), dict (string => int)
    OUTPUT: dict (string => int)

    example:
    INPUT: {"a": 2, "b": 5}, {"a": 7, "c":10}
    OUTPUT: {"a": 9, "b": 5, "c": 10}

    Create a new dictionary that contains all the key, value pairs from d1 and
    d2. If a key is in both dictionaries, sum the values.
    """
#-----------------------------------------------------------------------------

# here we made like a formate for what the result would look like based one the inputs, so here the result
# would first of all be a dictionary which has keys and valuse of course, and the common key will be the
# first thing in the dictionaryand after the common key we get the value after the key, by using .get(k, 0)
# command and the new list will be adding the comman key with its value in the first dictionary with the common
# key in the second dictionary and its gonna do that for number of how many keys we have, the set() command
# basically deletes what is written more than one time in a list, for example, l = [1, 1, 2, 3] so set(l)
# would look like [1,2,3], and after all that we print out the result.

#_____________________________________________________________________________