from Online.dataGrab import fetchData
from Offline.parseData import parseData
from CONSTANTS import PAGENUMBER,SITEHTML
from Offline.internalIntegrity import internalIntegrity
from Offline.fileLogic import fileLogic


class main:
    def __init__(self,):
        integrity=internalIntegrity()
        integrity.check()

    def run( self, fetchNew=False, checkMistakes=False, headless= True, writeHtmlList=False):
        if (fetchNew):
            fetchData(headless)
        self.costumers=self.initialiseCostumers()
        if (checkMistakes):
            fileLogic().checkExtra(self.costumers)
        if (writeHtmlList):
            fileLogic().writeHtmlFile(self.costumers)
        return 1

    def initialiseCostumers(self):
        parser=parseData()

        for page in range(1, PAGENUMBER+1):
            with open(f"{SITEHTML}{page}", "r", encoding="utf-8") as file:
                html=str(file.read())
            parser.addPeople(html)
        return parser.getPeople()
    
    def test(self): 
        self.run()
        fileLogic().checkFormExtra(self.costumers)
        fileLogic().formsMissing(self.costumers)
        print(len(self.costumers))
if __name__ == "__main__":
    # main().test()
    main().run(headless=True ,fetchNew=False, checkMistakes=True, writeHtmlList=True)