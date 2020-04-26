import names
import random
import requests

from csv import reader

travelerscript = open("travelerscript.sql", "w")

email_domains = ["gmail", "hotmail", "yahoo", "outlook"]
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
year = range(1965, 1997)


for i in range(250):
    
    id_ = i
    firstName = names.get_first_name()
    lastName = names.get_last_name()
    dob = '{0}-{1}-{2}'.format(random.choice(year), random.choice(month), random.choice(day))

    email = '{0}{1}@{2}.com'.format(firstName.lower(), lastName.lower(), random.choice(email_domains))
    phoneNumber = "({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}".format(random.randint(2,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9))
    #print(id_, firstName, lastName, email, dob, phoneNumber)
    #print(f"INSERT INTO TRAVELERS VALUES ({id_}, '{firstName}', '{lastName}', '{dob}', '{email}', '{phoneNumber}');")
    travelerscript.write(f"INSERT INTO TRAVELERS VALUES ({id_}, '{firstName}', '{lastName}', '{dob}', '{email}', '{phoneNumber}'); \n")