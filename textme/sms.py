from twilio.rest import Client 
 
account_sid = 'enter SID number' 
auth_token = 'enter token number' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG2d14d10556fe99a8f6c6e4fc36a2ee7c', 
                              body='HI!',      
                              to='enter #' 
                          ) 
 
print(message.sid)
