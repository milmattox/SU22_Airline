#Airline Reservation program
#Michelle Mattox
#July 17, 2022

import tkinter as tk
from tkinter import *

ws = Tk()
ws. title("E=mc\u00b2 Airlines")
ws.geometry('800x600')
ws.config(bg='#EEEEEE')
titleLabel = tk.Label(text = "E=mc\u00b2 Airline Reservations")
titleLabel.grid(row=0,column=0)
directionsLabel = tk.Label(text = "Choose a passenger from the list:")
directionsLabel.grid(row = 1, column = 0)

#passenger list
passengers = ["Ardeen, Blount","Crystal,Ballantyne","Cristina,Slany","Nicole,Pauling","Doy,Liddington","Lincoln,Moultrie","Binny,Lockney","Pris,Clitsome","Redd,Jekyll","Homerus,Braycotton","Judah,Willman","Helenelizabeth,Mallabone","Kirstyn,Kassman","Iolanthe,Melendez","Debbie,Dignon","Rosalyn,Aylott","Georgine,Nealon","Hatti,Durban","Sapphira,Lassells","Wini,Kuhnert","Ken,Benoit","Lindy,Woolard","Sonia,Spinola","Emmie,Ewers","Glenden,Fehner"]
#variables
person=''   
assigned=[]
availableFirstSeats = []
availableBusinessSeats = []
availableEconomySeats = []
assignedSeats=[]
seats = []
seatNotTaken = True
var = IntVar()  #class choice
pos = 0

def build_seats(rows,cols):  #creates a 2D Array of seats
    for r in range(0,rows):
        seats.append([(str(r+1)+chr(c+65)) for c in range(0,cols)])
    return seats

def available(rows,cols):
    for r in range(0,3):
        availableFirstSeats.append([(str(r+1)+chr(c+65)) for c in range(0,cols,2)])
    print(availableFirstSeats)
    for r in range(3,7):
        availableBusinessSeats.append([(str(r+1)+chr(c+65)) for c in range(0,cols,2)])
    print(availableBusinessSeats)
    for r in range(7,20):
        availableEconomySeats.append([(str(r+1)+chr(c+65)) for c in range(0,cols,2)])
    print(availableEconomySeats)
    return availableFirstSeats, availableBusinessSeats, availableEconomySeats


#----------unassigned listbox    
def create_unAssignedPassengerList():  #create listbox of unassigned passengers
    for i in range(len(passengers)):
        noAssignedSeatlb.insert(i,passengers[i])
#------------unassigned listbox end
        
def sel(): #choose Class for seat assignment
    selection = "You selected the option " + str(var.get())
    classChoice.config(text = selection)
#listbox for unassigned passengers
noAssignedSeatlb=tk.Listbox()
noAssignedSeatlb.grid(row = 2, column = 0, rowspan = 8)
#radio button for class choice
R1 = tk.Radiobutton(text="First Class", variable=var, value=1,
                  command=sel)
R1.grid(row = 10, column = 0 )

R2 = tk.Radiobutton(text="Business", variable=var, value=2,
                  command=sel)
R2.grid( row = 11, column = 0)
R3 = tk.Radiobutton(text="Economy", variable=var, value=3,
                  command=sel)
R3.grid( row = 12, column = 0)

classChoice = tk.Label()
classChoice.grid(row = 0, column = 12)

message = tk.Label(text = '')
message.grid(row = 13, column = 0)

def ReserveSeat():
    global person
    ch_class = var.get()
    person = noAssignedSeatlb.get(ANCHOR)
    print(person)
    if len(person) == 0:
        message.config(text = 'Choose a person')
    else:
        message.config(text = "")
    if ch_class == 0:
        message.config(text = "Choose a class!")
    elif ch_class == 1:
        message.config(text = "First class")
        assignedSeats[pos][0]=person
        assignedSeats[pos][1]=availableFirstSeats[0][0]
        print(assignedSeats)


autoReserve = tk.Button(text = "Assign Seat", bg = "lightgreen", command = ReserveSeat)
autoReserve.grid(row = 14, column = 0)

def covidSeat(k): #report that seat is not available due to covid restrictions
    messageLabel = tk.Label(text = "Seat "+ k + " NOT available due to COVID restrictions!")
    messageLabel.grid(row = 1, column = 15)
    
def reserveSeat(k):
    pass
    '''global assignedSeats
    if k not in assignedSeats:
        print(len(assignedSeats))
        assignedSeats.append([k,['''
def seatTaken(k):
    pass

def create_seat_buttons(seats):
    m = 1
    for r in seats:
        m=m+1
        n=4
        for col in r:
            n = n + 1
            if n % 2 == 0:
                seatButton = tk.Button(text = col, width=3, bg="lightgray", command=lambda k=col:covidSeat(k))
            elif seatNotTaken:
                seatButton = tk.Button(text = col, width=3, bg="lightblue", command=lambda k=col:reserveSeat(k))
            else:
                seatButton = tk.Button(text = col, width=3, bg="red", command=lambda k=col:seatTaken(k))
            seatButton.grid(row = m ,column = n )

build_seats(20,7)
available(20,7)
create_seat_buttons(seats)
print(seats[6][6])
create_unAssignedPassengerList()


