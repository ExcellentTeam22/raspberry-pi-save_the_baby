# # import smtplib
# #
# # gmail_user = 'savethebabyraspi@gmail.com'
# # gmail_password = 'hwmujicgkqihytqg'
# #
# # sent_from = gmail_user
# # to = ['shaindel720@gmail.com']
# # subject = 'Alert!! Baby left in car unattended'
# # body = 'Youre baby was left in the car unattended.' \
# #        'Please go back to the car in next minute.' \
# #        'If not we will contact the police!'
# #
# # email_text = """\
# # From: %s
# # To: %s
# # Subject: %s
# #
# # %s
# # """ % (sent_from, ", ".join(to), subject, body)
# #
# # try:
# #     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# #     server.ehlo()
# #     server.login(gmail_user, gmail_password)
# #     server.sendmail(sent_from, to, email_text)
# #     server.close()
# #
# #     print ('Email sent!')
# # except:
# #     print ('Something went wrong...')
# import smtplib
# import imghdr
# from email.message import EmailMessage
#
# gmail_user = 'savethebabyraspi@gmail.com'
# gmail_password = 'hwmujicgkqihytqg'
# receiver_email = "shaindel720@gmail.com"
#
# newMessage = EmailMessage()
# newMessage['Subject'] = "Alert!! Baby left in car unattended"
# newMessage['From'] = gmail_user
# newMessage['To'] = receiver_email
# newMessage.set_content('We have detected your child alone in the car.'
#                        'Please go back to the car in next immediately'
#                        'If not we will contact the police!')
#
#
# def send_emergency_email(image_name):
#     with open(image_name, 'rb') as f:
#         image_data = f.read()
#         image_type = imghdr.what(f.name)
#         image_name = f.name
#         newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
#
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(gmail_user, gmail_password)
#         smtp.send_message(newMessage)
#
#
# if __name__ == "__main__":
#     send_emergency_email('pi.jpg')
import userInterface
# if __name__ == "__main__":
