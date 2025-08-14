class _costumer:
    def __init__(self, KAYAS, name, lname, afm=None,
                  amka=None, stathero=None, kinito=None, email=None,
                    dhmos=None, date=None, title=None,AAe=None,AAt=None,
                    options=[], KAYASlink= None):
        #keeping insted of values.keys so i can be sure of the order being returned
        self.keys= ["KAYAS","name","lname","afm","amka","stathero",
       "kinito","email","dhmos","date", "title", "AAe", "AAt"
       ,"options", "KAYASlink"]
        self.values=dict()
        self.values["KAYAS"]=KAYAS
        self.values["name"]=name
        self.values["lname"]=lname
        self.values["afm"]=afm
        self.values["amka"]=amka
        self.values["stathero"]=stathero
        self.values["kinito"]=kinito
        self.values["email"]=email
        self.values["dhmos"]=dhmos
        self.values["date"]=date
        self.values["title"]=title
        self.values["AAe"]=AAe
        self.values["AAt"]=AAt
        self.values["options"]=options
        self.values["KAYASlink"]=KAYASlink

    def getAll(self):
        person=list()
        for i in range(len(self.keys)):
            person.append(self.values[self.keys[i]])
        return person
    
    def __str__(self):
        return str(self.getAll())
    
    def __getitem__(self,value):
        if value=="ALL": return self.getAll()
        elif value=="fullName":return f'{self.values["lname"]} {self.values["name"]}'
        return self.values[value]

class costumers:
    #essentially a list that handles costumer objects
    #adds removes , iterates , fetches data.
    def __init__(self):
        self.people= list()
        self.len=0

    def __getitem__(self, i):
        return self.people[i]
    
    def __str__(self):
        string= "["
        for person in self.people:
            string+=f'{str(person)},\n'
        string+="]"
        return string
    
    def __iter__(self):
        return iter(self.people)
    
    def __len__(self):
        return self.len

    def _nameBreak(self,fullName:str):
        # print(fullName, fullName.split(" "))
        fullName=fullName.split(" ")
        if (len(fullName)>2):
            # print(fullName)
            firstName=str()
            for name in fullName[:-1:1]:
                firstName+=f'{name} '
            # print(firstName, f' {fullName[-1]}')
            firstName=firstName[0:-1:1]
            lastName=fullName[-1]

            return firstName,lastName
        return fullName
       
    def add(self, KAYAS, fullName, afm=None,
                  amka=None, stathero=None, kinito=None, email=None,
                    dhmos=None, date=None, title=None,AAe=None,AAt=None,
                    options=[],KAYASlink=None):
        lname,name=self._nameBreak(fullName)
        self.people.append(_costumer(KAYAS, name, lname, afm,
                    amka, stathero, kinito, email,
                    dhmos, date, title,AAe,AAt,
                    options,KAYASlink))
        self.len+=1

    def remove(self,KAYAS):
        for i in range(self.len):
            if KAYAS == self.people[i]["KAYAS"]:
               self.people.pop(i)
               self.len-=1
               return 1
        return 0 