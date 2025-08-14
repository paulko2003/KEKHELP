from dataGrab import fetchData
from parseData import parseData
from CONSTANTS import PAGENUMBER,INSTALLEDDIR
from time import sleep
from internalIntegrity import internalIntegrity
import os
from fileLogic import fileLogic


class main:
    def __init__(self, fetchNew=True, checkMistakes=True, headless= False, writeHtmlList=True):
        integrity=internalIntegrity()
        integrity.check()
        self.costumers=self.initialiseCostumers(fetchNew, headless)
        print(len(self.costumers))
        if (checkMistakes):
            fileLogic().checkExtra(self.costumers)
        if (writeHtmlList):
            fileLogic().writeHtmlFile(self.costumers)
    

    def initialiseCostumers(self, fetchNew, headless):
        data=fetchData(fetchNew, headless)
        parser=parseData()
        for i in range(1, PAGENUMBER+1):
            html=str(data.getPageSource(i))
            parser.addPeople(html)
        return parser.getPeople()
    
if __name__ == "__main__":
    main(fetchNew=False, checkMistakes=True, headless=True)