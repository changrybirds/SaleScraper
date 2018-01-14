'''Dev notes 2018-01-14:
- XPath currently returning empty lists for Express and J.Crew
- Suspect it could be due to certain elements being generated w/ JavaScript
- Should test out alternative solutions like Selenium or PhantomJS instead of lxml'''

# Imports needed for parsing
from lxml import etree, html
import requests


def __brPath(tree):
    # create single-element list from markdown-specific class attribute
    # check to see if list is populated
    markdown_path = tree.xpath('//*[@id="product"]/div[2]/div[1]/div[1]/div[2]/h5[1][@class="product-price--markdown "]')

    if markdown_path:
        return True
    else:
        return False
    

def __exPath(tree):
    # create single-element list from markdown-specific class attribute
    # check to see if list is populated
    markdown_path = tree.xpath('//p[2][@class="bodyPrimary price__message"]')

    # debugging
    print(markdown_path)

    if markdown_path:
        return True
    else:
        return False


def __jcPath(tree):
    # create single-element list from markdown-specific class attribute
    # check to see if list is populated
    markdown_path = tree.xpath('//*[@class="product__price--sale discount-percentage"]/text()')

    # debugging
    print(markdown_path)

    if markdown_path:
        return True
    else:
        return False


def __nsPath(tree):
    # create single-element list from markdown-specific class attribute
    # check to see if list is populated
    markdown_path = tree.xpath('//*[@class="current-price price-display-sale"]')
    markdown_path_range = tree.xpath('//*[@class="percentage-off-range"]')

    if markdown_path or markdown_path_range:
        return True
    else:
        return False



def scrape_sale_status(vendor, url):
    # get page content and convert to tree format
    page = requests.get(url)
    tree = html.fromstring(page.content)
    tree = etree.ElementTree(tree)

    vendor_paths = {'Banana Republic' : __brPath,
                    'Express' : __exPath,
                    'J.Crew' : __jcPath,
                    'Nordstrom' : __nsPath,
                    }

    return vendor_paths[vendor](tree)



def __main():
    print(scrape_sale_status('Banana Republic', 'http://bananarepublic.gap.com/browse/product.do?cid=26220&pcid=26219&vid=2&pid=797686002'))

    # Express XPath method currently buggy
    print(scrape_sale_status('Express', 'https://www.express.com/clothing/men/camo-hooded-puffer-coat/pro/04314214C/color/GREEN'))

    # JCrew XPath method currently buggy
    print(scrape_sale_status('J.Crew', 'https://www.jcrew.com/p/mens_category/dressshirts/ludlowdress/ludlow-slimfit-shirt-in-thin-stripe/G7455?sale=true&color_name=cambridge-harvest&isFromSale=true'))

    print(scrape_sale_status('Nordstrom', 'https://shop.nordstrom.com/s/bonobos-slim-fit-stretch-washed-chinos/4877966?breadcrumb=Home%2FSale%2FMen%2FClothing'))



if __name__ == '__main__':
    __main()
