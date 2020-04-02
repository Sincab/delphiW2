# import mechanicalsoup
#
# my_browser = mechanicalsoup.Browser(
#                  soup_config={'features':'html.parser'})
# page = my_browser.get("http://www.staff.city.ac.uk/~ddimak/python/" \
#            "practice/Profile_Aphrodite.htm")
# print(page.soup)

import mechanicalsoup

my_browser = mechanicalsoup.Browser(
    soup_config={'features':'html.parser'})
login_page = my_browser.get(
    "https://whispering-reef-69172.herokuapp.com/login")
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "admin"
form.select("input")[1]["value"] = "default"

# form.select("input")[0]["value"] = "sinan"
# form.select("input")[1]["value"] = "selcuk \n asdsdasdf"

profiles_page = my_browser.submit(form, login_page.url)
print(profiles_page.url)
print(profiles_page.soup)

## TRY TO SUBMIT THE FORM
# testwrite = my_browser.get(profiles_page.url)
# test_html = testwrite.soup
#
# form = login_html.select("form")[0]
# form.select("input")[0]["value"] = "sinan"
# form.select("input")[1]["value"] = "selcuk \n asdsdasdf"
# profiles_page = my_browser.submit(form, login_page.url)