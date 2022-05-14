print("file modifier")
filename = input("filepath: ")
file = open(filename)
text = file.read()
print("content:")
print(text)
while True:
      choice = input("modify y/n: ")
      if choice == "n":
            file.close()
            print("file closed")
            break
      elif choice == "y":
            file.close()
            file1 = open(filename, 'w')
            file1.write(input("new text: "))
            file1.close()
            print("file modified")
            file2 = open(filename)
            text1 = file2.read()
            print("check:")
            print(text1)
            file2.close()
            print("file closed")
            break
      else:
            print("input exception")
end = input("enter to terminate")
