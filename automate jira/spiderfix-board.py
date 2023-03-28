import json
import re

from playwright.sync_api import sync_playwright
from scrapy import Selector

email = "abdelrahmanabbas@rentola.com"
gmail_password = "tVjV.>22Z<;#`$a^"


# spidernest_pass = "abbas101"

def main(search_patterns):
    jira_page_source = open_jira(email, gmail_password, search_pattern)
    jira_tickets_content = tickets_content(jira_page_source)

    return jira_tickets_content


# headless=False, slow_mo=50
def open_jira(user_name, password, pattern):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        page = context.new_page()

        # browser = p.chromium.launch(headless=True, slow_mo=50)
        # page = browser.new_page()

        # login with Google account
        page.goto("https://id.atlassian.com/login", wait_until="networkidle")
        page.get_by_role("button", name="Continue with Google").click()

        # Entering the email
        page.fill('//input[@type="email"]', user_name)
        page.get_by_role('button', name='Weiter').click()

        # # Enter the password
        page.fill('//input[@type="password"]', password)
        page.get_by_role("button", name="Weiter").click()

        # Go to SPIDER FIX BOARD && wait until loading
        page.get_by_role("link", name="Spider Fixing and Rebuiliding Jira").locator("button").click()
        page.wait_for_load_state()

        # Search for specific issue like wrong amenities in {Spider Fixing and Rebuiliding}
        page.locator('//input[@data-test-id="search-dialog-input"]').click()
        page.get_by_placeholder("Search Jira").fill(pattern)
        page.get_by_label("Spider Fixing and Rebuiliding").check()

        page.get_by_placeholder('Search Jira').press("Enter")
        page.wait_for_load_state()

        # QA column
        page.get_by_role("button", name="Status: All").click()
        page.get_by_label("Q&A").check()
        page.get_by_role("listitem").filter(has_text="Search").get_by_role("button", name="Search").click()
        page.wait_for_load_state()

        page_source = page.content()

        # ---------------------
        context.close()
        browser.close()

        return page_source


def tickets_content(source_code):
    all_tickets = {}
    select = Selector(text=source_code)
    counter = 0
    tickets = select.xpath('//ol[@class="issue-list"]/li')
    for ticket in tickets:
        title = ticket.xpath('./@title').get()
        domain_name = re.findall("(\[+.*\]+)", title)
        if domain_name:
            domain_name = domain_name[0].replace("[", '').replace(']', '')

        issue_link = ticket.xpath('./@data-key').get()
        all_tickets[issue_link] = {
            "ticket title": title,
            "domain": domain_name
        }

        counter += 1

    # all_tickets['total_tickets'] = counter
    with open("out_put_files/Q&A.json", "w+") as file:
        json.dump(all_tickets, file)

    return all_tickets


# def main(search_pattern: list):
#     for pattern in search_pattern:
#         page_source = open_jira(pattern)
#         domains = scrape_html(page_source)
#


if __name__ == "__main__":
    search_pattern = "images less than"
    x = main(search_pattern)
    print(x)
