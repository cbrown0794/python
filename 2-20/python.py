filename = input("Enter filename: ")
outfile = open(filename, "w")
content_ = "This is a test\n"

try:
    outfile.write(content_)
except Exception as e:
    print("An error occurred while writing to the file:", e)
finally:
    outfile.close()
    print("File has been safely closed.")