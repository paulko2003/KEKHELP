import os
from CONSTANTS import SITEHTML


class internalIntegrity:
    def __init__(self):
        self.paths=os.listdir()
        print(self.paths)

    def _cSiteData(self):
        absPath=SITEHTML.split('/')
        relPath=absPath[-2] #-1 einai to "" giati to SITEHTML teleionei se /
        if not (relPath in self.paths):
            os.mkdir(relPath)
        
    def check(self):
        self._cSiteData()