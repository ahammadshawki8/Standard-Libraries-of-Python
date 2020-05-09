# csv module

# in this module, we will learn how to read, parse and write csv files in python.
# csv stands for character(comma) sparated values.
# basically, csv files allows us to put into a plain text file some data
# and use some type of delimiter usually a comma to separate the different fields.

# we have a csv file here. we can see that the first line of our csv file is the field names.
# after the first line we have some comma-separated values and the character which separates the value is the delimeter.
# comma is a common delimeter.
# but we can use any characters. we can even use tabs, dashes(_), semicolon(;) etc.

# now lets read, write and parse to csv files.

# first we need to import csv module.
import csv

# we might first think of using string split method on each line of the csv file to parse out the data.
# we could do that.
# but csv module makes parsing very easy.
# for example, if ssomeone puts a comma or something in their name then we dont want to split on that.
# and csv module also handle new linea and all those things.

# reading csv file.
# first we need to open the file just like any other file.
# so we will use a context manager.
with open("4. Standerd Libraries\\bd_modified.csv","r") as data:
    my_reader = csv.reader(data) # we can read the data by reader() method.
# in the background, the reader() method is using a dialect that has some preset parameters for what it expects the format of our csv file to be.
# so by default, it is expecting values to be separated by comma and few other things.
# as our csv file is simple so we dont need to pass any additional arguement now.

# the my_reader variable that we created is something that we need to iterate over several times.
# if we print the my_reader,
print(my_reader)
# we can see that it gives us a csv.reader object in memory.
# <_csv.reader object at 0x000001803842B580>

# so instead of printing the object directly, we need to iterate over all these lines in the reader.
with open("4. Standerd Libraries\\bd_modified.csv","r") as data:
    my_reader = csv.reader(data)
    
    for line in my_reader:
        print(line)
    # each line we are printing is a list of values.
    # our firstline is the field names.

# we can also print by specific values by index.
with open("4. Standerd Libraries\\bd_modified.csv","r") as data:
    my_reader = csv.reader(data)
    
    for line in my_reader:
        print(line[2])

# if we dont want the first line of the field name and only prints the values, then we can skip the field name.
# we can use next() method. it will skip one line each time of the execution and it will remember it current state.
with open("4. Standerd Libraries\\bd_modified.csv","r") as data:
    my_reader = csv.reader(data)
    
    next(my_reader) # it will skip oneline.

    for line in my_reader:
        print(line[2])


# Write to a csv file.
# we can do that any list of values.
# but since we already have a list of values in our csv file, lets go ahead and use those.

# lets say we want to save the same values into a csv file but use dashes instead of commas for the delimiter.
# first we need to write the field name headers into the new csv file.
with open("4. Standerd Libraries\\bd_modified.csv","r") as data:
    my_reader = csv.reader(data)

    # opening a new file for writing
    with open("4. Standerd Libraries\\new_bangladesh.csv","w") as wfile:
        # to write to this file we are going to use writer() method.
        my_writer=csv.writer(wfile, delimiter="-")
        # we need to pass in delimiter arguement to change the default delimeter.
        
        for line in my_reader:
            # we can write rows by writerow() function.
            my_writer.writerow(line)
# now if we run that, we can see that we have our new csv file which is separated by dash(-)
# if any vaues of the rows contains dash(-), then csv.writer() automaticaly put a quote outside of that value 
# so that when we read the value we can understand it is a whole value, not separated by dash(-).

# now lets use tabs as delimeters.
with open("4. Standerd Libraries\\bd_modified.csv", "r") as rfile:
    reader=csv.reader(rfile)
    with open("4. Standerd Libraries\\new_bangaldesh tab.csv","w") as wfile:
        writer=csv.writer(wfile,delimiter="\t")
        for line in reader:
            writer.writerow(line) 

# if we want to read in that tab delimetered file we can add the delimiter arguement into our reader() as well.
# if we try to read a csv file with the wrong delimeter, then it wont split teh rows because it was expecting commas.
with open("4. Standerd Libraries\\new_bangaldesh tab.csv", "r") as rfile:
    reader=csv.reader(rfile, delimiter="\t")

    for line in reader:
        print(line)


# the way we are working with the csv file using reader() and writer() method is probably the common way to work with the csv data
# since they are the first thing that comes up in python docs.
# but we can also work with csv data using DictReader() and DictWriter() method.

# first lets take a look at the DictReader()
with open("4. Standerd Libraries\\bd_modified.csv","r") as data:
    my_reader = csv.DictReader(data)

    for line in my_reader:
        print(line)

# at first glance it might look little complicated.
# each of the values is now an ordered dictionary.
# and at the top, we can see that the first line no loger contains the field name.
# it starts of immidiately with the first person.
# now, field names are the keys of each of this values.
# this is recommanded because it is lot easier to parse out the information that we want.
# for example,
# we have used index for print out the values of hobbyiest field.
# so anyone who read to our code dont know suddenly what the index in refers too. so they have to go to the file and check for the index manually.
# but now we have the fields as the dictionary keys, we can use them to get the values of "Hobbyiest" field
with open("4. Standerd Libraries\\bd_modified.csv","r") as data:
    my_reader = csv.DictReader(data)

    for line in my_reader:
        print(line["Hobbyist"])


# now lets look how to use the DictWriter() method.
with open("4. Standerd Libraries\\bd_modified.csv", "r") as rfile:
    reader=csv.DictReader(rfile)

    with open("4. Standerd Libraries\\new_bangaldesh dict tab.csv","w") as wfile:
        # creating a fieldname list
        field= ['Respondent', 'MainBranch', 'Hobbyist', 'OpenSourcer', 'OpenSource', 'Employment', 'Country', 'Student', 'EdLevel', 'UndergradMajor',
                'EduOther', 'OrgSize', 'DevType', 'YearsCode', 'Age1stCode', 'YearsCodePro', 'CareerSat', 'JobSat', 'MgrIdiot', 'MgrMoney', 'MgrWant',
                'JobSeek', 'LastHireDate', 'LastInt', 'FizzBuzz', 'JobFactors', 'ResumeUpdate', 'CurrencySymbol', 'CurrencyDesc', 'CompTotal', 'CompFreq',
                'ConvertedComp', 'WorkWeekHrs', 'WorkPlan', 'WorkChallenge', 'WorkRemote', 'WorkLoc', 'ImpSyn', 'CodeRev', 'CodeRevHrs', 'UnitTests', 
                'PurchaseHow', 'PurchaseWhat', 'LanguageWorkedWith', 'LanguageDesireNextYear', 'DatabaseWorkedWith', 'DatabaseDesireNextYear', 
                'PlatformWorkedWith', 'PlatformDesireNextYear', 'WebFrameWorkedWith', 'WebFrameDesireNextYear', 'MiscTechWorkedWith', 'MiscTechDesireNextYear', 
                'DevEnviron', 'OpSys', 'Containers', 'BlockchainOrg', 'BlockchainIs', 'BetterLife', 'ITperson', 'OffOn', 'SocialMedia', 'Extraversion', 
                'ScreenName', 'SOVisit1st', 'SOVisitFreq', 'SOVisitTo', 'SOFindAnswer', 'SOTimeSaved', 'SOHowMuchTime', 'SOAccount', 'SOPartFreq', 'SOJobs', 
                'EntTeams', 'SOComm', 'WelcomeChange', 'SONewContent', 'Age', 'Gender', 'Trans', 'Sexuality', 'Ethnicity', 'Dependents', 'SurveyLength', 'SurveyEase']

        writer=csv.DictWriter(wfile,fieldnames=field, delimiter="\t")
        # here we have to pass another arguement which is fieldnames.

        # writing the header
        writer.writeheader()

        for line in reader:
            writer.writerow(line) 

# with DictReader() we didn't need to change anything.
# but with DictWriter() we need to provide the field names of our file.
# in DictWriter() we have the option whether or not to write the fieldnames as headers.
# if we want to write the header then we can use the writeheader() method.

# if we run this we can see that it works.

# DictReader() and DictWriter() is more obious way for working with csv files.
# for example if we dont want Hobbyiest in our new csv file which we created by DictWriter(),
# in regular reader() and writer() we would be modified those indexes.
# but in the DictWriter we can remove hobbyist from our field list.
# before we write each line in our loop we can just remove the hobbyist key and value by del keyword.
with open("4. Standerd Libraries\\bd_modified.csv", "r") as rfile:
    reader=csv.DictReader(rfile)

    with open("4. Standerd Libraries\\new_bangaldesh dict tab 2.csv","w") as wfile:

        field= ['Respondent', 'MainBranch', 'OpenSourcer', 'OpenSource', 'Employment', 'Country', 'Student', 'EdLevel', 'UndergradMajor',
                'EduOther', 'OrgSize', 'DevType', 'YearsCode', 'Age1stCode', 'YearsCodePro', 'CareerSat', 'JobSat', 'MgrIdiot', 'MgrMoney', 'MgrWant',
                'JobSeek', 'LastHireDate', 'LastInt', 'FizzBuzz', 'JobFactors', 'ResumeUpdate', 'CurrencySymbol', 'CurrencyDesc', 'CompTotal', 'CompFreq',
                'ConvertedComp', 'WorkWeekHrs', 'WorkPlan', 'WorkChallenge', 'WorkRemote', 'WorkLoc', 'ImpSyn', 'CodeRev', 'CodeRevHrs', 'UnitTests', 
                'PurchaseHow', 'PurchaseWhat', 'LanguageWorkedWith', 'LanguageDesireNextYear', 'DatabaseWorkedWith', 'DatabaseDesireNextYear', 
                'PlatformWorkedWith', 'PlatformDesireNextYear', 'WebFrameWorkedWith', 'WebFrameDesireNextYear', 'MiscTechWorkedWith', 'MiscTechDesireNextYear', 
                'DevEnviron', 'OpSys', 'Containers', 'BlockchainOrg', 'BlockchainIs', 'BetterLife', 'ITperson', 'OffOn', 'SocialMedia', 'Extraversion', 
                'ScreenName', 'SOVisit1st', 'SOVisitFreq', 'SOVisitTo', 'SOFindAnswer', 'SOTimeSaved', 'SOHowMuchTime', 'SOAccount', 'SOPartFreq', 'SOJobs', 
                'EntTeams', 'SOComm', 'WelcomeChange', 'SONewContent', 'Age', 'Gender', 'Trans', 'Sexuality', 'Ethnicity', 'Dependents', 'SurveyLength', 'SurveyEase']


        writer=csv.DictWriter(wfile,fieldnames=field, delimiter="\t")
        
        writer.writeheader()

        for line in reader:
            # deleting hobbyist key's values.
            del line["Hobbyist"]
            writer.writerow(line) 

# now if we run it, we can see that we dont have hobbyist.

# there are several ways that we could have written these rows.
# we could have deleted the hobbyist key first just like we do here.
# or we could have created a new dictionary without having the hobbyist key, and pass that into the writerow() method.


# now we have a good idea of working with csv files.
# we have some other functions in csv module. lets see all of them
print(dir(csv))

# we can see we have
['Dialect', 'DictReader', 'DictWriter', 'Error', 'QUOTE_ALL', 'QUOTE_MINIMAL', 
'QUOTE_NONE', 'QUOTE_NONNUMERIC', 'Sniffer', 'StringIO', '_Dialect', '__all__',
'__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
'__package__', '__spec__', '__version__', 'excel', 'excel_tab', 'field_size_limit',
'get_dialect', 'list_dialects', 're', 'reader', 'register_dialect', 'unix_dialect',
'unregister_dialect', 'writer']
