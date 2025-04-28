
try:
    file1 = open("Sample.txt","r")
    lines = file1.readlines()

    lineno = 0
    for line in lines:
        lineno += 1
        print("Line ",lineno,": ",line.strip())

    file1.close()

except:
    print("file Sample.txt was not found.")