from app import app, db
from app.models import Tracker
from lxml import html
import requests


def main()


def brPath(tree):
    # create single-element list from class attribute
    # check to see if the markdown-specific attribute exists
    sale = tree.xpath('//*[@id="product"]'
        '/div[2]/div[1]/div[1]/div[2]/h5[1]/@class')

    # print('Test: ', sale[0])

    if 'markdown' in scrape_sale_status(url):
        return True
    else:
        return False


def exPath(tree):
    # create single-element list from class attribute
    # check to see if the markdown-specific attribute exists


def jcPath(tree):
    # create single-element list from class attribute
    # check to see if the markdown-specific attribute exists


def nsPath(tree):
    # create single-element list from class attribute
    # check to see if the markdown-specific attribute exists



def scrape_sale_status(vendor, url):
    # get page content and convert to tree format
    page = requests.get(url)
    tree = html.fromstring(page.content)

    vendor_paths = {'Banana Republic' : brPath,
                    'Express' : exPath,
                    'J.Crew' : jcPath,
                    'Nordstrom' : nsPath,
                    }

    return vendor_paths[vendor](tree)



def main():
    print(scrape_sale_status('http://bananarepublic.gap.com/browse/product.do?cid=26222&vid=1&pid=480008012'))

if __name__ == '__main__':
    main()