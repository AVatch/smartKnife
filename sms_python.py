from twilio.rest import TwilioRestClient

account_sid = "ACa9d55e2824dbbbd3bda7b4e5a7a2e418"
auth_token = "4e9d3571e0828ee83f24685fc4566615"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+12673349121", from_="+16314065044",
                                     body="Hello there!")
