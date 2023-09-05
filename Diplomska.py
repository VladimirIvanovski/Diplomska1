import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests as requests
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from bs4 import BeautifulSoup
#anhoch.com

def getLaptopsAnhoch():
    # URL of the website you want to scrape
    df = pd.DataFrame()

    df["name_of_laptop"] = ""
    df["price"] = ""
    df["photo_url"]= ""
    df["link_to_laptop_specs"]=""
    df["distributer"]=""
    index =0
    for i in range(1,6):
        url = f"https://www.anhoch.com/category/3003/prenosni-kompjuteri-laptopi#page/{i}/offset/64/"

        # Initialize the WebDriver with Chrome
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(4)
        page_source = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_source, "html.parser")
        # print(soup)
        li_tags = soup.find_all("li","span3 product-fix")

        # Loop through the <li> elements and print their content
        for li_tag in li_tags:
            try:
                # print(li_tag)
                name = li_tag.find("div", class_="product-name").text
                price = li_tag.find("span", class_="nm").text
                photo_url = str(li_tag.find("img", class_="products-img")['src'])
                href_link = li_tag.find("a")['href']

                proizvoditel = li_tag.findAll("strong")[1].text


                df.at[index,"name_of_laptop"] = name
                df.at[index, "price"] = str(price).replace(",","")
                df.at[index, "photo_url"] = photo_url
                df.at[index, "link_to_laptop_specs"] = href_link
                df.at[index, "distributer"] = proizvoditel
                # print("Name:", name)
                # print("Price:", price)
                # print("Photo URL:", photo_url)
                # print("Href Link:", href_link)
                # print("proizvoditel",proizvoditel)

            except:
                print("ne moze")
            index+=1


    df.to_csv("D:/Diplomska scraping/anhoch_database_laptops.csv",index=False)

def getPhonesAnhoch():
    # URL of the website you want to scrape
    df = pd.DataFrame()

    df["name_of_phone"] = ""
    df["price"] = ""
    df["photo_url"]= ""
    df["link_to_phone_specs"]=""
    df["distributer"]=""
    index =0
    for i in range(1,6):
        url = f"https://www.anhoch.com/category/3017/smartfoni-i-mobilni-tel#page/{i}/offset/64/"

        # Initialize the WebDriver with Chrome
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(4)
        page_source = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_source, "html.parser")
        # print(soup)
        li_tags = soup.find_all("li","span3 product-fix")

        # Loop through the <li> elements and print their content
        for li_tag in li_tags:
            try:
                # print(li_tag)
                name = li_tag.find("div", class_="product-name").text
                price = li_tag.find("span", class_="nm").text
                photo_url = str(li_tag.find("img", class_="products-img")['src'])
                href_link = li_tag.find("a")['href']

                proizvoditel = li_tag.findAll("strong")[1].text


                df.at[index,"name_of_phone"] = name
                df.at[index, "price"] = str(price).replace(",","")
                df.at[index, "photo_url"] = photo_url
                df.at[index, "link_to_phone_specs"] = href_link
                df.at[index, "distributer"] = proizvoditel
            except:
                print("ne moze")
            index+=1


    df.to_csv("D:/Diplomska scraping/anhoch_database_phones.csv",index=False)

def getLaptopsNeptun():
    df = pd.DataFrame()

    df["name_of_laptop"] = ""
    df["photo_url"] = ""
    df["link_to_laptop_specs"] = ""
    index = 0
    for i in range(1,3):
        url = f"https://www.neptun.mk/prenosni_kompjuteri.nspx?items=100&page={i}&priceRange=16999_183199"
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(3)
        page_source = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_source, "html.parser")


        products = soup.find_all('div',class_="ng-scope product-list-item-grid")

        for prod in products:
            try:
                df.at[index,"name_of_laptop"] = str(prod.find_next('h2').text).replace("Лаптоп ","")
                df.at[index, "regular_price"] = str(prod.findAllNext('span',class_="product-price__amount--value ng-binding")[1].text).replace(".","")
                df.at[index, "happy_price"] = str(prod.find_next('span',class_="product-price__amount--value ng-binding").text).replace(".","")
                df.at[index,"link_to_laptop_specs"]="https://www.neptun.mk/"+prod.find_next('a')['href']
                df.at[index,"photo_url"] = "https://www.neptun.mk/"+prod.find_next('img')['src']
                df.at[index,"discount_procentage"] = prod.find_next('span',class_="bb ng-binding").text
            except:
                print("couldnt find smthing")
            index+=1
    df.to_csv("D:/Diplomska scraping/neptun_database_laptops.csv",index=False)
def getPhonesNeptun():
    df = pd.DataFrame()

    df["name_of_phone"] = ""
    df["photo_url"] = ""
    df["link_to_phone_specs"] = ""
    index = 0
    for i in range(1,3):
        url = f"https://www.neptun.mk/mobilni_telefoni.nspx?items=100&page={i}&priceRange=1499_120999"
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(3)
        page_source = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_source, "html.parser")


        products = soup.find_all('div',class_="ng-scope product-list-item-grid")

        for prod in products:
            try:
                df.at[index,"name_of_phone"] = str(prod.find_next('h2').text).replace("Лаптоп ","")
                df.at[index, "regular_price"] = str(prod.findAllNext('span',class_="product-price__amount--value ng-binding")[1].text).replace(".","")
                df.at[index, "happy_price"] = str(prod.find_next('span',class_="product-price__amount--value ng-binding").text).replace(".","")
                df.at[index,"link_to_phone_specs"]="https://www.neptun.mk/"+prod.find_next('a')['href']
                df.at[index,"photo_url"] = "https://www.neptun.mk/"+prod.find_next('img')['src']
                df.at[index,"discount_procentage"] = prod.find_next('span',class_="bb ng-binding").text
            except:
                print("couldnt find smthing")
            index+=1
    df.to_csv("D:/Diplomska scraping/neptun_database_phones.csv",index=False)



def getLaptopsSettec():
    df = pd.DataFrame()

    index = 0
    for i in range(1, 4):
        url = f"https://setec.mk/index.php?route=product/category&path=10002_10003&limit=100&page={i}"
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(3)
        page_source = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_source, "html.parser")
        products = soup.find_all('div', class_="product clearfix product-hover")
        for product in products:
            try:
                df.at[index,"link_to_laptop_specs"] =product.find_next('a')['href']
                df.at[index, "name_of_laptop"] = product.find_next('img')['alt']
                df.at[index, "regular_price"] =product.find_next('span',class_='price-old-new').text
                df.at[index, "discount_price"] = product.find_next('span',class_='price-new-new').text
                df.at[index, "one_year_monthly"] = str(product.findAllNext('span', class_='klub-rata')[0].text) + " " + str(product.findAllNext('span',class_='klub-rata-suma')[0].text)
                df.at[index, "two_years_monthly"] = product.findAllNext('span', class_='klub-rata')[1].text + " " + product.findAllNext('span', class_='klub-rata-suma')[1].text
                df.at[index, "discount_procentage"] = product.find_next('div',class_='sale').text
                df.at[index, "link_to_photo"] = product.find_next('img')['data-echo']
            except:
                pass
            index+=1
    df.to_csv("D:/Diplomska scraping/setec_database_laptops.csv", index=False)

def getPhonesSettec():
    df = pd.DataFrame()

    index = 0
    for i in range(1, 4):
        url = f"https://setec.mk/index.php?route=product/category&path=10066_10067&limit=100&page={i}"
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(3)
        page_source = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_source, "html.parser")
        products = soup.find_all('div', class_="product clearfix product-hover")
        for product in products:
            try:
                df.at[index, "link_to_phones_specs"] = product.find_next('a')['href']
                df.at[index, "name_of_phone"] = product.find_next('img')['alt']
                df.at[index, "regular_price"] = product.find_next('span', class_='price-old-new').text
                df.at[index, "discount_price"] = product.find_next('span', class_='price-new-new').text
                df.at[index, "one_year_monthly"] = str(
                    product.findAllNext('span', class_='klub-rata')[0].text) + " " + str(
                    product.findAllNext('span', class_='klub-rata-suma')[0].text)
                df.at[index, "two_years_monthly"] = product.findAllNext('span', class_='klub-rata')[1].text + " " + \
                                                    product.findAllNext('span', class_='klub-rata-suma')[1].text
                df.at[index, "discount_procentage"] = product.find_next('div', class_='sale').text
                df.at[index, "link_to_photo"] = product.find_next('img')['data-echo']
            except:
                pass
            index += 1
    df = df.dropna(subset=['regular_price'], axis=0)
    df.to_csv("D:/Diplomska scraping/setec_database_phones.csv", index=False)




def statistical_analysis():
    # Define the file paths for the CSV files
    main_dataframe = pd.DataFrame()
    file_path_laptops1 = 'D:/Diplomska scraping/anhoch_database_laptops.csv'
    file_path_laptops2 = "D:/Diplomska scraping/neptun_database_laptops.csv"
    file_path_laptops3 = "D:/Diplomska scraping/setec_database_laptops.csv"

    file_path_phones1 = 'D:/Diplomska scraping/anhoch_database_phones.csv'
    file_path_phones2 = "D:/Diplomska scraping/neptun_database_phones.csv"
    file_path_phones3 = "D:/Diplomska scraping/setec_database_phones.csv"
    # Read the CSV files into dataframes
    df_laptops1 = pd.read_csv(file_path_laptops1)
    df_laptops2 = pd.read_csv(file_path_laptops2)
    df_laptops3 = pd.read_csv(file_path_laptops3)

    df_phones1 = pd.read_csv(file_path_phones1)
    df_phones2 = pd.read_csv(file_path_phones2)
    df_phones3 = pd.read_csv(file_path_phones3)

    main_dataframe.at[0,'Store']  = 'anhoch'
    main_dataframe.at[1,'Store'] = 'neptun'
    main_dataframe.at[2,'Store'] = 'setec'

    main_dataframe.at[0,'number_of_laptops'] = df_laptops1.shape[0]
    main_dataframe.at[1, 'number_of_laptops'] = df_laptops2.shape[0]
    main_dataframe.at[2, 'number_of_laptops'] = df_laptops3.shape[0]

    main_dataframe.at[0, 'number_of_phones'] = df_phones1.shape[0]
    main_dataframe.at[1, 'number_of_phones'] = df_phones2.shape[0]
    main_dataframe.at[2, 'number_of_phones'] = df_phones3.shape[0]

    column_stats1 = df_laptops1['price'].describe()
    column_stats2 = df_laptops2['happy_price'].describe()
    sum = 0
    for value in df_laptops3['discount_price']:
        sum +=int(str(value).replace(" Ден.","").replace(",",""))

    max =0
    min=999999999
    for value in df_laptops3['discount_price']:
        if(int(str(value).replace(" Ден.","").replace(",","")) > max):
            max=int(str(value).replace(" Ден.","").replace(",",""))
        if (int(str(value).replace(" Ден.", "").replace(",", "")) < min):
            min = int(str(value).replace(" Ден.", "").replace(",", ""))
        sum +=int(str(value).replace(" Ден.","").replace(",",""))

    # print(sum/df_laptops3.shape[0])

    column_stats4 = df_phones1['price'].describe()
    column_stats5 = df_phones2['happy_price'].describe()
    column_stats6 = df_phones3['discount_price'].replace(" Ден.","").describe()

    sum2 = 0
    max2=0
    min2=99999999
    for value in df_phones3['discount_price']:
        if (int(str(value).replace(" Ден.", "").replace(",", "")) > max2):
            max2 = int(str(value).replace(" Ден.", "").replace(",", ""))
        if (int(str(value).replace(" Ден.", "").replace(",", "")) < min2):
            min2 = int(str(value).replace(" Ден.", "").replace(",", ""))
        sum2 +=int(str(value).replace(" Ден.","").replace(",",""))

    main_dataframe.at[0, 'mean_price_laptops'] =  round(column_stats1['mean'],2)
    main_dataframe.at[1, 'mean_price_laptops'] =  round(column_stats2['mean'],2)
    main_dataframe.at[2, 'mean_price_laptops']=  round(sum/df_laptops3.shape[0],2)

    main_dataframe.at[0, 'mean_price_phones'] = round(column_stats4['mean'],2)
    main_dataframe.at[1, 'mean_price_phones'] = round(column_stats5['mean'],2)
    main_dataframe.at[2, 'mean_price_phones'] = round(sum2 / df_phones3.shape[0],2)

    main_dataframe.at[0, 'max_price_laptop'] = column_stats1['max']
    main_dataframe.at[1, 'max_price_laptop'] = column_stats2['max']
    main_dataframe.at[2, 'max_price_laptop'] = max

    main_dataframe.at[0, 'max_price_phone'] = column_stats4['max']
    main_dataframe.at[1, 'max_price_phone'] = column_stats5['max']
    main_dataframe.at[2, 'max_price_phone'] = max2

    main_dataframe.at[0, 'min_price_laptop'] = column_stats1['min']
    main_dataframe.at[1, 'min_price_laptop'] = column_stats2['min']
    main_dataframe.at[2, 'min_price_laptop'] = min

    main_dataframe.at[0, 'min_price_phone'] = column_stats4['min']
    main_dataframe.at[1, 'min_price_phone'] = column_stats5['min']
    main_dataframe.at[2, 'min_price_phone'] = min2

    main_dataframe.to_csv('D:/Diplomska scraping/statistics.csv',index=False)




def function_for_extracting(df_phones3):
    index = 0
    for value in df_phones3['name_of_laptop']:
        # Ram
        if str(value).__contains__("4GB"):
            df_phones3.at[index, 'RAM'] = "4"
        elif str(value).__contains__("8GB"):
            df_phones3.at[index, 'RAM'] = "8"
        elif str(value).__contains__("12GB"):
            df_phones3.at[index, 'RAM'] = "12"
        elif str(value).__contains__("16GB"):
            df_phones3.at[index, 'RAM'] = "16"
        elif str(value).__contains__("32GB"):
            df_phones3.at[index, 'RAM'] = "32"

        if str(value).__contains__("128GB"):
            df_phones3.at[index, 'Memory'] = "128"
        elif str(value).__contains__("256GB"):
            df_phones3.at[index, 'Memory'] = "256"
        elif str(value).__contains__("512GB"):
            df_phones3.at[index, 'Memory'] = "512"
        elif str(value).__contains__("1T"):
            df_phones3.at[index, 'Memory'] = "1"

        # if str(value).__contains__("128GB SSD"):
        #     df_phones3.at[index, 'MemorySSD'] = "128"
        # elif str(value).__contains__("256GB SSD"):
        #     df_phones3.at[index, 'MemorySSD'] = "256"
        # elif str(value).__contains__("512GB SSD"):
        #     df_phones3.at[index, 'MemorySSD'] = "512"
        # elif str(value).__contains__("1TB SSD"):
        #     df_phones3.at[index, 'MemorySSD'] = "1"
        index+=1
    df_phones3.to_csv('D:/Diplomska scraping/memory/anhoch_database_laptops_withRam.csv',index=False)



def extract_ram_and_memory():
    file_path_laptops1 = 'D:/Diplomska scraping/anhoch_database_laptops.csv'
    file_path_laptops2 = "D:/Diplomska scraping/neptun_database_laptops.csv"
    file_path_laptops3 = "D:/Diplomska scraping/setec_database_laptops.csv"

    file_path_phones1 = 'D:/Diplomska scraping/anhoch_database_phones.csv'
    file_path_phones2 = "D:/Diplomska scraping/neptun_database_phones.csv"
    file_path_phones3 = "D:/Diplomska scraping/setec_database_phones.csv"
    # Read the CSV files into dataframes
    df_laptops1 = pd.read_csv(file_path_laptops1)
    df_laptops2 = pd.read_csv(file_path_laptops2)
    df_laptops3 = pd.read_csv(file_path_laptops3)

    df_phones1 = pd.read_csv(file_path_phones1)
    df_phones2 = pd.read_csv(file_path_phones2)
    df_phones3 = pd.read_csv(file_path_phones3)

    # function_for_extracting(df_laptops1)
    function_for_extracting(df_laptops2)
    # function_for_extracting(df_laptops3)

    # df_laptops1.to_csv('D:/Diplomska scraping/memory/anhoch_database_laptops_withRam.csv',index=False)
    df_laptops2.to_csv('D:/Diplomska scraping/memory/neptun_database_laptops_withRam.csv', index=False)
    # df_laptops3.to_csv('D:/Diplomska scraping/memory/setec_database_laptops_withRam.csv', index=False)



async def fetch_url(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            html_content = await response.text()
            soup = BeautifulSoup(html_content, 'html.parser')
            return soup
        else:
            return None

async def gather_soup_from_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        soups = await asyncio.gather(*tasks)
        return soups


def scrape_links(df):
    urls_to_scrape = []
    for value in df['link_to_laptop_specs']:
        urls_to_scrape.append(value)

        # response = requests.get(value)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.find_all('meta')[5])
        # break
    loop = asyncio.get_event_loop()
    gathered_soups = loop.run_until_complete(gather_soup_from_urls(urls_to_scrape))
    index=0
    for ga in gathered_soups:
        if ga:
            try:
                if str(ga.find_all('div',class_='tab-content')[0]).__contains__("4GB"):
                    df.at[index,'RAM'] = "4"
                elif str(ga.find_all('div',class_='tab-content')[0]).__contains__("8GB"):
                    df.at[index,'RAM'] = "8"
                elif str(ga.find_all('div',class_='tab-content')[0]).__contains__("16GB"):
                    df.at[index,'RAM'] = "16"
                elif str(ga.find_all('div',class_='tab-content')[0]).__contains__("32GB"):
                    df.at[index,'RAM'] = "32"
                if str(ga.find_all('div',class_='tab-content')[0]).__contains__("256GB"):
                    df.at[index, 'Memory'] = "256"
                elif str(ga.find_all('div',class_='tab-content')[0]).__contains__("512GB"):
                    df.at[index, 'Memory'] = "512"

                elif str(ga.find_all('div', class_='tab-content')[0]).__contains__("1TB"):
                    df.at[index, 'Memory'] = "1"
                # print(ga.find_all('div',class_='tab-content')[0])
            except:
                pass
            index+=1
    df.to_csv('D:/Diplomska scraping/memory/setec_database_laptops_withRam.csv',index=False)


def correlation(df):
    # Calculate the correlation matrix for the selected columns
    df['discount_price'] = df['discount_price'].str.replace(' Ден.', '').str.replace(',','')

    # print(df['discount_price'])

    correlation_matrix = df[['RAM', 'Memory', 'discount_price']].corr()

    # Create a heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Heatmap (RAM, Memory, Price)")
    plt.show()


if __name__ == '__main__':
    # getLaptopsAnhoch()
    # getPhonesAnhoch()
    # getLaptopsNeptun()
    # getPhonesNeptun()
    # getLaptopsSettec()
    # getPhonesSettec()
    #statistical_analysis()

    #Baza celosna za anhoch setec neptun
    #column 1 broj na laptopi -
    #column 2 broj na telefoni -
    #column 3 average_price na laptopi -
    #columnd 4 average_price na telefoni -
    #column 5 average price na popust
    #column 6 regresijonalna povrzanost na cenata so ramot
    #column 7 regresiojanlna povrzanost na cenata so memorijata
    #column 8 median na site laptops
    #column 9 median na site phones
    #column 10 range na najeftin so najskap laptop
    #column 11 range na najeftin so najskap phone
    #column 12 max-min na laptop -
    #column 13 max-min na phone -

    #box plot za unusual prices on a laptop which stands out
    #histogram za koj standnuva out za laptopite ram/memorija/screensize



    #column 6 regresijonalna povrzanost na cenata so ramot
    #column 7 regresiojanlna povrzanost na cenata so memorijata Ovie vo boxplot i histogram da vidime korelacii

    # extract_ram_and_memory()

    urls_to_scrape = []
    # df = pd.read_csv("D:/Diplomska scraping/statistics.csv")

    # file_path_laptops1 = "D:/Diplomska scraping/memory/anhoch_database_laptops_withRam.csv"
    # file_path_laptops2 = "D:/Diplomska scraping/memory/neptun_database_laptops_withRam.csv"
    file_path_laptops3 = "D:/Diplomska scraping/memory/setec_database_laptops_withRam.csv"

    # df_laptops1 = pd.read_csv(file_path_laptops1)
    # df_laptops2 = pd.read_csv(file_path_laptops2)
    df_laptops3 = pd.read_csv(file_path_laptops3)

    # correlation(df_laptops1)
    # correlation(df_laptops2)
    correlation(df_laptops3)


    # summary_stats = df.describe()
    # plt.figure(figsize=(10, 6))
    # plt.bar(df['Store'], df['mean_price_laptops'], label='Mean Laptop Price')
    # plt.bar(df['Store'], df['mean_price_phones'], label='Mean Phone Price', alpha=0.5)
    # plt.xlabel('Store')
    # plt.ylabel('Mean Price')
    # plt.title('Mean Prices of Laptops and Phones by Store')
    # plt.legend()
    # plt.show()
    #
    # # Box plots for max prices of laptops and phones
    # plt.figure(figsize=(10, 6))
    # plt.boxplot([df['max_price_laptop'], df['max_price_phone']], labels=['Max Laptop Price', 'Max Phone Price'])
    # plt.ylabel('Price')
    # plt.title('Distribution of Max Prices of Laptops and Phones')
    # plt.show()
    # print(summary_stats)