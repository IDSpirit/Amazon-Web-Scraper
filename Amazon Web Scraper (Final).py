from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import time

#my_url = 'https://www.amazon.co.uk/s?k=nintendo+switch+games&crid=1EYFS6XS0SBTZ&sprefix=nintendo%2Caps%2C339&ref=nb_sb_ss_i_3_8'

#https://medium.com/@pknerd/write-your-first-web-scraper-in-python-with-beautifulsoup-564dddd8693c
#https://medium.com/python-pandemonium/6-things-to-develop-an-efficient-web-scraper-in-python-1dffa688793c

def main():

    my_url = str(input("Paste the Amazon link you want to see the products of: "))

    #Opening up connection, grabbing the page
    print("\n")
    
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    #html parser
    page_soup = soup(page_html, "html.parser")

    #Grabs each product
    containers = page_soup.findAll("div", {"class":"sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"}) #I think this creates a list of each product

    #print(containers)

    i = 0
    len_title_container = 5 #This is just here to define the variable len_title_container since im using it for the "while" loop below, the actual value of the variable is defined during the loop

    for container in containers:
    
        divWithInfo = container.findAll("div", "a-link-normal a-text-normal")

        #print(divWithInfo)
        #num_products = len(container)

        while i != len_title_container:
        #    try:
        #        brand = divWithInfo[i].span.text
        #    except:
        #        brand = "No Brand"

            title_container = container.findAll("a", {"class":"a-link-normal a-text-normal"})
            #print(len_title_container)
            len_title_container = len(title_container)
            #print(len_title_container)
            #print(i)
            product_name = title_container[i].text

            #print(product_name)

            price_container = container.findAll("a", {"class":"a-size-base a-link-normal s-no-hover a-text-normal"})

            #print(price_container)
            
            #price_container = price_container[i].span.span

            #####print(price_container)

            try:
                product_price = price_container[i].text.strip()
            except:
                break

            full_stop = product_price.find(".")

            #print(full_stop)

            num_full_stops = product_price.count(".")

            #print(num_full_stops)

            if num_full_stops != 1:
                product_price = product_price[0:int(full_stop+3)]

            #print(product_price)

        
#
        #product_price.find('Offer')       
#
        
        
        #product_price = re.findall('\d+', product_price)
        #product_price = product_price[0:2]

        #try:
        #    product_price = int(product_price[0]) + int(product_price[1])/100

        #except:
        #    product_price = "Request Price"
            i += 1

            #print("Brand: " + brand)
            print("Product Name: " + product_name)
            if product_price == "":
                print("Product Price: Request Price From Website")
            else:
                print("Product Price: " + str(product_price) + "\n-----------------------------------------------------\n")

        i = 0
        len_title_container = 5
    asking()

def asking():
    retry = str(input("\n\nWould you like to see some products on Amazon without all the sponsored links and recommendations? (1 for yes and 2 for no): "))
    if retry == "1":
        print("\n")
        main()
    elif retry == "2":
        quit()
    elif retry != "1" and retry != "2":
        print("\nError, incorrect input. Please try again")
        time.sleep(2)
        asking()

asking()
