import smtplib as s  
ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('kinglalit298@gmail.com','xgbzfhdcitqlsnms')
subject = 'Testing Sending Email from python'
body = 'I Love Teaching Python'
message = 'Subject : {}\n\n {}'.format(subject,body)
listadd = ['lalitkapoor308@gmail.com','balrajsingh6801@gmail.com']
ob.sendmail('kinglalit298@gmail.com',listadd,message)
print('Email Send Successfully')
ob.quit()