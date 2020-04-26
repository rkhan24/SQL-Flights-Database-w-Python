import names
import random
import requests
from bs4 import BeautifulSoup

from csv import reader

pilotsscript = open("pilots_script.sql", "w")

month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
year = range(1965, 1997)
salary = range(50000, 100000)



for i in range(250):
    
    id_ = i
    firstName = names.get_first_name()
    lastName = names.get_last_name()
    dob = '{0}-{1}-{2}'.format(random.choice(year), random.choice(month), random.choice(day))
    pilot_salary = random.choice(salary)
    hire_date = '{0}-{1}-{2}'.format(random.choice(range(2005, 2019)), random.choice(month), random.choice(day))

    pilotsscript.write(f"INSERT INTO PILOT VALUES ({id_}, '{firstName}', '{lastName}','{dob}', '{hire_date}', {pilot_salary}); \n")
