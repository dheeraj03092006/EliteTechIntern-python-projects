def slicer(email):
    mail_list = email.split("@")
    return mail_list

input_mail = input("enter your mail id ")
split_mail = slicer(input_mail)
user_name = split_mail[0]
domain = split_mail[1]
print("The username of given email id is ",user_name," and the domain is ",domain)