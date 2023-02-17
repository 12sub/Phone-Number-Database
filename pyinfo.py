import phonenumbers as pn
from phonenumbers import geocoder as gc
from phonenumbers import carrier as cr
from phonenumbers import timezone as tz

# parsing phonenumbers
def parsing(phoneNo):
    number = pn.parse(phoneNo)
    regionOfPn = gc.description_for_number(number, 'en')
    carrierPn = cr.name_for_number(number, 'en')
    timezoneGeoOfPn = tz.time_zones_for_geographical_number(number)
    timezoneOfPn = tz.time_zones_for_number(number)
    print("The region of the given phone number is:", regionOfPn)
    print("The SIM Card operator or carrier of the given phone number is:", carrierPn)
    print("The timezone goegraphical of the given phone number is:", timezoneGeoOfPn)
    print("The timezone of the given phone number is:", timezoneOfPn)
    
    return parsing

#This will not store your code in a database but it will print it out on your teminal
parse = input("Type in your phone number:")
phoneInfo = parsing(parse)
print(phoneInfo)