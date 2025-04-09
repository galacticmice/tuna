import requests
from bs4 import BeautifulSoup
import csv

query = input("Enter search query to scrape: ")
print('\n')

# We need to use "html.duckduckgo.com/html" because the javascript can cause problems otherwise
url = f"https://html.duckduckgo.com/html/?q={query}"

# This prompts a get request to the specified "url" which returns an HTML response
getRequestResponse = requests.get(url)

soup = BeautifulSoup(getRequestResponse.text, "html.parser")

# An array to store the results of each output from the parsing. Or "list" I suppose 😒
results = []

# BeautifulSoup searched for <a> tags in the HTML which define hyperlinks (for search results)
# Specifically, all <a> tags with with the class result__a (the clickable search titles)
for link in soup.select("a.result__a"):
    # This grabs the "link text" or the title of the search results (search headlines)
    title = link.text

    # In HTML is used to define the hyperlink URL
    # For each element <a> grab the corresponding URL attributed to the search result headline
    href = link.get("href")

    # APPEND ONLY TAKES 1 PARAMETER
    # We are grouping "title" and "href" to a single index in the list.
    # The [] creates a new "mini" list within the list so one index points to another list containing both elements
    # To access the title we would use [i][0]. Conversely, the href is stored in [i][1]
    results.append([title, href])

    # Print the output the current title and href in the loop to terminal
    # print(f"{title} - {href}")

    print(f"{title}\n{href}\n")

# Save the output to a CSV
# open(open/create filename.csv, write, newline rule) # new line is \n, so the CSV saves with LF line endings
with open(f"search-{query}.csv", "w", newline="\n") as f:
    # Initialize the writer object to writer and writes to "f", the csv file
    # lineterminator needed to force LF file type
    writer = csv.writer(f, lineterminator='\n')

    # First write the header row to specify the column headers
    writer.writerow(["Search-Query", "URL"])

    # From the results list, write each element (mini lists) to a row. Lists print with command and are already delimited by commas, so no need to specify delimiter.
    writer.writerows(results)

print(f"Search results for '{query}' saved to search-{query}.csv")
