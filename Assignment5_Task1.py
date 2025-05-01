#Creating list of student name and marks
marks = {'Arun':39,'Alice':49,'Bill':83}

#Reading input from user.  Stripping the input to ensure all leading
#and trailing spaces are ignored
name = (input("Enter student name: ")).strip()

#Capitalizing input name, to ensure it matches with names in
#dictionary.
name = name.capitalize()

#if name exists in dictionary, print marks otherwise print
#proper message
if name  in marks:
    print("{}'s marks: {}".format(name,marks.get(name)))
else:
    print("Student not found")

