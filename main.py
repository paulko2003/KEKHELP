from checkInstalled import checkInstalled
from dataGrab import fetchData
from parseData import parseData
from CONSTANTS import PAGENUMBER,INSTALLEDDIR
from time import sleep
from internalIntegrity import internalIntegrity
import os

def checkExtra(lista):
    with open("extras.txt", "w", encoding="utf-8") as file:
        for dir in os.listdir(INSTALLEDDIR): 
            Write=True
            for page in lista:
                for item in page:
                    # print(dir, "   \n", item[1])
                    if dir == item[1]:
                        # print('me hehe')
                        Write=False

            if Write:
                file.write(f'1: {dir}"\n"')

            
        

if __name__ == "__main__":
    integrity=internalIntegrity()
    data=fetchData()
    parser=parseData()
    integrity.check()
    html=""
    everything=[]
    for i in range(1, PAGENUMBER+1):
        html=str(data.getPageSource(i))
        everything.append(list(parser.getPeople(html)))
        sleep(0.3)
    print(len(everything))

    with open("llista.html", "w", encoding="utf-8") as file:
        # write the JS once at the top
        counter=0
        for page in everything:
            for person in page:
                if checkInstalled(INSTALLEDDIR, person[1]):
                    counter+=1
                    html_line = (
                        f'{counter} : <a href="{person[0]}">kayas</a> ||| '
                        f'<span style="cursor:pointer;color:black;" '
                        f'onclick="navigator.clipboard.writeText(\'{person[1]}\')">{person[1]}</span><br>\n'
                    )
                    file.write(html_line)
    checkExtra(everything)
