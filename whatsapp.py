from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACd15f157b32130ab93bc69e91d432acd6'
auth_token = '65ca15446b076c61cf4e3971ad3978b0'
# this is the Twilio sandbox testing number
from_whatsapp_number = 'whatsapp:+14155238886'


def sendEmergencyWhatsapp(userPhoneNum):
    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client(account_sid, auth_token)
    print(userPhoneNum)
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number = 'whatsapp:+972584864862'
    # to_whatsapp_number = 'whatsapp:' + str(userPhoneNum)
    # print(to_whatsapp_number)
    client.messages.create(body='We have detected that your child is alone in the car.'
                                ' Please go back to the car immediately.'
                                '\n-Carsafey',
                           media_url='https://media.istockphoto.com/photos/baby-in-a-carseat-picture-id1217449568?k=20&m=1217449568&s=612x612&w=0&h=WhvnmAwm4Wfxm2TRZtXcpRFnRD-lDbV8_WIPRUm-p1c=',
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)
