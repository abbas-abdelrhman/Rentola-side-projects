import json
from scrapy import Selector

from playwright.sync_api import sync_playwright

email = "abdelrahmanabbas@rentola.com"
spider_nest_pass = "abbas101"


def read_html(source, jira_ticket):
    selector = Selector(text=source)
    name = selector.xpath('//table[@class="table"]//tr/td[9]/text()').getall()
    domain = selector.xpath('//table[@class="table"]//tr/td[2]/a/text()').get()

    with open('out_put_files/out_text.txt', "a+") as file:
        file.write(f"https://rentola-dev.atlassian.net/browse/{jira_ticket}  |  {domain}  | {name} \n")

    if not domain:
        return None

    else:
        return True


def open_spider_nest():
    with sync_playwright() as nest:
        browser = nest.chromium.launch(headless=True, slow_mo=50)
        page = browser.new_page()

        # open spider nest and login
        page.goto("https://c.findboliger.dk/users/sign_in")

        # enter email
        page.locator('//input[@type="email"]').click()
        page.fill('//input[@type="email"]', email)

        # enter password
        page.locator('//input[@type="password"]').click()
        page.fill('//input[@type="password"]', spider_nest_pass)

        page.locator('//input[@type="submit"]').click()

        # read domains name from the json file
        with open('Q&A.json', "r") as file:
            data = json.load(file)

        # loop through domains and read its details
        for keys, values in data.items():
            domain = values.get("domain", 0)
            jira_ticket = keys

            page.goto("https://c.findboliger.dk/spider_details")
            page.locator('//input[@id="spider_detail_domain"]').click()
            page.fill('//input[@id="spider_detail_domain"]', domain)

            page.locator('//input[@type="submit"]').click()
            page.is_visible("Status")
            x = read_html(page.content(), jira_ticket)

            if x:
                page.locator('//a[@title="View Submissions"]').click()
                page.is_visible("Name")

                print("it should not be none", domain)
            else:
                print("this is none domain", domain)


open_spider_nest()
