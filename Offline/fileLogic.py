import os
from CONSTANTS import INSTALLEDDIR,FORMSDIR


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
                        f'onclick="navigator.clipboard.writeText(\'{costumer["fullName"]}\')">{costumer["fullName"]} </span>'
                        f'||| <b>{costumer["email"]}</b><br>\n'
                    )
                    file.write(html_line)
    def _helpSecName(self,currName):
        if " " in currName["lname"]:
            return currName["lname"].split(" ")[0]
        return currName["lname"]

    def _helpSecNameForname(self,currName):
        if " " in currName["lname"]:
            return currName["lname"].split(" ")[1]
        return currName["name"]

    def _checkFormName(self, file, currName):
        lname= self._helpSecName(currName)
        name= self._helpSecNameForname(currName)
        #issues with double sec name
        # print(f'{lname}_ΦΟΡΜΑ.pdf ', f'{lname}_{currName["name"]}_ΦΟΡΜΑ.pdf ',f'(ΛΑΘΟΣ){lname}_ΦΟΡΜΑ.pdf ',f'(ΛΑΘΟΣ){lname}_{currName["name"]}_ΦΟΡΜΑ.pdf ')
        hasName= file == f'{lname}_ΦΟΡΜΑ.pdf'
        hasFullName= file == f'{lname}_{name}_ΦΟΡΜΑ.pdf'
        hasNameWrong= file == f'(ΛΑΘΟΣ){lname}_ΦΟΡΜΑ.pdf'
        hasFullNameWrong= file == f'(ΛΑΘΟΣ){lname}_{name}_ΦΟΡΜΑ.pdf'
        return hasName or hasFullName or hasNameWrong or hasFullNameWrong
    
    def _hasFrom(self, currName):
        exists= False
        for form in os.listdir(FORMSDIR):
            exists = exists or self._checkFormName(form, currName)
        return exists
        
    
    def checkFormExtra(self, costumers):
        with open("extraForms.txt", "w", encoding="utf-8") as file:
            for form in os.listdir(FORMSDIR): 
                Write=True
                for costumer in costumers:
                    if self._checkFormName(form, costumer):
                        Write=False
                        continue

                if Write:
                    file.write(f'1: {form}"\n"')
    
    def formsMissing(self, costumers):
         with open("missingForms.html", "w", encoding="utf-8") as file:
            # write the JS once at the top
            counter=0
            for costumer in costumers:
                if not self._hasFrom(costumer):
                    counter+=1
                    html_line = (
                        f'{counter} : '
                        f'<b><span style="cursor:pointer;color:black;" '
                        f'onclick="navigator.clipboard.writeText(\'{costumer["email"]}\')">{costumer["email"]} </span></b> '
                        f'||| {costumer["fullName"]}<br>\n'
                    )
                    file.write(html_line)

