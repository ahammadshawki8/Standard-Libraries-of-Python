# In this module, we will learn how to work with dates in Python.
# It is extreamly important to know how to work with dates,
# because we are going to using this in almost every type of application we are going to write in future.

# and dates can sometime become overwhelming because there are lots of things to think about.
# for example, in Python we have dates, times, datetimes, timezones, timedeltas.
# and its not really obius when we should use what.
# so, lets go ahead and looks some examples of this to become comfortable.

# the main module we need to import when we are working with dates is te datetime module.
import datetime

# the first thing to talk about date, times and datetimes is understanding the difference between naive and aware datetimes.
# and we will hear this two terms a lot.

# naive dates and times dont have enough information to determine things like timezones or daylight saving times.
# but they are easier to work with if we dont need that level of details.

# but if we do need that level of details to avoid confussion, then we need to use aware dates and times.
# these do have enough information to determine their timezones and keep track of daylight savings times.

# since naive datetimes are easier to work with we first start by learning those.

# a normal date we will work with year,month and date. there are couple of different ways we can create dates.
# we can use datetime.date() function to create a date.
d = datetime.date(2004, 12, 28)
# we have to pass in year, month and day.
print(d)
# when we rae creating this dates we need to pass regular integers with no leading zeros (not 07, use 7)
# this will give us a syntax error.

# if we want todays date then we can use datetime.date.today() method
tday = datetime.date.today()
print(tday) 

# we also have more attributes and methods to grab some additional informations from our date.
# we can grab just the year, moth or day by
print(tday.year)
print(tday.month)
print(tday.day)
# we can also grab the day of the week and there are 2 different ways to do that.
# we can use both weekday() and isoweekday() method.
print(tday.weekday())
print(tday.isoweekday())
# the only difference is for weekday(): Monday=0 and Sunday=6
# for isoweekday(): Monday=1 and Sunday=7


# Now lets look at timedeltas
# timedeltas are simply the difference between two dates and times.
# and they are extreamly useful when we want to do operations in our days and times.

# for example, let us create a timedelta which will be one week away
tdelta = datetime.timedelta(days=7)
# now that we have this timedelta of 7 days we can use this to do some calculations.
# lets say we want toi print out what the date will be one week from now.
# we can just add up tday and tdelta
print(tday + tdelta)
# we can also substrac timedeltas
print(tday - tdelta)

# if we add/sub a timedelta with a date we get another date.
# but if we instead add/sub a date from a date then we will geta timedelta as the result.
# date2 = date1 + timedelta
# timedelta = date1 - date2

# lets see how many days are there till my next birthday
bday = datetime.date(2020, 12, 28)
till_bday = bday - tday
print(till_bday)
# if we want to get just days then we can use the days attribute of timedelta.
print(till_bday.days)
# we can also see total seconds by total_seconds() method.
print(till_bday.total_seconds())



# Now that we have looked datetime.date() now lets look at datetime.time()

# when we are working with datetime.date() we was working with year, month and day.
# now in datetime.time() we will work with hours, minutes, seconds and microseconds.
# by default it doesn't have any time zone information, so it is still naive.
# we can add timezone information using tz_info if we like.
t = datetime.time(9, 30, 45, 200000)
# here we have to pass hours, minutes, seconds and microseconds
print(t)

# just like the dates we can access this attributes individually
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

# but we will hardly going to need datetime.time()
# because when we are going to need time we also going to need date with that,
# thats where datetime.datetime() comes in.

# datetime.datetime() will give us access to everything (year, month, day, hour, minute, second, msecond)
dt = datetime.datetime(2020, 5, 20, 12, 30, 44, 333333)
print(dt)
# datetimes are great because we have access to anything we need.
# we can grab the date without the time by date() method.
print(dt.date())
# we can also only grab the time with time() method
print(dt.time())

# we can still grab each and every attributes like we did before.
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.weekday())
print(dt.isoweekday())

print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)

# just like we did with dates, we can add/substrac timedeltas from datetime.
# but now we can also add hours, minutes, seconds, miliseconds and microseconds in the timedelta.
tdelta = datetime.timedelta(days=7, hours=8, minutes=3, seconds=45, milliseconds=43)
print(dt + tdelta)

# We can find more options/code/programme to find out the differences between two dates in "http://dateutil/" library.


# Now lets look at some of the alternative constructures that come with our datetime.
# 3 of those are pretty useful but people get confused them most often.
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

# we can see that top 2 here are pretty simillar.
# the difference between these two is that today() gives us current local time with None timezone.
# now() gives us the option to pass in a timezone, 
# so if we leave the timezone empty then these are simmilar.
# utctime() gives us current utctime but the tz_info is stil set to None.

# Nothing that we have done so far have given us time zone aware datetimes, we have to explicitely set those.
# first we have see how to use timezones. there are lots of different ways we can look at using timezones.
# but we will jump directly and look at how to use pytz.
# pytz is a third party package that we have to install using pip.

# we might be wondering why we are not using standard library to work with timezone.
# but in the official documentation of python, they recommend to use pytz for working with timezones.
# so we need to install pytz
"""pip install pytz"""
# now l;ets import that
import pytz

# pytz official documentation recommend to always use utc for dealing with timezones.
# we can make the datetime timezone aware by adding tzinfo attribute.
dt = datetime.datetime(2016,7,23,11,53,56, tzinfo=pytz.UTC) 
print(dt)
# we can see now we have utc offset.

# now lets get the current utc time that also timezone aware.
# there are 2 ways we can do this.

# we have now() and utcnow()
dt_now = datetime.datetime.now(tz=pytz.UTC)
# we have to add tz arguement here.
print(dt_now)

# utcnow() doesn't have the option of passing timezone.
# but we can replace the default tzinfo by replace() methodafter we assign dt_utcnow.
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)
# we can do this in 2 ways but using now() is recommanded.

# now we have current utc time which is timezone aware.
# lets look at how we can convert this to different timezones.
# if we wanted to convert this utc time to our timezone, we can use astimezone() method
dt_dha = dt_utcnow.astimezone(pytz.timezone("Asia/Dacca"))
# here we have to enter the timezone usinf timezone() method as an arguement.
print(dt_dha)
# to see all timezones we can use all_timezones attribute
#print(pytz.all_timezones)

# what if we have a naive datetime and we want to make that naive datetime time zone aware?
# first we have to take our local datetime using now() which is not time zone aware.
dt_local = datetime.datetime.now()
print(dt_local)
# if we wanted to convert it to another timezone, we can use the previous approach.
dt_east = dt_local.astimezone(pytz.timezone("US/Eastern"))
print(dt_east)
# But sometimes this approach gives ValueError.

# So, we can also do that by this second approach:
# first we need to grab the timezone.
dha_tz = pytz.timezone("Asia/Dacca")
# then we can convert this naive datetime to timezone aware by localize() method.
dt_local = dha_tz.localize(dt_local)
# now we can use astimezone() function.
dt_east = dt_local.astimezone(pytz.timezone("US/Eastern"))
print(dt_east)

# Now we will see couple of different ways to diaplay this datetimes.
dt_now = datetime.datetime.now(tz=pytz.timezone("Asia/Dacca"))
# probably, the best way to save this dates or use them for external use is to save them in iso format.
# we can display this in iso format by isoformat() method.
print(dt_now.isoformat())

# if we want to print this dates out in other specific format then we can go to python documentation 
# and look at the format codes to print this out in just about any way that we want.
# we can format the dates by strftime() method.
print(dt_now.strftime("%B %d, %Y")) # or,
print(datetime.datetime.strftime(dt_now,"%B %d, %Y"))
# In first line we have to write only one argument as we have mention our variable name earliar.
# In second line we have to write two arguments, because here we did not mention our variable name earliar.

# %b is the month abbreviated.
# %B is the full month name.
# %m is month in number.
# %y is two digit year.
# %Y is four digit year.
# %a is the day of the week abbreviated.
# %A is the day of the week.
# %d is the day
# %D is the full date in numbers.

# %H means hours(24 o'clock)
# %I means hours(12 o'clock)
# %p means AM or PM
# %M means minutes
# %S means seconds

# we dont have to memorize this, everytime we may need this we can o to python official documentation.
# FOR MORE OPTIONS VISIT "http://strftime.org/" 

# sometimes we have the opposite, sometimes we have a string and we want to convert them to a datetime.
# then we can use strptime() method.
dt_str = "August 12, 2020"
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
# here we have to pass the string and the format of the string
print(dt)

# So, 
# strftime (str from time) - converts string from a datetime
# strptime (str python time) - coverts python readable dateime from string

# sometimes we have to use different letters, symbles and numbers in our code/dates which is not belongs to English.
# The programmers speak that is named localization.
# it would take more time and code to access those letters or symbles.
# we can find more information in this site-"http://babel.pocoo.org/"

# there is a popular python package called arrow which eases the usage of working with datetime.
# we could learn that later in near future.
# This basics about built-in datetime module will allow us to solve the problems that we come up against.