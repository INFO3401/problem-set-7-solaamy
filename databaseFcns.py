#Kexin Zhai INFO 3401
# Place any necessary imports here
import sqlite3
import csv
####################################################
# Part 0
####################################################

# Move your parsers.py file to your Problem Set 7
# directory. Once you've done so, you can use the 
# following code to have access to all of your parsing
# functions. You can access these functions using the 
# parsers.<function name> notation as in: 
# parsers.countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Bush_1989.txt')
import parsers
####################################################
# Part 1
####################################################

def populateDatabase(databaseName, wordCounts, metaData):
    # Write a function that will populate your database
    # with the contents of the word counts and us_presidents.csv
    # to your database. 
    # Inputs: A string containing the filepath to your database,
    #         A word count dictionary containing wordcounts for 
    #         each file in a directory,
    #         A metadata file containing a dictionary of data
    #         extracted from a supplemental file
    # Outputs: None
    conn = sqlite3.connect(databaseName)

    c = conn.cursor()

    add_president = ''' INSERT INTO president_info(number, start_date, end_date, president_name, prior_position, party, vice_president) values (?, ?, ?, ?, ?, ?, ?) '''
    add_wordCounts = ''' INSERT INTO wordCounts_info(filename, words, counts) values (?, ?, ?) '''
    
    for value in metaData:
        c.execute(add_president, (value['number'], value['start'],value['end'], value['president'], value['prior'], value['party'],value['vice'] ))
    for key, value in wordCounts.items():
        for inkey, invalue in value.items():
            c.execute(add_wordCounts, (key, inkey, invalue))
    conn.commit()

    conn.close()
    
    return 0

# Test your code here
#words_Counts = parsers.countWordsMany("./state-of-the-union-corpus-1989-2017")
#parsers.createDatabase('presidents.db')
#with open('./us_presidents.csv', encoding="utf8", errors='ignore') as csv_file:
#    reader = [{k: v for k, v in row.items()} for row in csv.DictReader(csv_file, skipinitialspace=True)]
#populateDatabase('presidents.db', words_Counts, reader)
####################################################
# Part 2
####################################################
#
def searchDatabase(databaseName, word): 
    # Write a function that will query the database to find the 
    # president whose speech had the largest count of a specified word.
    # Inputs: A database file to search and a word to search for
    # Outputs: The name of the president whose speech contained 
    #          the highest count of the target word
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute("SELECT filename FROM wordCounts_info WHERE words=? ORDER BY counts DESC", (word,))
    file_name = c.fetchone()
    presidentName = str(file_name).split("_")
    name = presidentName[0]
    name = name[2:]     
    return name

#presi_name = searchDatabase('presidents.db', "than")
#print(presi_name)

def computeLengthByParty(databaseName): 
    # Write a function that will query the database to find the 
    # average length (number of words) of a speech by presidents
    # of the two major political parties.
    # Inputs: A database file to search and a word to search for
    # Outputs: The average speech length for presidents of each 
    #          of the two major political parties.
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute("SELECT filename, SUM(counts) FROM wordCounts_info GROUP BY filename")
    sum_fileWCounts = c.fetchall()
    print(sum_fileWCounts)
    ######
    #Not finish, stuck here
    #I guess we might need to create a third table in database including presidents name, filename of the speech, party then use left join method to combine the tables?????
    #Tricky >^<
    ######
    
    #return 0
computeLengthByParty('presidents.db')