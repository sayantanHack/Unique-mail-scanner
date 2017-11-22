print "OPEN a new file for scaning."
#fname = raw_input("Enter file name: ")   choose other files as well manually .
file_text = open('List of log.txt')
count = 0
word_list =[]           #making blank list
for line in file_text:
    line.rstrip()
    if not line.startswith("From"): continue    #if line starts with From then only applicable use your custom starts with.      
    words = line.split()
    if words[1] not in word_list:            #I select the 2nd word & check if it`s in the new list word_list(Which is initially empty.) .
        word_list.append(words[1])          #if the word is new & never seen before in Word_list then add to word_list.
        print "Emails : " ,words[1]                       
        count += 1                            #counting the iterations , How many mals we get.
print "The mail itterates ",count ,'times.'

