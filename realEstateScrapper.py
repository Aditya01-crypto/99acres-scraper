from playwright.async_api  import async_playwright
import logging
import os
from bs4 import BeautifulSoup
import asyncio
import random
from playwright_stealth import Stealth
from RealEstatelogger import logger
from RealEstateDataCleaner import data_to_excel

async def human_like_mouse_movement(page,start_x=None,start_y=None,duration=1.5):
    start=asyncio.get_event_loop().time()
    if start_x is None:
        start_x =random.randint(200,500)
    if start_y is None:
        start_y=random.randint(200,500)
    
    await page.mouse.move(start_x,start_y)

    while asyncio.get_event_loop().time()-start<duration:
        start_x+=random.randint(-15,15)
        start_y+=random.randint(-15,15)
        await page.mouse.move(start_x,start_y,steps=random.randint(1,4))
        await asyncio.sleep(random.uniform(0.005,0.05))

    await asyncio.sleep(random.uniform(0.15, 0.35))  
    

async def human_like_scroll(page,max_scroll=20):
    """Scroll like a human """
    for i in range(max_scroll):
        scroll_amount=random.randint(200,900)
        increments=random.randint(3,7)
        per_scroll=scroll_amount//increments

        for _ in range(increments):
            await page.evaluate(f'window.scrollBy(0, {per_scroll})')
            await asyncio.sleep(random.uniform(0.05,0.15))

        delay=random.uniform(0.3,2)
        logger.info(f"Scrolled {i+1}/{max_scroll} , waiting till {delay:.1f}s")
        await asyncio.sleep(delay)
        if random.random()<0.3:
            read_time=random.uniform(3,8)
            logger.info(f"Reading for {read_time:.1f}s")
            await asyncio.sleep(read_time)
        if random.random()<0.35:
            await human_like_mouse_movement(page,duration=random.uniform(0.5,1.5))



async def main(loc,scroll=20,no_gui=False):
    url=r"https://www.99acres.com/"

    async with Stealth().use_async(async_playwright()) as p:#setup
        
        browser= await p.chromium.launch(headless=no_gui)

        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1920, 'height': 1080},
            locale='en-IN',  # Indian locale for 99acres
            timezone_id='Asia/Kolkata',
            geolocation={'latitude': 12.9716, 'longitude': 77.5946},  # Bangalore
            permissions=['geolocation']
            )

        page= await context.new_page()
        await page.goto(url)
        logger.info(f"Navigating to {page.url}")

        await page.wait_for_load_state('networkidle',timeout=10000)
        search_box= page.locator('#inPageSearchForm')

        search_bar= page.locator('input[name="keyword"]')


        if await search_bar.count()>0:
            await search_bar.nth(1).fill(loc)
            logger.info("Search Bar Found, Filled the location")
        else:
            logger.error("Search Bar not found , can't run the scraper ")
            logger.debug("Search Bar not found")
            return
        
        search_suggestion=page.locator('.component__suggestor').locator('ul#suggestions_custom').first
        await search_suggestion.wait_for(state='visible')
        await search_suggestion.locator('li').first.click()
        

        
        async with page.expect_navigation():        
            await page.locator('#searchform_search_btn').first.click()
            logger.info(f"Navigated to new page : {page.url}")

        await page.wait_for_load_state('networkidle')

        content_box=page.locator('div[data-label="SEARCH"]')
        await content_box.wait_for(timeout=15000)

        await human_like_scroll(page,max_scroll=scroll)

        await asyncio.sleep(3)
        
        html=await page.content()

        if html:
            logger.info("Html Content Found")
            soup = BeautifulSoup(html,'lxml')

            with open('outputdata.txt','w',encoding='utf-8') as f:
                f.write(soup.prettify())

        else:
            logger.error("HTML CONTENT NOT FOUND")

        await browser.close()

    data_to_excel(loc)

if __name__=="__main__":    
    asyncio.run(main('Pune'))
    