# json module

# in this module, we will learn how to work with json data within python.
# json stands for "JavaScript Object Notation"
# it is a very common data format for storing informations.
# it is used most when fetching data from online api's, 
# but it is also used for configuration files and that kind of data which can be saved in our local machine. 

# it is inspired by javascipt, but it is now independent of any one language.
# pretty much every language has library for parsing and generating json data.

# first we need to import the json library
import json
# it is  a standerd library so we dont need to install any package.

# now, we have a multi-line string here that is a valid json.
# and we can see that it is almost look like a python dictionary.
# this json here has a key called people, and the value of people is a list of more objects.
# in this example, we have 2 more dictionary object and each onject has name, phone, emails and has_license key.

prople_string="""
{
    "people": [
        {
            "name":"Ahammad Shawki",
            "phone": "01926821177",
            "emails":["ahammadshawki8@gamil.com","ahammadshawki8@outlook.com"],
            "has_license": true
        },
        {
            "name":"John Doe",
            "phone": "560-555-555",
            "emails": null,
            "has_license": false            
        }
    ]
}
"""

# right now this is just a python string that happens to be a valid json.
# lets see how to load this into a python object so that we can work with the data more easily.

# to load this object from string we can use loads() method. here loads means load string.
data=json.loads(prople_string)
# we want to pass in the string as an arguement.

# now lets print our data.
print(data)
# we can see it prints that out but its not very clean.
# its look like python dictionary. lets check the type.
print(type(data))
# we can see that it is a dictionary.

# python follows the following table while converting json object.
# json          python
# object        dict
# array         list
# string        str
# number(int)   int
# number(real)  float
# true          True
# false         False
# null          None

# since array is converted to a list so the value of people key must be a list.
print(type(data["people"])) 

print("\n\n")
# now that we converted the json to python object it is going to be a lot more easier to work with this.
# we can loop through all of this people and access each one individually.
for person in data["people"]:
    for key,value in person.items():
        print(key,"-->",value)
    print()

# now lets do a reverse formula and dump a python object into a json string.
# to do this we can use the json.dumps() method

# lets say we want to remove the phone number from each person and then convert the data to json
for person in data["people"]:
    del person["phone"]

new_string=json.dumps(data)

print(new_string)
# we can see that we have a new json string that no longer contains the phone numbers.

# since it is a string it would be nice to format this is in a way so that it is easier to read.
# to do this we can pass in a indent arguement to dumps() function
new_string2=json.dumps(data, indent= 2)
# here indent takes the number of indention that we want per item in the string.
print(new_string2) 
# so indent method is really helpful when we are dumping like this.

# another thing that we can do to clean up our jsons when dumping it to a string is to sort the keys.
# we cna do that by passing another arguement sort_keys=True
new_string3=json.dumps(data, indent= 2, sort_keys=True)
print(new_string3)
# now we can see that all of the keys have been sorted alphabetically.

# now, lets see how to load json files into python objects and write those objects back to json files.

# to load json files, we can use the json.load() method.
# NOTE: load() method loads a file to a python object,
# whereas loads() method loads a string.

# to load in this file we need to first open it, we can use context manager.
with open("4. Standerd Libraries\\bd_modified.json","r") as f:
    file_data=json.load(f)

# now we should be able to loop through our data just like before.
for key,value in file_data["MainBranch"].items():
    print(key," --> ",value)

# now lets write this python object to a json file.
# lets remove one of the keys from that data and write that data into a json file.

# lets remove the "Hobbyiest" code.
for key, value in file_data.items():
    if key=="Hobbyist":
        del key

# or , we can do this in this way too.
del file_data["ConvertedComp"]

# to dump the python object into json file we will use the dump() method.
# NOTE: dump() method dumps a python object to a file,
# whereas dumps() method dumps to a json object.

# first we need to open the file that we want write to.
with open("4. Standerd Libraries\\new_bangladesh.json","w") as f: 
    json.dump(file_data,f,indent=2)
    # here we need to add another arguement which is the file name where we want to dump this data to.
    # we can pass in indent method to clean up little bit.


# now lets look at a real world example of using json data.

# its pretty common for websites to return json from their api's because it is easy to parse.
# there is a yahoo api that converts united states dollars to other currency.
# lets pull down that data, convert it to a python object and parse out some information.

# to make a request to web api, we will use the built_in urllib module
# so we are importing urlopen from urllib.request
# we can also use the request library to do this, if we are more comfortable of using that.
import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()
    # here we have passed the url as an arguement of urlopen and read the json file with read() method.

print(source)
# right now, it is going to be a string.
# we can see it not very readable.

# now lets load this json into a python object.

data_yahoo=json.loads(source)
# now its a a python object.  
print(data_yahoo)

# now lets dump it back to a string with the indent arguement passed in.
# so that it clean little bit and we can read it well.
print(json.dumps(data_yahoo, indent=2))
# now we can see we have some cleaned up json here.
# we can see that the first key is list and within list we have meta key which have metadata.
# we can see it says that the count is 188 items.
# and within that dictianary we have resources key and in that resources we have some individual resources about conversion information.

# lets start working with that data.
# first see if the count 188 is correct or not.
# so lets see if there are 188 resources.
print(len(data_yahoo["list"]["resources"]))
# we can see there 188 resources there.

# now lets loop through all of that resources.
for item in data_yahoo["list"]["resources"]:
    print(item)
# we can see each of the items has a resource key and within that key we have classname, fields and within that fields we have the name and price.
# lets say we want to print all the conversions name and prices.
# we can do this by,
for item in data_yahoo["list"]["resources"]:
    name=item["resource"]["feilds"]["name"]
    price=item["resource"]["feilds"]["price"]
    # this look kind of messy but we have to do this lots of time when we are working with real world json data.
    print(name,"-->",price)

# now lets use this conversions rate to convert us dollars to specific currencies.
# we are going to create a new dictionary where all of the names will be keys and all of the prices will be the values.
usd_rate=dict()
for item in data_yahoo["list"]["resources"]:
    name=item["resource"]["feilds"]["name"]
    price=item["resource"]["feilds"]["price"]
    usd_rate[name]=price

# now we can access a specific value just by accessing that key.
print(usd_rate["USD/EUR"])

# now if we want to convert 88 usd to euros then we can,
eur=float(usd_rate["USD/EUR"])
print(50*eur)
# we can also pass in different currencies. lets convert for BDT.
ban=float(usd_rate["USD/BDT"])
print(100*ban)

# we can also create a script which pulls down the corversion info from an api once a day,
# and then save it to a local json file for faster access.
# and then we can create a function that access this json file in a more repeatable way.

# so understanding parsiong and working with json files can be extreamly beneficial for grabbing data from internet and using it to feed our need.
# there are countless json api's in online and it is essential to know how to work with this information if we want to grab data from external sources.
