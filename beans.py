class person:  
    def __init__(self, cin,nom,prenom,tel,email):
       self.cin=cin
       self.nom=nom 
       self.prenom=prenom
       self.tel=tel
       self.email=email
    def setCin(self,cin):
        self.cin=cin
    def setNom(self,nom):
        self.nom=nom
    def setPrenom(self,prenom):
        self.prenom=prenom
    def setTel(self,tel):
        self.tel=tel
    def setEmail(self,email):
        self.email=email
    def __str__(self):
        return str(self.cin)+' '+self.nom+' '+self.prenom+' '+self.tel+' '+self.email
    def getJson(self):
        return {'cin':self.cin,'nom':self.nom,'prenom':self.prenom,'tel':self.tel,'email':self.email}
    def aff(self):
        print(str(self.cin)+' '+self.nom+' '+self.prenom+' '+self.tel+' '+self.email)
