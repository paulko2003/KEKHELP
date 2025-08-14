from bs4 import BeautifulSoup
from helpers.costumers import costumers

class parseData:
    def __init__(self):
        self.costumers= costumers() 

    def getPeople(self):
        return self.costumers 
        

    def addPeople(self, html:str):
        #returns 
        soup = BeautifulSoup(html, "html.parser")
        self.rows0 = soup.find_all("tr", class_="row0") #to site exei 2 klaseis 1 gia mple mia gia axno mple, parinei afta ta 2 kai ta ksexorizei
        self.rows1 = soup.find_all("tr", class_="row1")
        self._makePpleList()
        
    def _getRowData(self, row):
        cells= row.find_all("td", class_=["cell_num_0", "cell_num_1","cell_num_2","cell_num_3","cell_num_4","cell_num_5","cell_num_6","cell_num_7","cell_num_8","cell_num_9","cell_num_10","cell_num_11"])
        KAYAS=cells[0].get_text(strip=True)
        fullname=cells[1].get_text(strip=True)
        afm=cells[2].get_text(strip=True)
        amka=cells[3].get_text(strip=True)
        stathero=cells[4].get_text(strip=True)
        kinito=cells[5].get_text(strip=True)
        email=cells[6].get_text(strip=True)
        dhmos=cells[7].get_text(strip=True)
        date=cells[8].get_text(strip=True)
        title=cells[9].get_text(strip=True)
        aae=cells[10].get_text(strip=True)
        aat=cells[11].get_text(strip=True)
        options=[]
        kayaslink="https://voucher.gov.gr"+cells[0].find("a", href=True).get("href")
        return [KAYAS,fullname,afm,amka,stathero,kinito,email,dhmos,
                date,title,aae,aat,options,kayaslink]

    def _makePpleList(self):
        for i in range(max(len(self.rows0), len(self.rows1))):
            
            try:
                data0=self._getRowData(self.rows0[i])
                self.costumers.add(*data0)
            except IndexError as ex: 
                pass

            try:
                data1=self._getRowData(self.rows1[i])
                self.costumers.add(*data1)
            except IndexError as ex:
                pass