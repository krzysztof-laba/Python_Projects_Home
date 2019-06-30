# Write text to the file.
my_list = [i ** 3 for i in range(1, 11)]
print("My list of items:", my_list, "\n")

file = open("output.txt", "r+")

print("Write 'my_list' in a file.txt:")
for item in my_list:
	print(item)
	# Write each item in one line.
	file.write(str(item) + '\n')

file.close()
print("Writing to the file finished.", "\n")
print("*********************************")



# Read text from file.
file_read = open("output.txt", "r+")

print("Read from text file in one part:")
print(file_read.read(), "Finished reading from file.", "\n")
file.close()
print("*********************************")



# Read from file by line.
print("Reading lines from file:")
file_read = open("output.txt", "r")

print("Reading first line from file:")
print(file_read.readline())
print("Reading second line from file:")
print(file_read.readline())
print("Open file closed True/False:", file_read.closed)
print("**************************************************** ********")



# Automatically closing an open file read/write.
print("Auto closing an open file instead of using 'close file'.")

with open("output.txt", "r") as reading_file:
	print(reading_file.readline())
	print("This step automatically close a file without using 'close'.")
print("Open file closed (True/False):", reading_file.closed)
print("**************************************************** ********")