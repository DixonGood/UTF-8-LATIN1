code = b'r\xc3\xa9sum\xc3\xa9'
print(code)
print(len(code))
code_old = code.decode()
print(code_old)

code_new = code_old.encode('Latin1')
print(code_new)
print(len(code_new))

code_new1 = code_new.decode('Latin1')
print(code_new1)