from bs4 import BeautifulSoup as bs
import re

a = '''<td class="availabiItm">
																							Кассы
											
																					</td>'''

soup = bs(a, "lxml")
#print(soup)
subbed = re.sub("\n|\t", '', soup.string)
print(subbed)
