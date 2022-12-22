from Databases import sqlite3
from datetime import date

class client:

    def __init__(self, userId=0, username="",userPass="",userFirstName="",userLastName="",userDNI="",userBirthday="",userPhone="",userEmail="",userRegisterDate="",userStatus=1,userAddress="",userPaymentCard="",rolId=1):
        self.__userId = userId
        self.__username = username
        self.__userPass = userPass
        self.__userFirstName = userFirstName
        self.__userLastName = userLastName
        self.__userDNI = userDNI
        self.__userBirthday = userBirthday
        self.__userPhone = userPhone
        self.__userEmail = userEmail
        self.__userRegisterDate = userRegisterDate
        self.__userStatus = userStatus
        self.__userAddress = userAddress
        self.__userPaymentCard = userPaymentCard
        self.__rolId = rolId

@property
def userId(self):
    return self.__userId

@userId.setter
def userId(self,userId):
    self.__userId=userId

@property
def username(self):
    return self.__username

@username.setter
def username(self,username):
    self.__username=username

@property
def userPass(self):
    return self.__userPass

@userPass.setter
def userPass(self,userPass):
    self.__userPass=userPass

@property
def userFirstName(self):
    return self.__userFirstName

@userFirstName.setter
def userFirstName(self,userFirstName):
    self.__userFirstName=userFirstName

@property
def userLastName(self):
    return self.__userLastName

@userLastName.setter
def userLastName(self,userLastName):
    self.__userLastName=userLastName

@property
def userDNI(self):
    return self.__userDNI

@userDNI.setter
def userDNI(self,userDNI):
    self.__userDNI=userDNI

@property
def userBirthday(self):
    return self.__userBirthday

@userBirthday.setter
def userBithday(self,userBirthday):
    self.__userBirthday=userBirthday

@property
def userPhone(self):
    return self.__userPhone

@userPhone.setter
def userPhone(self,userPhone):
    self.__userPhone=userPhone

@property
def userEmail(self):
    return self.__userEmail

@userEmail.setter
def userEmail(self,userEmail):
    self.__userEmail=userEmail

@property
def userRegisterDate(self):
    return self.__userRegisterDate

@userRegisterDate.setter
def userRegisterDate(self,userRegisterDate):
    self.__userRegisterDate=userRegisterDate

@property
def userStatus(self):
    return self.__userStatus

@userStatus.setter
def userStatus(self,userStatus):
    self.__userStatus=userStatus

@property
def userAddress(self):
    return self.__userAddress

@userAddress.setter
def userAddress(self,userAddress):
    self.__userAddress=userAddress

@property
def userPaymentCard(self):
    return self.__userPaymentCard

@userPaymentCard.setter
def userPaymentCard(self,userPaymentCard):
    self.__userPaymentCard=userPaymentCard

@property
def rolId(self):
    return self.__rolId

@rolId.setter
def rolId(self,rolId):
    self.__rolId=rolId

def __str__(self):
    return self.__username + "-" + self.__userFirstName + "-" + self.__userLastName + "-" + "-" + self.__userEmail + "-" + self.__userPass

#TODOS LOS USERS SE CREAN COMO CLIENTES. 
#DE NECESITARSE UN USER CON PROFILE DE EMPLEADO, SE DEBE CORREGIR POR BASE DE DATOS.
def addUser(self):
    self.__username = input("Nombre de Usuario: ")
    self.__userPass = input("Contraseña: ")
    self.__userFirstName= input("Nombre: ")
    self.__userLastName= input("Apellido: ")
    self.__userDNI= input("DNI: ")
    self.__userBirthday = input("Fecha de Nacimiento DD-MM-AAAA: ")
    self.__userPhone = input ("Teléfono/Celular: ")
    self.__userEmail= input("Email: ")
    self.__userRegisterDate = date.today()
    self.__userAddress= input("Dirección: ")
    self.__userPaymentCard= input("Ingrese N° Tarjeta: ")
    self.__userStatus=1
    self.__rolId=1
    print("---- El usuario será creado como Cliente ----")
    db=sqlite3.Databases("supermark.db")
#INGRESAR DATOS A LA BD:
    db.insert("client_table", "username, userPass, userFirstName, userLastName, userDNI, userBirthday, userPhone, userEmail, userRegisterDate, userStatus, userAddress, userPaymentCard, rolId",
            f"'{self.__username}','{self.__userPass}','{self.userFirstName}','{self.__userLastName}','{self.__userDNI}','{self.__serBirthday}','{self.__userPhone}','{self.__userEmail}','{self.__userRegisterDate}','{self.__userStatus}','{self.__userAddress}','{self.__userPaymentCard}','{self.__rolId}'")
    db.close()

def login(self,userEmail,userPassword):
    db=sqlite3.Databases("supermak.db")
    client_table=db.select("client_table","userPass",f"email= '{userEmail}'")
    if len(username)>0:
        self.___userPass=client_table[0][0]
        db.close()
        if self.__userPass==userPass:
            return True
        else:
            print("Incorrect Pass")
            return False
    else:
        print("The username does not exist")
        return False

def logout(self):
    self.__userEmail=""
    self.__userPass=""

def editUser(self,userId):
    db=sqlite3.Databases("supermark.db")
    print("Si no desea modificar su usuario, presione Enter")
    print("hasta el Dato que SI quiera modificar.")
    client_table=db.select("client_table","userId,userFirstName,userLastName,userDNI,userBirthday,userPhone,userEmail,userAddress,userPaymentCard")
    self.__username = input(f"Modifique el username: {client_table[0][1]}") or client_table[0][1]
    self.__userPass = input(f"Modifique la contraseña: {client_table[0][2]}") or client_table[0][2]
    self.__userFirstName= input(f"Modifique su Nombre: {client_table[0][3]}") or client_table[0][3]
    self.__userLastName= input(f"Modifique su Apellido: {client_table[0][4]}") or client_table[0][4]
    self.__userDNI= input(f"Modifique su DNI: {client_table[0][5]}") or client_table[0][5]
    self.__userBirthday = input(f"Modifique su fecha de Nacimiento: {client_table[0][6]}") or client_table[0][6]
    self.__userPhone = input(f"Modifique su teléfono: {client_table[0][7]}") or client_table[0][7]
    self.__userEmail= input(f"Modifique su email: {client_table[0][8]}") or client_table[0][8]
    self.__userAddress= input(f"Modifique su dirección: {client_table[0][9]}") or client_table[0][9]
    self.__userPaymentCard= input(f"Modifique sus datos de Tarjeta de pago: {client_table[0][10]}") or client_table[0][10]
    db.update("client_table","username",f"'{self.__username}'",f"userId={userId}")
    db.update("client_table","userPass",f"'{self.__userPass}'",f"userId={userId}")
    db.update("client_table","userFirstName",f"'{self.__userFirstName}'",f"userId={userId}")
    db.update("client_table","userLastName",f"'{self.__userLastName}'",f"userId={userId}")
    db.update("client_table","userDNI",f"'{self.__userDNI}'",f"userId={userId}")
    db.update("client_table","userBirthday",f"'{self.__userBirthday}'",f"userId={userId}")
    db.update("client_table","userPhone",f"'{self.__userPhone}'",f"userId={userId}")
    db.update("client_table","userEmail",f"'{self.__userEmail}'",f"userId={userId}")
    db.update("client_table","userAddress",f"'{self.__userAddress}'",f"userId={userId}")
    db.update("client_table","userPaymentCard",f"'{self.__userPaymentCard}'",f"userId={userId}")
    db.close()
   
def deleteUser(self,userId):
    db=sqlite3.Databases("supermark.db")
    db.update("client_table","userStatus",f"userId={userId}")
    db.close()

def all_clients(self):
    db=sqlite3.Databases("supermark.db")
    client_table=db.select_all("client_table","userId,userFirstName,userLastName,userDNI,userBirthday,userPhone,userEmail,userRegisterDate,userStatus,userAddress,userPaymentCard,rolId")
    print("NRO\tFirstName\tLastName\tDNI\tBirthday\tPhone\tEmail\tRegisterDate\tStatus\tAddress\tPaymentCard\tRol")
    for user in client_table:
        rol=db.select("rol_table","username",f"rolId='{user[11]}'")
        print(f"{user[0]}\{user[1]}\{user[2]}\{user[3]}\{user[4]}\{user[5]}\{user[6]}\{user[7]}\{user[8]}\{user[9]}\{user[10]}\{user[0][0]}")
    db.close()


