import phonenumbers as pn
from phonenumbers import geocoder as gc
from phonenumbers import carrier as cr
from phonenumbers import timezone as tz
import mysql.connector



def database(number, host, user, passwd):
    conn_obj = mysql.connector.connect(host=host, user=user, passwd=passwd)
    cur_obj = conn_obj.cursor()
    number = pn.parse(phoneNo)
    regionOfPn = gc.description_for_number(number, 'en')
    carrierPn = cr.name_for_number(number, 'en')
    timezoneGeoOfPn = tz.time_zones_for_geographical_number(number)
    timezoneOfPn = tz.time_zones_for_number(number)
    try:
        cur_obj.execute("Create Database Python_PhoneNumber_DB")
        cur_obj.execute("create table PhoneNumbers(phone_no varchar(30) not null, region varchar(30), operator varchar(50), geo varchar(50), timezone varchar(30))")
        # for phoneNo in parsing(phoneNo):
        sqlInfo = "insert into PhoneNumbers(phone_no, region, operator, geo, timezone)values(%s, %s, %s, %s)"
        val = (regionOfPn, carrierPn, timezoneGeoOfPn, timezoneOfPn)
        cur_obj.execute(sqlInfo, val)
        print("Phone number inserted successfully.")
    except:
        conn_obj.rollback()
    for x in cur_obj:
        print(x)
    conn_obj.commit()
    conn_obj.close()
    
    return database

phoneNo = input("Type in your phone Number: ")
# regionOfPn, carrierPn, timezoneGeoOfPn, timezoneOfPn = parsing(phoneNo)
# database(regionOfPn, carrierPn, timezoneGeoOfPn, timezoneOfPn)
database(phoneNo, 'localhost', 'root', 'admin123')