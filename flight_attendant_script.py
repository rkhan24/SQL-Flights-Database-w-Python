import names
import random
import requests
from bs4 import BeautifulSoup

from csv import reader

flight_attendantscript = open("flightattendant.sql", "w")

traveler_id = range(0,200)
flight_id = range(0,300)

month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']
year = range(2010, 2020)


for i in range(800):
    id_ = i
    trav_id = random.choice(traveler_id)
    flt_id = random.choice(flight_id)
    flight_date = '{0}-{1}-{2}'.format(random.choice(year), random.choice(month), random.choice(day))
    print(id_, trav_id, flt_id, flight_date)
    flight_attendantscript.write(f"INSERT INTO FLIGHT_ATTENDANTS VALUES ({id_}, {flt_id}, {trav_id}, '{flight_date}'); \n")
