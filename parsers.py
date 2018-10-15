##Kexin Zhai - INFO 3401
import string
import csv
import json
import pandas
from os import listdir

################################################################################
# PART #1
################################################################################

def countWordsUnstructured(filename):
    # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts
    
    #initialize a word count dictionary
    wordcount = {}
    
    #open the file
    file = open(filename, encoding= "utf-8")    

    #read & split the file
    for word in file.read().split():
        for mark in string.punctuation:
            word=word.replace(mark, "")
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] +=1 
    return wordcount

    
    ##another way to do part 1
    ##initialize a word count dictionary
    #wordCount={}
    
    ##open the file
    #datafile = open(filename).read()
    
    ##Split out into words
    #data = datafile.split()
    
    ##Count the words
    #for word in data:
        #for mark in string.punctuation:
            #word=word.replace(mark, "")
            
        #if word in wordCounts:
#            wordCounts[word] = wordCounts[word] +1
        #else:
#            wordCounts[word] =1
            
    #return wordCounts
    
# Test your part 1 code below.
#bush1989 = countWordsUnstructured("./state-of-the-union-corpus-1989-2017/Bush_1989.txt")
#print(bush1989)
################################################################################
# PART 2
################################################################################
def generateSimpleCSV(targetfile, wordCounts): 
    # This function should transform a dictionary containing word counts to a
    # CSV file. The first row of the CSV should be a header noting: 
    # Word, Count
    # Inputs: A word count list and a name for the target file
    # Outputs: A new CSV file named targetfile containing the wordcount data
    #-------------------------------
    #open the file
    #print the headers
    #iterate through the word counts
        #Add to our csv file
        
    #close file
    #return pointer to the file
    #------------------------------
    with open(targetfile, 'w') as csvFile:
        writer = csv.writer(csvFile, delimiter=",")
        writer.writerow(['Word','Count'])
        for key, value in wordCounts.items():
            writer.writerow([key, value])
    csvFile.close()
    
    return csvFile

    
# Test your part 2 code below
#generateSimpleCSV("test.csv", bush1989)    
################################################################################
# PART 3
################################################################################
def countWordsMany(directory): 
    # This function should create a dictionary of word count dictionaries
    # The dictionary should have one dictionary per file in the directory
    # Each entry in the dictionary should be a word count dictionary
    # Inputs: A directory containing a set of text files
    # Outputs: A dictionary containing a word count dictionary for each
    #          text file in the directory
    
    #-------------------------------
    #open the directory and pull a list of file names
    #create a blank dictionary to hold our data
    #populate the dictionary
    #Loop through the list of files
        #For each file, call countWordsUnstructured to get the word counts for that file
        #Place the word count dictionary into the empty dictionary
    #Return the dictionary   
    #------------------------------
    wordcount = {}
    dir_list = listdir(directory)
    for file in dir_list:
        if file == ".DS_Store":
            continue
        file_wordcount = countWordsUnstructured(directory + "/" + file)
        wordcount[file] = file_wordcount
        
    return wordcount

# Test your part 3 code below
some_dict = countWordsMany("./state-of-the-union-corpus-1989-2017")
#print (some_dict)
################################################################################
# PART 4
################################################################################
def generateDirectoryCSV(wordCounts, targetfile): 
    # This function should create a CSV containing the word counts generated in
    # part 3 with the header: 
    # Filename, Word, Count
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: A CSV file named targetfile containing the word count data
    with open(targetfile, 'w') as csvFile:
        writer = csv.writer(csvFile, delimiter=",")
        writer.writerow(['Filename','Word','Count'])
        for key, value in wordCounts.items():
            for inkey, invalue in value.items():
                writer.writerow([key, inkey, invalue])           
    csvFile.close()
    
    return csvFile
# Test your part 4 code below
#generateDirectoryCSV(some_dict, "targetfile.csv")
#### ############################################################################
# PART 5
################################################################################
def generateJSONFile(wordCounts, targetfile): 
    # This function should create a JSON file containing the word counts generated in
    # part 3. Architect your JSON file such that the hierarchy will allow
    # the user to quickly navigate and compare word counts between files. 
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: An JSON file named targetfile containing the word count data
    with open(targetfile, 'w') as JSONFile:
        #for key, value in wordCounts.items():
            #for inkey, invalue in value.items():
        jsonData = json.dumps(wordCounts)
        JSONFile.write(jsonData)
#        json.dump(jsonData, JSONFile)          
    JSONFile.close()   
    return JSONFile
# Test your part 5 code below
#generateJSONFile(some_dict, "targetfile.json")
################################################################################
# PART 6
################################################################################
def searchCSV(csvfile, word): 
    # This function should search a CSV file from part 4 and find the filename
    # with the largest count of a specified word
    # Inputs: A CSV file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    count = 0
    wordcount = 0
    with open(csvfile) as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        next(data, None)
        for row in data:
            wordcount = float(row[2])
            if row[1] == word and wordcount > count:
                count = wordcount
                filename = row[0]
    csv_file.close()
    return filename
file_name = searchCSV("./targetfile.csv", "than")
#print(file_name)

def searchJSON(JSONfile, word): 
    # This function should search a JSON file from part 5 and find the filename
    # with the largest count of a specified word
    # Inputs: An JSON file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    count = 0
    with open(JSONfile) as json_file:
        datastore = json.load(json_file)
        for key, value in datastore.items():         
            for inkey, invalue in value.items():
                wordcount = int(invalue)
                if inkey == word and wordcount > count:
                    filename_injoson = key
                    count = wordcount
        json_file.close()
        return filename_injoson
# Test your part 6 code to find which file has the highest count of a given word
#searchJSON("./targetfile.json", "than")
file_json = searchJSON("./targetfile.json", "than")
#print(file_json)
# +1 bonus point for figuring out how many datapoints you had to process to 
# compute this value

##############
#Friday problem set
    #problem 2
#Table1 US_presidents.csv
    #date/string    start_date
    #date/string    end_date
    #string         president_name
    #string         prior_position
    #string         party
    #string         vice_president
#Table2 wordcounts.csv
    #string         Words
    #number         Counts
    #string         president_name
    #number         year
#Connect both table based on president_name, for those that match president_name on wordcounts
#table, add words, counts, data. Or only keep president information from table 1 for those name
#that matches president_name on table 2
#
    #Problem 3
import sqlite3

conn = sqlite3.connect('presidents.db')

c = conn.cursor()

c.execute('''CREATE TABLE presidents_data(start_date text, end_date text, president_name text, prior_position text, party text, vice_president text, words text, counts integer, year integer)''')
conn.commit()

conn.close()