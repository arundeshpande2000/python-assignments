
try:
    file1 = open("Sample.txt","r")
    lines = file1.readlines()

    for line in lines:
        print(line)

    file1.close()

except:
    print("Sample.txt doesn't exist")


