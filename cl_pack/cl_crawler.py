import os
import sys

# Test after changing username.

# Make the URL
def create_url(location, domain, ext):
    url = "https://" + location + "." + domain + "." + ext
    return url


# Create a new directory for each website.
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Que for links and crawled files (so that a link is not crawled twice).
def create_data_files(project_name, base_url):

    # List of links that need to be crawled.
    queue = project_name + 'queue.txt'

    # Links that have been crawled.
    crawled = project_name + 'crawled.txt'


if len(sys.argv) < 5:
    print('Choose a city and item to search for.')

else:
    for i in range (0, len(sys.argv)):
        if sys.argv[i] == '-c':
            city = sys.argv[i + 1]
            print('City: ' + city)

        elif sys.argv[i] == '-i':
            item = sys.argv[i + 1]
            print('Item: ' + item);

address = create_url(city, 'craigslist', 'org')
print('Address: ' + address)
