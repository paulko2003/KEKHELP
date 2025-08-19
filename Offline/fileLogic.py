import os
from CONSTANTS import INSTALLEDDIR


class fileLogic:

    def _checkInstalled(self,dir,name): ##if name not in dir install
        return not (name in os.listdir(dir))

    def checkExtra(self, costumers):
        with open("extras.txt", "w", encoding="utf-8") as file:
            for dir in os.listdir(INSTALLEDDIR): 
                Write=True
                for costumer in costumers:
                    if dir == costumer["fullName"]:
                        Write=False
                        continue

                if Write:
                    file.write(f'1: {dir}"\n"')

    def writeHtmlFile(self, costumers):
        with open("llista.html", "w", encoding="utf-8") as file:
            # write the JS once at the top
            counter=0
            for costumer in costumers:
                
                if self._checkInstalled(INSTALLEDDIR, costumer["fullName"]):
                    counter+=1
                    html_line = (
                        f'{counter} : <a href="{costumer["KAYASlink"]}">kayas</a> ||| '
                        f'<span style="cursor:pointer;color:black;" '
                        f'onclick="navigator.clipboard.writeText(\'{costumer["fullName"]}\')">{costumer["fullName"]}</span><br>\n'
                    )
                    file.write(html_line)