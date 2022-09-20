with open("name.txt", 'r', encoding='utf-8') as name_file:
   name = name_file.read()
   name.strip()
   
   with open("body.txt", 'r', encoding='utf-8') as body_file:
    body = body_file.read()

    mail = "Hello ! " + name + "\n" + body

    with open(name+".txt", 'w', encoding='utf-8') as mail_file:
        mail_file.write(mail)