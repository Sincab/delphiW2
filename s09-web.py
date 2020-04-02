# # # # from urllib.request import urlopen
# # # # my_address = "http://www.staff.city.ac.uk/~ddimak/python/practice/Profile_Aphrodite.htm"
# # # # html_page = urlopen(my_address)
# # # # html_text = html_page.read().decode('windows-1252')
# # # # print(html_text)
# # #
# # # from urllib.request import urlopen
# # # my_address = "http://www.staff.city.ac.uk/~ddimak/python/" \
# # #              "practice/Profile_Aphrodite.htm"
# # # html_page = urlopen(my_address)
# # # html_text = html_page.read().decode('windows-1252')
# # # start_tag = "<title>"
# # # end_tag = "</title>"
# # # start_index = html_text.find(start_tag) + len(start_tag)
# # # end_index = html_text.find(end_tag)
# # # print(html_text[start_index:end_index])
# #
# # from urllib.request import urlopen
# # my_address = "http://www.staff.city.ac.uk/~ddimak/python/" \
# #              "practice/Profile_Poseidon.htm"
# # html_page = urlopen(my_address)
# # html_text = html_page.read().decode('windows-1252')
# # start_tag = "<title>"
# # end_tag = "</title>"
# # start_index = html_text.find(start_tag) + len(start_tag)
# # end_index = html_text.find(end_tag)
# # print(html_text[start_index:end_index])
#
# my_string = "This is very boring"
# print(my_string.replace('boring', 'funny'))
# import re
# print(re.sub('boring', 'WHAT?', my_string))

import re
from urllib.request import urlopen
my_address = "http://www.staff.city.ac.uk/~ddimak/python/practice/Profile_Dionysus.htm"
html_page = urlopen(my_address)
html_text = html_page.read().decode('windows-1252')
match_results = re.search("<title .*?>.*</title .*?>", html_text, re.IGNORECASE)
title = match_results.group()
print(title)
title = re.sub("<.*?>", "", title)
print(title)