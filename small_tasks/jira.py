# from playwright.sync_api import sync_playwright, expect
# from bs4 import BeautifulSoup
# from lxml import etree
# from scrapy import Selector
#
# email = "abdelrahmanabbas@rentola.com"
# gmail_password = "tVjV.>22Z<;#`$a^"
# spidernest_pass = "abbas101"
#
#
# # headless=False, slow_mo=50
# def open_jira():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=50)
#         # browser = p.chromium.launch()
#
#         context = browser.new_context()
#         page = context.new_page()
#         page.set_default_timeout(40000)
#

        # login with Google account
        # page.goto("https://id.atlassian.com/login")
        # page.get_by_role("button", name="Continue with Google").click()
        #
        # # Entering the email
        # page.fill('//input[@type="email"]', "abdelrahmanabbas@rentola.com")
        # page.get_by_role('button', name='Weiter').click()
        #
        # # # Enter the password
        # page.get_by_role("button", name="Weiter").is_visible()
        #
        # page.fill('//input[@type="password"]', "tVjV.>22Z<;#`$a^")
        # page.get_by_role("button", name="Weiter").click()
        #
        # page.get_by_role("link", name="Spider Fixing and Rebuiliding Jira").locator("button").click()
        #
        # page.locator('//input[@data-test-id="search-dialog-input"]').click(timeout=20000)
        # page.get_by_placeholder("Search Jira").fill("wrong amenities")
        # page.get_by_placeholder('Search Jira').press("Enter")
        #
        # page.get_by_role("button", name="Status: All").click()
        # page.get_by_role("option", name="Q&A").get_by_text("Q&A").click(timeout=30000)

#         page.get_by_role("button", name="Project: All").click()
#         page.get_by_role("list", name="Recent projects").get_by_role(
#             "option", name="Spider Fixing and Rebuiliding (SFR)").click(timeout=20000)
#
#         return page.content()
#
#
# def scrape_html(source_code):
#     issues = {}
#     select = Selector(text=source_code)
#     counter = 0
#     tickets = select.xpath('//ol[@class="issue-list"]/li')
#     for ticket in tickets:
#         title = ticket.xpath('./@title').get()
#         domain_name = title.split(']')[0].replace("[",'')
#         issue_link = ticket.xpath('./@data-key').get()
#         issues[issue_link] = {title,domain_name}
#         counter += 1
#
#     issues['total_tickets'] = counter
#     return issues
#
#
# page_source = open_jira()
# domains = scrape_html(page_source)
#
# print(domains)

