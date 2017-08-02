from Tkinter import *
#List to store values
my_list = []
# Front lables to display
flabels = []
# Answer lables
alabels = []
# Dummy list generator incrementor
i = 1

def start_app():
    """ 
	Start the application when start button pressed
	"""
    #Disable start button after presee
    start_button.config(state=DISABLED)
    print "Starting app!"
    update_values()

def stop_app():
    """
	Stop the app
    """
    print "Stopping"
    master.quit()

def update_values():
    """
	Helper function to trigger label values after reading list
    """
    my_list = dummy_list_gen()
    update_label_values(my_list)
    # Repeat the function after 1s (no need time.sleep)
    master.after(1000, update_values)

def dummy_list_gen():
    """
	Dummy List generator
    """
    global i
    my_list = [3,2,3,4,5]
    my_list = [i] * 5
    print my_list
    i += 1
    return my_list

def update_label_values(my_list):
    """
	Update the answer lables values with list
    """
    for label in alabels:
        for i in range(5):
            label.config(text=str(my_list[i])+' Ohm')
        #update idletasks finish all tk loops of current execution
        master.update_idletasks()

#Declare new master
master = Tk()

#Create a canvas to place label and button at desired place
w = Canvas(master, width=400, height=300)
w.pack()

#Example string
string = 'Channel'

#Define x axis for front label
lblx = 70

#Define Y axis for front label
lbly = 50

#Loop over and define labels Here i need 5 labels
for x in range(5):
    str_label = string + str(x)
    label = Label(master, text=str_label, fg='white', bg='black')
    label.pack()
    flabels.append(label)
    
#Add Front lables to canvas
for label in flabels:
    w.create_window(lblx,lbly,window=label)
    lbly = lbly + 20

#Define x axis for answer label
lblx = 140

#Define y axis for answer label
lbly = 50

#Loop over and define labels Here i need 5 labels
for x in range(5):
    str_label = string + str(x)
    label = Label(master, text=str_label, fg='white', bg='blue')
    label.pack()
    alabels.append(label)

#Add Answer lables to canvas    
for label in alabels:
    w.create_window(lblx,lbly,window=label)
    lbly = lbly + 20

#Create start button and call start_app function
start_button = Button(master, text="Start",height=2, width=10, command=start_app)
start_button.pack()

#Create Stop button to exit program
stop_button = Button(master, text="Stop",height=2, width=10, command=stop_app)
stop_button.pack()

#Add buttons to canvas
w.create_window(70, 170, window=start_button)
w.create_window(190, 170, window=stop_button)

#main loop
master.mainloop()
