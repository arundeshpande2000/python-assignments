marks = {'Arun':39,'Alice':49,'Bill':83,}

name = (input("Enter student name: ")).strip()
name = name.capitalize()

if name  in marks:
    print("{}'s marks: {}".format(name,marks.get(name)))
else:
    print("Student not found")

