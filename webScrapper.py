import requests
from bs4 import BeautifulSoup
from xlwt import Workbook

wb = Workbook()                     #creating a workbook
sheet1 = wb.add_sheet('Sheet1')     #adding sheet to the workbook
sheet1.write(0, 0, "Name")
sheet1.write(0, 1, "Rating")        #sheetVar.write(row, column, value)
sheet1.write(0, 2, "Price")

def spider():
    titles = []
    ratings = []
    dPrices = []
    aPrices = []
    url = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    sourceCode = requests.get(url)                           #gets the response
    plain_text = sourceCode.text                             #to get the content

    soup = BeautifulSoup(plain_text, "html.parser")           #to initialise the parser

    for link in soup.findAll('div', {'class': '_4rR01T'}):    # to get all the attributes of an object print(dir(obj))
        title = link.string                                   #soup.findAll() returns all the matched elements within a list
        titles.append(title)

    for link in soup.findAll('div', {'class': '_3LWZlK'}):
        rating = link.text
        ratings.append(rating)

    for link in soup.findAll('div', {'class': '_30jeq3 _1_WHN1'}):
        dPrice = link.string
        dPrices.append(dPrice)

    # for link in soup.findAll('div', {'class': '_3I9_wc _27UcVY'}):
    #     aPrice = link.text
    #     aPrices.append(aPrice)

    for i in range(len(titles)):
        print(titles[i] + "   " + ratings[i]  + "  " + dPrices[i])

    for i in range(1, len(titles)):
        sheet1.write(i, 0, titles[i])       #sheetVar.write(row, column, value)
        sheet1.write(i, 1, ratings[i])
        sheet1.write(i, 2, dPrices[i])

    # wb.save('C:\\Users\\path\\filename')   #workbookVar.save(fileName)
    wb.save('flipkartGadgets.xls')

spider()