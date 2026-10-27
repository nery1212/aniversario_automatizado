##################### Hard Starting Project ######################
import smtplib
import random
import pandas as pd
import datetime as dt
lista_arquivos = []

#--------parte que usa pandas-------------#
arquivo = pd.read_csv('birthdays.csv')

nome = arquivo.loc[0, 'name']

email = arquivo.loc[0, 'email']

ano = arquivo.loc[0, 'year']

mes = arquivo.loc[0, 'month']

dia = arquivo.loc[0, 'day']

#------------datetime-----------#

agora = dt.datetime.now()
dia_atual = agora.day
mes_atual = agora.month







#------------abrir arquivo aleatorio-------------#
with open("letter_templates/letter_1.txt") as arquivo:
    letter_templates1 = arquivo.read()
with open("letter_templates/letter_2.txt") as arquivo:
    letter_templates2 = arquivo.read()
with open("letter_templates/letter_3.txt") as arquivo:
    letter_templates3 = arquivo.read()

lista_arquivos.append(letter_templates1)
lista_arquivos.append(letter_templates2)
lista_arquivos.append(letter_templates3)

escolha_aleatoria = random.choice(lista_arquivos)



#-------------mandar email--------------#
my_email = "EMAIL"
password = "SENHA"
if mes_atual == mes and dia_atual == dia:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="email",
                            msg=f"Subject:Feliz aniversario\n\n {escolha_aleatoria}")








# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



