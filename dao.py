import mysql.connector
from beans import person
class dao:
    mydb = mysql.connector.connect(
      host='localhost',
      user='root',
      password='',
      database='myData'
    )
    sql= 'select cin,nom,prenom,tel,email from person order by id desc limit 3'
    def affPers(self):
        pers=[]    
        mycursor = self.mydb.cursor()
        mycursor.execute(self.sql)
        for row in mycursor:
            pers.append(person(row[0],row[1],row[2],row[3],row[4]))           
        return pers
    def insertPers(self,per):
        sql_ins='INSERT INTO person (cin, nom, prenom, tel, email) VALUES (%s, %s, %s, %s, %s)'    
        mycursor = self.mydb.cursor()
        val=(per.cin,per.nom,per.prenom,per.tel,per.email)
        mycursor.execute(sql_ins,val)
        self.mydb.commit()
    def searchPers(self,id):
        mycursor = self.mydb.cursor()
        sql_srch= 'select cin,nom,prenom,tel,email from person where id='+str(id)+' order by id desc limit 10'
        val=(id)
        mycursor.execute(sql_srch)
        for x in mycursor:
            row=x
        return person(row[0],row[1],row[2],row[3],row[4])
    def affJson(self):
        pers=[]
        mycursor = self.mydb.cursor()
        mycursor.execute(self.sql)
        for row in mycursor:
            pers.append(person(row[0],row[1],row[2],row[3],row[4]).getJson())           
        return pers
    