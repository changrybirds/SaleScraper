'''Dev notes 2018-02-10:
- Hypothesis: any site that has 'js' as part of its HTML header won't work properly, since content is rendered via JavaScript, which lxml won't pick up

'''

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


def __uqPath(tree):
  no_markdown_path = tree.xpath('//*[@id="product-content"]/div/div[5]/span[3][@class="price-sales sale-price-only"]')

  print(no_markdown_path)

  if no_markdown_path:
    return False
  else:
    return True


def scrape_sale_status(vendor, url):
  # get page content and convert to tree format
  page = requests.get(url)
  tree = html.fromstring(page.content)
  tree = etree.ElementTree(tree)

  vendor_paths = {'Banana Republic' : __brPath,
          'Express' : __exPath,
          'J.Crew' : __jcPath,
          'Nordstrom' : __nsPath,
          'Uniqlo' : __uqPath
          }

  return vendor_paths[vendor](tree)



def __main():
  
  print(scrape_sale_status('Banana Republic', 'http://bananarepublic.gap.com/browse/product.do?cid=47431&pcid=10894&vid=1&pid=176742382'))
  
  '''
  # Express XPath method currently buggy
  print(scrape_sale_status('Express', 'https://www.express.com/clothing/men/camo-hooded-puffer-coat/pro/04314214C/color/GREEN'))

  # JCrew XPath method currently buggy
  print(scrape_sale_status('J.Crew', 'https://www.jcrew.com/p/mens_category/dressshirts/ludlowdress/ludlow-slimfit-shirt-in-thin-stripe/G7455?sale=true&color_name=cambridge-harvest&isFromSale=true'))
  '''
  print(scrape_sale_status('Nordstrom', 'https://shop.nordstrom.com/s/nordstrom-mens-shop-smartcare-trim-fit-dress-shirt/3286612?breadcrumb=Home%2FSale%2FMen%2FClothing'))
  

  print(scrape_sale_status('Uniqlo', 'https://www.uniqlo.com/us/en/men-ultra-light-down-jacket-400504.html'))

  print(scrape_sale_status('Uniqlo', 'https://www.uniqlo.com/us/en/men-blocktech-parka-404362.html'))



if __name__ == '__main__':
  __main()
