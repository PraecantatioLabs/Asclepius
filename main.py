from requests_html import HTMLSession

session = HTMLSession()
r = session.get("https://www.nyp.org/hudsonvalley/patients-and-visitors/charges")
pricing = r.html.find("body > div.fill > div > div.col-sm-8.noleftpad > div:nth-child(3) > div > div > div")[0]
# print(pricing)
categories = pricing.find("h3")
pricing_table = pricing.find("table")
for i in zip(categories, pricing_table): 
    # format of i: (categories, pricing_table)
    # i[0] is categories
    # Prints list of Categories
    print("\n\n\n" +  "=== Start of " + i[0].text + " ===" + "\n\n\n")
    # Gets list of tds in row
    for j in i[1].find("tr"):
        # Gets list of text nodes in body which may or may not be in a strong tag
        k_iter = iter(j.find("td"))
        for k in k_iter:
        # Handle first row
            l = k.find("strong")
            if l:
                print(l[0].text + " " + next(k_iter).find("strong")[0].text)
            else:
                print (k.text + " " + next(k_iter).text)
                # print(k[0] + k[1] + "\n")
    print("\n\n\n" + "=== End of " + i[0].text + " ===")

import datetime
print("\nInformation fetched on: " + str(datetime.datetime.now()))




