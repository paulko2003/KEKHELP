from dataGrab import fetchData
from parseData import parseData
from CONSTANTS import PAGENUMBER,INSTALLEDDIR
from time import sleep
from internalIntegrity import internalIntegrity
import os
from fileLogic import fileLogic


class main:
    def __init__(self,):
        integrity=internalIntegrity()
        integrity.check()
        

    def run( self, fetchNew=False, checkMistakes=False, headless= True, writeHtmlList=False):
        self.costumers=self.initialiseCostumers(fetchNew, headless)
        if (checkMistakes):
            fileLogic().checkExtra(self.costumers)
        if (writeHtmlList):
            fileLogic().writeHtmlFile(self.costumers)
        return 1

    def initialiseCostumers(self, fetchNew, headless):
        data=fetchData(fetchNew, headless)
        parser=parseData()
        for i in range(1, PAGENUMBER+1):
            html=str(data.getPageSource(i))
            parser.addPeople(html)
        return parser.getPeople()
    
if __name__ == "__main__":
    main().run(writeHtmlList=True)