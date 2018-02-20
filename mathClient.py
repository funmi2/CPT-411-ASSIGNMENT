import socket
#create client socket
socket = socket.socket(socket. AF_INET , socket. SOCK_DGRAM )
#initialize and empty list to hold the message (an array of strings)
message = []
#ask user for the operation they want to perform
operation = input (
"""
Net-Centric Assignment client code By Adebayo Funmilayo Taiwo
Please select your operation:
1 - Addidtion of Numbers   2 - Subtraction of Numbers     3 - Multiplication of Numbers
4 - Division of Numbers    5 - Modulus of Numbers
>_
"""
)
#add operation to message
message.append( str (operation))
#ask user for the two values on which the operation is performed
first_variable = input ( 'enter the first value: >_ ' )
second_variable = input ('enter the second value: >_ ' )
#add the values to the message
message.append( str (first_variable))
message.append( str (second_variable))
#format message into [operation,first_varible,second_variable]
message = ',' .join(message)
#send message to client-side
socket.sendto(message, ( '127.0.0.1' , 2014))
#receive result from server
server_result, server_address = socket.recvfrom( 1024 *3 )
print ( 'server result: ' + server_result)
#close connection between client and server
socket.close() ;



