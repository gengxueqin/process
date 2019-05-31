#  \x06,\X07全角空格  \X08 无空格？


bytes = b'\x08m99'
a='banana'
str = bytes.decode()
print(a)
print(str)