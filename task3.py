
#Write a Python program that accepts a filename from the user and prints the extension of the file.


filename = input("Enter the filename: ")  
extension = filename.split('.')[-1]  
print(f"The extension of the file is: {extension}")  
