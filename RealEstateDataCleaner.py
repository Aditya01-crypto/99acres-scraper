import os
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
from RealEstatelogger import logger


def data_to_excel(position):
    #lists to hold data
    building=[]
    fullPrice=[]
    bedRoomHouseAndFloor=[]
    pricePerSqft=[]
    location=[]
    linksToSite=[]
    summarizedInfo=[]

    with open('outputdata.txt','r',encoding='utf-8') as f:
        content=f.read()

    soup=BeautifulSoup(content,'lxml')


    card1=soup.find_all("div",class_="tupleNew__contentWrap")

    for card in card1:
        build_name=card.select('div[class*="tupleNew__locationName"]')
        for b in build_name:
            data=(b.text.strip())
            building.append(data)
        full_price=card.find_all("div",class_="tupleNew__priceValWrap")
        data_list=[]
        for fp in full_price:
            data=(fp.text.strip())
            data_list.append(data)
        fullPrice.append(", ".join(d for d in data_list))

        sqft_price=card.select('div[class*="tupleNew__perSqftWrap"]')
        data_list=[]
        for sqp in sqft_price:
            data=(sqp.text.strip())
            data_list.append(data)
        pricePerSqft.append(", ".join(d for d in data_list))

        bhks=card.select('span[class="tupleNew__area1Type"]')
        data_list=[]
        for bhk in bhks:
            data=(bhk.text.strip())
            data_list.append(data)
        bedRoomHouseAndFloor.append(", ".join(d for d in data_list))

        loc=card.select('p[data-label="DESCRIPTION"]')
        data_list=[]
        for l in loc:
            data=(l.text.strip())
            data_list.append(data)
        location.append(", ".join(d for d in data_list))

        links=card.find_all(class_="tupleNew__propertyHeading")
        for link in links:
            data=(link.get('href'))
            linksToSite.append(data)
        summary=card.select('a[class*="tupleNew__propertyHeading"]')
        for s in summary:
            data=(s.get('title'))
            summarizedInfo.append(data)

    #FOR 
    card2=soup.find_all("div",class_="PseudoTupleRevamp__contentWrapAb")

    for card in card2:
        build_name=card.select('div[class*="PseudoTupleRevamp__headNrating"] a')
        for b in build_name:
            data=(b.text.strip())
            building.append(data)

        full_price=card.find_all("div",class_="configs__ccl2")
        data_list=[]
        for fp in full_price:
            data=(fp.text.strip())
            data_list.append(data)
        fullPrice.append(", ".join(d for d in data_list))

        pricePerSqft.append('N/A')# TYpe 2 Cards doesn't have  price per sqft which makes hte majority of  the site content

        bhks=card.select('div[class="configs__ccl1"]')
        data_list=[]
        for bhk in bhks:    
            data=(bhk.text.strip())
            data_list.append(data)
        bedRoomHouseAndFloor.append(", ".join(d for d in data_list))

        loc=card.select('div[class="tupleNew__onlyNearby"]')
        data_list=[]
        for l in loc:
            data=(l.get_text(strip=True,separator=" "))
            data_list.append(data)
        location.append(", ".join(d for d in data_list))

        links=card.select('div[class="PseudoTupleRevamp__headNrating"] a')
        for link in links:
            data=(link.get('href'))
            linksToSite.append(data)

        summary=card.select('h2[class="PseudoTupleRevamp__subHeading ellipsis PseudoTupleRevamp__projectHeading"]')
        for s in summary:
            data=(s.get_text(strip=True,separator=" "))
            summarizedInfo.append(data)

    #USED FOR DEBUGGING PURPOSE
    # print("Building List ", building)
    # print("Price",fullPrice)
    # print('price per sqft',pricePerSqft)
    # print('bhk',bedRoomHouseAndFloor)
    # print('location',location)
    # print('links',linksToSite)
    # print('summary',summarizedInfo)

    logger.info("---------Length of Data ----------")
    logger.info(f"Building List   {len(building)}")
    logger.info(f"Price {len(fullPrice)}")
    logger.info(f'price per sqft {len(pricePerSqft)}')
    logger.info(f'bhk {len(bedRoomHouseAndFloor)}')
    logger.info(f'location {len(location)}')
    logger.info(f'links {len(linksToSite)}')
    logger.info(f'summary {len(summarizedInfo)}')


    df = pd.DataFrame({
        "Building Name": building,
        "Full Price": fullPrice,
        "Price per Sqft": pricePerSqft,
        "BHK": bedRoomHouseAndFloor,
        "Location": location,
        "Link": linksToSite,
        "Summary": summarizedInfo
    })

    #filling empty values with 'N/A'
    df = df.replace(r'^\s*$', None, regex=True).fillna('N/A')

    filename = datetime.now().strftime(f"%Y%m%d_%H%M%S_{position}_RealEstateData") + ".xlsx"
    logger.debug("Filling empty values with 'N/A' ")
    logger.debug(f"Filename: {filename}")
    df.to_excel(f"{filename}", index=False)
    logger.info(f"Excel file saved as {filename}!")

