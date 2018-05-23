import os


# Create a new file.
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Create a new directory for each website.
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Que for links and crawled files (so that a link is not crawled twice).
def create_data_files(project_name, base_url):

    # List of links that need to be crawled.
    queue = project_name + '_queue.txt'

    # Links that have been crawled.
    crawled = project_name + '_crawled.txt'

    # Make the queue file if it does not exist.
    if not os.path.isfile(queue):
        write_file(queue, base_url)

    # Make the crawled file if it does not exist.
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Append data to existing file.
def append_to_file(path, data):