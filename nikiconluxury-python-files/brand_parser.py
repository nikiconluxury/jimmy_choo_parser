from main_parser import WebsiteParser
class JimmyChooParser(WebsiteParser):

    def __init__(self, directory):
        self.brand = 'jimmy_choo'  # Replace spaces with underscores
        self.directory = directory

    def parse_product_blocks(self,soup,category):
        product_blocks = soup.select('.product-tile')
        print(len(product_blocks))
        parsed_data = []
        column_names = [
            'category', 'name', 'product_id', 'product_url', 'image_url','full_price','discount_price']
        parsed_data.append(column_names)
        for product in product_blocks:
            name = product.select_one(
               '.product-name a').text.strip() if product.select_one('.product-name a') else None
            product_id = product.get('data-itemid')
            product_url = product.select_one(
               '.product-name a').get('href') if product.select_one('.product-name a') else None
            image_url_tag = product.select_one('.js-producttile_image')
            image_url = image_url_tag.get(
               'data-main-src') if image_url_tag else None
            price = product.select_one('.product-standard-price').text.strip(
            ) if product.select_one('.product-standard-price') else None
            discount_price_tag = product.select_one('.product-discount-price')
            discount_price = discount_price_tag.text.strip() if discount_price_tag else None
            product_data = [
               category,
               name,
                product_id,
              product_url,
              image_url,
             price,
          discount_price,
            ]
            parsed_data.append(product_data)
        return parsed_data
