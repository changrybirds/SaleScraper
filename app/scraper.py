'''Dev notes 2018-02-24:
- selenium implementation is working!
- refactored webdriver initialization to avoid initializing and quitting w/ every query
'''

# Imports needed for parsing
from lxml import etree, html
from selenium import webdriver
import requests


def __brPath(tree):
  # create single-element list from markdown-specific class attribute
  # check to see if list is populated
  markdown_path = tree.xpath('//*[@id="product"]/div[2]/div[1]/div[1]/div[2]/h5/span[@class="product-price--highlight"]')

  if markdown_path:
    return True
  else:
    return False
  

def __exPath(tree):
  # create single-element list from markdown-specific class attribute
  # check to see if list element contains markdown text
  markdown_path = tree.xpath('//*[@id="content"]/div/div/section/section[1]/section/div[2]/div/div/text()')

  markdown_string = "marked down from"

  if markdown_string in markdown_path[0]:
    return True
  else:
    return False


def __jcPath(tree):
  # create single-element list from markdown-specific class attribute
  # check to see if list is populated
  markdown_path = tree.xpath('//*[@class="product__price--sale discount-percentage"]/text()')

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
  markdown_path = tree.xpath('//*[@id="product-content"]/div/div[5]/span[2][@class="price-standard pdp-space-price"]')

  if markdown_path:
    return True
  else:
    return False


def scrape_sale_status(browser, vendor, url):
  # navigate to url and grab page content via selenium
  browser.get(url)
  html_source = browser.page_source

  tree = html.fromstring(html_source)
  tree = etree.ElementTree(tree)

  vendor_paths = {'Banana Republic' : __brPath,
                  'Express' : __exPath,
                  'J.Crew' : __jcPath,
                  'Nordstrom' : __nsPath,
                  'Uniqlo' : __uqPath
                  }

  return vendor_paths[vendor](tree)


def start_browser():
  return webdriver.Chrome()

def shutdown_browser(browser):
  browser.quit()


# test code
def main():
  browser = start_browser()

  # uncomment lines to run individual tests

  # print(scrape_sale_status(browser, 'Banana Republic', 'http://bananarepublic.gap.com/browse/product.do?cid=47431&pcid=10894&vid=1&pid=176742382'))
  
  # print(scrape_sale_status(browser, 'Express', 'https://www.express.com/clothing/men/detailed-crew-neck-sweater/pro/01775033/color/YELLOW'))

  # print(scrape_sale_status(browser, 'J.Crew', 'https://www.jcrew.com/p/mens_category/shirts/classicfitshirts/slim-brushed-flannel-shirt-in-tattersall/G8286?color_name=metal-abyss'))
  
  # print(scrape_sale_status(browser, 'Nordstrom', 'https://shop.nordstrom.com/s/nordstrom-mens-shop-smartcare-trim-fit-dress-shirt/3286612?breadcrumb=Home%2FSale%2FMen%2FClothing'))

  # print(scrape_sale_status(browser, 'Uniqlo', 'https://www.uniqlo.com/us/en/men-ultra-light-down-jacket-400504.html'))

  # print(scrape_sale_status(browser, 'Uniqlo', 'https://www.uniqlo.com/us/en/men-blocktech-parka-404362.html'))

  shutdown_browser(browser)

  pass


if __name__ == '__main__':
  main()
