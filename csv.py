# da mone make necessary changes for these variable and remove these unnecesary comments ;)
header_string = 'name,address,phone' # header string for csv column
name = 'fathima'
address = 'tkmcpo'
phone = '2255'

row_line = name+','+address+','+phone
print(row_line)

#comment idanilla mone nee vayichu manasilaaku *)
main_string_data = header_string+'?'+row_line
with open('my_file.csv', 'w') as out:
    lines = [line for line in main_string_data.split('?')]
    my_string = '\n'.join(lines)
    out.write(my_string)

