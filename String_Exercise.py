# s = 'Hello World'
# print('d'+ s[1:-1] + 'h')

# s1 = 'Hello'
# s2 = 'World'
# s3 = s1[1:] + s2[:len(s2)-2]
# print(s3)

# s = 'Hello World !'
# s1 = (s[:2] * 5) + 'Hello World' + (s[-1:] * 3)
# print(s1)


# from re import sub

# mail_id = str(input('Enter your mail ID = '))
# index1 = mail_id.index('@') #index only use for get the value of string
# username = mail_id[:index1]
# special_case = sub(r'[^a-zA-Z]','', username).upper()
# domain = mail_id[index1 + 1:]

# print(f'User name is = {special_case}')
# print(f'Domain name is = http:www.{domain}')



# string = 'Deepa 35 *9/11/1977* Najibabad'
# n1 = string.index('*')
# n2 = string.rindex('*')
# n3 = string[n1+1:n2]
# print(n3)

# s = '    welcome to Bengaluru     '
# steam = print
# steam(s.lstrip())
# steam(s.rstrip())


# s = 'he  he  that  he  that  he that that he he that'
# replace1 = s.replace('he','she').replace('that','  ').split(' ')
# print(replace1)

# s = 'Hello World'
# upper_lower = f'The First word in upper case  = [{s[:5].upper().center(15,'*')}] \nThe Second word in the lower case  =  [{s[6:].lower().center(15,'*')}]'
# print(upper_lower)

# s = 'Line should be straight and end will be proper Done'
# s1 = s[:4]
# s2 = s[-4:]
# print(s1)
# print(s2)
# start_end = s.startswith('Line') and s.endswith('Done')
# print(start_end)


# name = 'Anirudh Bhattacharya'
# dob = '06/07/1982'
# city = 'Faridabad'

# upto_8_char = name[0:8:2]
# print(upto_8_char)

# first2_last2 = dob[:2] + dob[-2:]
# print(first2_last2)

# first3 = city[:3]
# print(first3)

# code = upto_8_char + first2_last2 + first3
# print(code)

# s = 'I am Anirudh Bhattacharya'
# dash = s.center(80,'_')
# print(dash)

# print(80 * '_')


# s = (5 * '-')
# print(s,'\n',s,'\n',s,'\n',s,'\n',s)

# print('\n' * 5)

# n = '1234'
# integer = n[::-1]
# print(integer)


# n = '1234'
# reverse_integer = int(n[::-1])
# print(reverse_integer)

# n = 1234
# reverse_integer = int(str(n)[::-1])
# print(reverse_integer)

# s = '     Python     '
# s1 = s.rjust(20,'_').strip()
# print(s1)

# s = '     love/Python/     '
# s1 = s.strip().rjust(20,'-')
# s2 = s.strip().ljust(20,'-')
# print(s1 + s2)


# str = "caattt's curiosity killed the cat"
# prefix = str.removeprefix("caattt's")
# print(prefix) 

# print()
# print('Anirudh:',end='\n')