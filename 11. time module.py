# time module

# time module is an important module in python.
# we not only have to use it in our time related program, 
# but also have to work with it in our every project to make our code efficient and user-friendly.
 
# first lets import time module.
import time

# lets see what methods and attributes we have.
print(dir(time))

['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__',
 'altzone', 'asctime', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 
 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 
 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 
 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname']

# we can convert a time tuple to a string by asctime() method.
print(time.asctime())
# we have to pass the time tuple here, if we dont pass anything, then it will give us the localtime().

# we can converts seconds to a string by ctime() method.
print(time.ctime(1509006150.0319273))

# we can convert the seconds in this format by gmtime().
    # (tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)
print(time.gmtime(1509006150.0319273))

# we can print the local time using localtime() method.
print(time.localtime(1509006150.0319273))
# it is almost same as gmtime(), but instead of giving us the gmt time it gives us the local time (gmt + 6)
# we can see the difference in tm_hour.

# we can do the reverse thing using mktime()
print(time.mktime(time.localtime(1509006150.0319273)))
# we have to pass here struct_time object or time tuple, then it will give us the seconds in "local time"(NOTE)
# it wont give 1000000000, for below code
print(time.mktime(time.gmtime(1000000000))) # it will change for every time zone.

# we can make a monotonic clock using monotonic() method. a monotonic clock cannot go backward.
print(time.monotonic())
# we can make a monotonic clock which calculates in nano seconds using monotonic_ns() method
print(time.monotonic_ns())

# we can make a Performance counter for benchmarking by perf_counter() method.
print(time.perf_counter())
# we can also use perf_counter_ns() 
print(time.perf_counter_ns())

# we can Process time for profiling: sum of the kernel and user-space CPU time by process_time() method.
print(time.process_time())
print(time.process_time_ns())

# Thread time for profiling: sum of the kernel and user-space CPU time by thread_time() method.
print(time.thread_time())
print(time.thread_time_ns())

# we can sleep the kernal and Delay execution for a given number of seconds by sleep() method.
print(time.sleep(1.3))

# we can calculate the current time by time() method.
print(time.time())
# we can get the current time in nano seconds by time_ns() method.
print(time.time_ns())

# we can Convert a time tuple to a string according to a format specification by strftime() method.
import datetime
a=datetime.datetime.now()
print(a.strftime("weekday => %a,\nmonth => %b,\ndate => %d,\ntime => %H:%M:%S,\nyear => %Y"))

# we can Parse a string to a time tuple according to a format specification
print(time.strptime("Thu Oct 26 14:22:30 2017","%a %b %d %H:%M:%S %Y"))

# we can create a struc time object by passing the structime sequence as a list.
print(time.struct_time([2017,10,26,14,22,30,3,299,-1]))

# we can get the time zone by time_zone attribute.
print(time.timezone)

# we can print the time zone name by tzname attribute.
print(time.tzname)

# we can print the daylight time by daylight attribute.
print(time.daylight)

# we can print the altzone by altzone attribute.
print(time.altzone)


# we can see the real world example of time module in python documentation.
"""https://www.python.org/"""