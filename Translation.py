
#Programme to tranlate abbreviation
#limited to one abbreviation. Will improve upon it


#user input 
text=input("Please enter abbreviation: ")
print (text)

#getting a list of all the words in the text

wordList=text.split()
print(wordList)

#search translation file
 
filename="Translation.txt"
READ="r"

print("\n")
with open (filename,mode=READ) as file:
    readFile=file.read()
    print(readFile)

    with open (filename) as file:
        line=file.readline()
        print(line)

    lineList=line.split()
    print(lineList)
 
#check if word in text file exists in translation text
if wordList[0] in lineList:
      print(f"{text} was found in the translation file ")
      print(f"{text} ")
else:
      print("Word not found")

#remove the first and second elements

del lineList[0]
del lineList[0]
joinedString=(" ".join(lineList))   #now we can join the elememts in the list

#Translating abbreviation

translation= text + " - " + joinedString
print(translation)

