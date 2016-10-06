import subprocess
import os


'''
This program will unencrypt hard drives so that they can be deleted in terminal. 
It outputs a list of all of the drives it recognizes, and allows the user to input the drive of interest.
Then it runs the proper terminal command to remove the UUID from the drive so that it can be zeroed in terminal. 
'''
proc = subprocess.Popen(["diskutil cs list"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
list_out = out.split("\n")


newList = []
for item in list_out:
    #this removes all lines from the file except for the lines required to identify the name of the drive and the UUID
    if ("Name" in item):
        if ("LV" not in item) and ("Volume" not in item):
            newList.append(item)
    elif ("Logical Volume Group" in item):
        newList.append(item)

final_list = []
for item in newList:
    #this further removes from the list any extraneous information
    if "Name" in item:
        x = item.split("         ")
        final_list.append(x[1])
    else: 
        y = item.split(" ")
        final_list.append(y[4])

for item in range(len(final_list)):
    counter = 1
    if item % 2 == 1:
        print item,final_list[item]
        
#user is shown a list of (odd numbered) disk names, they input the number of the disk of interest 
user_input = input("Which is your disk? ")

UUID = final_list[user_input - 1]

os.system("diskutil cs delete " + UUID)





        