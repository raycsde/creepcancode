#this program shows name how to upper and lower its first zimu
#f"{} {}" f means format let two variables be together
ur_name = "eric"
message = f"Hello {ur_name.title()}"
print(f"{message}, would you like to learn some Python today?")
print(message.title())
print(message.upper())
print(message.lower())
name_firstmodern = "albert"
name_lastmodern = "einstein"
name_fullmodern =f"{name_firstmodern} {name_lastmodern}"
print(f'\t{name_fullmodern.title()} once said, "A person who never made a mistake never tried\nanything new."')
message_new = f'\t{name_fullmodern.title()} once said, "A person who never made a mistake never tried\nanything new."'
print(message_new)

#lstrip() delete the left blank
#rstrip() delete the right blank
#strip() delete the left and right blank
name_sun = "\tsunsunsun   \n\tmoon   "
print(name_sun)
print(name_sun.lstrip())
print(name_sun.rstrip())
print(name_sun.strip())