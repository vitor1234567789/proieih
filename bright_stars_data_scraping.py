from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# URL de dados de brilho das estrelas da Wikipedia
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scarped_data = []


# Defina o método de coleta de dados
def scrape():
               
        # Objeto BeautifulSoup
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # MUITO IMPORTANTE: A classe "wikitable" e os dados <tr> são os existentes no momento da criação deste código. 
        # Isso pode ser atualizado no futuro, pois a página é atualizada pela Wikipedia. 
        # Entenda a estrutura da página conforme discutido na aula e execute a coleta de dados do zero.

        # Localize <table>
        bright_star_table = soup.find("table", attrs={"class", "wikitable"})
        
        # Localize <tbody>
        table_body = bright_star_table.find('tbody')

        # Localize <tr>
        table_rows = table_body.find_all('tr')

        # Obtenha os dados de <td>
        for row in table_rows:
            table_cols = row.find_all('td')
            # print(table_cols)
            
            temp_list = []

            for col_data in table_cols:
                # Imprimir somente colunas de dados textuais usando a propriedade ".text"
                # print(col_data.text)

                # Remova os espaços em branco extras usando o método strip()
                data = col_data.text.strip()
                # print(data)

                temp_list.append(data)

            # Anexe os  dados à lista star_data
            scarped_data.append(temp_list)


       
# Chamando o método    
scrape()

################################################################

# Importe os dados para CSV

stars_data = []


for i in range(0,len(scarped_data)):
    
    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

print(stars_data)


# Defina o cabeçalho
headers = ['Star_name','Distance','Mass','Radius','Luminosity']  

# Defina o dataframe do pandas
star_df_1 = pd.DataFrame(stars_data, columns=headers)

# Converta para CSV
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
