# All th things needed to run this project. 
## Don't remove. | Removing this will not allow the code to run and you will recive a long error regarding you removing this. 
import speedtest
from rich import print
from tkinter import *
from tkinter.ttk import *

print("    ")
print("[yellow]Python Speed Tester Beta 1.1.0")
print("    ")
print("    ")
print("[purple]Beta Update: Added App/GUI | Test will show in both console/shell/terminal and via output/app/GUI")
print("    ")
print("[bold red]-------------------------------------------------------------")
print("    ")
print("[bold red]Keep in Mind, Internet speed chnage so much that these results may not be as accurate as a speed test site.")
print("    ")
print("[bold red]-------------------------------------------------------------")
print("    ")
print("[blue]Running SpeedTest")
print("    ")

#Declaring the varibles for the Speed Tester
test = speedtest.Speedtest()
download = test.download()
upload = test.upload()
print(f"[green]Download Speed | {download}")
print(f"[green]Upload Speed   | {upload}")

# creates a Tk() object
master = Tk()

# sets the geometry of main
# root window
master.geometry("200x200")


# function to open a new window
# on a button click
def openNewWindow():
	
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("Python Speed Test")

	# sets the geometry of toplevel
	newWindow.geometry("150x500")

	# A Label widget to show in toplevel
	Label(newWindow,
		text ="Python Speed Test Beta 1.1.0").pack()


label = Label(master,
			text ="Python Speed Test V: Beta 1.1.0")

label.pack(pady = 10)

# a button widget which will open a
# new window on button click
btn = Button(master,
			text ="Run Speed Test",
			command = "python3 speed-test.py")
btn.pack(pady = 10)

# mainloop, runs infinitely
mainloop()
