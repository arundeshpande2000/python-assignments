
try:
    file1 = open("output.txt","w")
    str1 = input("Enter text to write to the file: ")
    file1.write(str1+"\n")
    print("Data successfully written to file output.txt\n")

    str1 = input("Enter additional text to append to the file: ")
    file1.write(str1)
    print("Additional data successfully written to file output.txt\n")
    file1.close()

    file1 = open("output.txt", "r")
    print("Final content of output.txt")
    lines = file1.read()
    print(lines)
    file1.close()

except:
    print("file output.txt was not found.")


