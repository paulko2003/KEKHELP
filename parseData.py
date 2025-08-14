from bs4 import BeautifulSoup
class parseData:
    def __init__(self):
        pass 

    def getPeople(self, html:str):
        soup = BeautifulSoup(html, "html.parser")
        self.rows0 = soup.find_all("tr", class_="row0")
        self.rows1 = soup.find_all("tr", class_="row1")
        return self._makePpleList()
        
    def _makePpleList(self):
        print(len(self.rows0), len(self.rows1))
        people=list()
        try:
            for i in range(max(len(self.rows0), len(self.rows1))):
                cells0= self.rows0[i].find_all("td", class_=["cell_num_0", "cell_num_1"])
                cells1= self.rows1[i].find_all("td", class_=["cell_num_0", "cell_num_1"])
                people.append(["https://voucher.gov.gr"+cells0[0].find("a", href=True).get("href"),cells0[1].get_text(strip=True)])
                people.append(["https://voucher.gov.gr"+cells1[0].find("a", href=True).get("href"),cells1[1].get_text(strip=True)])
        except IndexError: 
            print("lol")
        return people
        