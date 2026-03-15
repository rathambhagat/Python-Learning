# names = input("What's your name? ")
# # Doc note: `open(file, mode)` opens a file and returns a file object. Raises OSError if the file can't be opened.
# # Doc note: Mode `'w'` truncates (wipes) the file before writing. Mode `'a'` appends to the end without erasing existing content.
# file = open("name.txt","w") #overwrite
# file = open("name.txt","a")#append
# # Doc note: `file.write(str)` writes the string to the file. Does NOT add a newline automatically — use `\n` if needed.
# file.write(names)
# # Doc note: `file.close()` flushes the write buffer and releases the OS file handle. Prefer `with open(...) as f:` to close automatically.
# file.close()
"""
'r'-> open for reading (default)

'w'-> open for writing, truncating the file first

'x'-> open for exclusive creation, failing if the file already exists

'a'-> open for writing, appending to the end of file if it exists

'b'-> binary mode

't'-> text mode (default)

'+'-> open for updating (reading and writing)

"""
# # Better Approach and much prefered
# with open("name.txt",mode = "r") as file:
#     lines = file.readlines()
#     print(lines)







