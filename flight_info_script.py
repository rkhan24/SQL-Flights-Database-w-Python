from csv import reader
import random


flight_info_script_ = open("flight_info_script.sql", "w")

airlines = [ "AAY", "AAL", "DAL", "FFT", "JBU", "SWA", "NKS", "UAL"]
airports = ["IAH", "HOU", "DAL", "DFW", "AUS", "SAT", "JFK", "LGA", "EWR", "LAX", "DEN", "PHX", "MIA", "MCO", "ATL", "ORD", "MDW", "BWI", "BOS", "DTW", "MSP", "MCI", "STL", "LAS", "CLT", "CLE", "PDX", "PHL", "PIT", "BNA", "SLC", "MKE", "SEA", "DCA", "IAD", "ANC", "HNL", "MSY", "SAN"]
terminal = ["", "A", "B", "C", "D", "E", "F", "G"]
gate = range(1,50)
hour = range(0,24)
minute = range(0,60)

durationIncrement = range(1,4)

for i in range(300):
    flight_id = i
    airline_ = random.choice(airlines)
    dept_airport = random.choice(airports)
    arr_airport = random.choice(airports)

    if arr_airport == dept_airport:
        arr_airport = "ATL"
    departure_hour = random.choice(hour)

    if arr_airport == "ANC" or dept_airport == "ANC":
        airline_ = "ASA"
    elif arr_airport == "HNL" or dept_airport == "HNL":
        airline = "HAL"
       

    if departure_hour < 10:
        departure_hour = "0{0}".format(departure_hour)

    departure_minute = random.choice(minute) 

    if departure_minute < 10:
        departure_minute = "0{0}".format(departure_minute)

    flight_dept_time = "{0}:{1}".format(departure_hour, departure_minute)

    arrival_hour = int(departure_hour) + random.choice(durationIncrement)
    arrival_minute = random.choice(minute) 

    if arrival_minute < 10:
        arrival_minute = "0{0}".format(arrival_minute)

    if arrival_hour >= 24:
        arrival_hour = arrival_hour - 24

    if arrival_hour < 10:
        arrival_hour = "0{0}".format(arrival_hour)
    

    flight_arr_time = "{0}:{1}".format(arrival_hour, arrival_minute)

    if int(departure_hour) > int(arrival_hour):
        flight_arr_day = "Next Day"
    else: 
        flight_arr_day = "Same Day"

    
    gateNum = "{0}{1}".format(random.choice(terminal), random.choice(gate))

    pilot_id = random.choice(range(0,250))
    
    #print(flight_id, airline_, dept_airport, arr_airport, flight_dept_time, flight_arr_time, flight_arr_day, gateNum)
    flight_info_script_.write(f"INSERT INTO FLIGHT_INFO VALUES ({flight_id}, '{airline_}', '{dept_airport}', '{arr_airport}', '{flight_dept_time}', '{flight_arr_time}', '{flight_arr_day}', '{gateNum}', {pilot_id}); \n")



# with open('Flight_Info.csv', 'r') as read_obj:

#     csv_reader = reader(read_obj)

#     for val in csv_reader:
#         sqlscript.write(f"INSERT INTO FLIGHT_INFO VALUES ({val[0]},'{val[1]}', '{val[2]}', '{val[3]}', '{val[4]}','{val[5]}', '{val[6]}', '{val[7]}'); \n ")