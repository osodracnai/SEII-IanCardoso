
#  Ian Cardoso
# 11411EMT014


 message = "Hello World"
 print(message)
 print(message[6:])
 
 print(message.lower())
 print(message.upper())
 print(message.count("Hello"))
 
 print(message.find('World')) #retorna -1 se não encontrar
 
 newMessage = message.replace('World', 'Universe')
 
 greeting="Hello"
 name="Ian"
 
 message = '{}, {}. Welcome!'.format(greeting, name)
 message = f'{greeting}, {name.upper()}. Welcome!'

print(dir(name)) 
print(help(str))
 