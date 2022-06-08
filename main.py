# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
from collections import namedtuple

import curl

# Press the green button in the gutter to run the script.
import shopper_data
import pandas as pd

if __name__ == '__main__':
    shopper_curl = curl.Curl()
    response = shopper_curl.shopper_request()

    # Vários subdepartments
    # Vários produtos em cada subpartment

    shopper_json = shopper_data.Shopper.from_json(response)
    subdepartments = shopper_json.subdepartments

    for subdepartment in range(len(subdepartments)):
        subdepartment_details = subdepartments[subdepartment]

        for products in range(len(subdepartment_details['products'])):
            product_details = subdepartment_details['products'][products]

            product_department_const = "Alimentos"  # Const
            product_seller_store_const = "Shopper"  # Const
            product_available_const = "S"  # Const

            product_name = product_details['name']
            product_id = product_details['id']
            product_category = subdepartment_details['name']
            product_seller_player = product_details['merchants'][0]['name']
            product_price_store = product_details['price']
            product_price_player = product_details['merchants'][0]['price']
            product_discount_store = product_details['savingPercentage']
            product_stock_qty = product_details['maxCartQuantity']
            product_url = product_details['url']
            product_image = product_details['image']

            # Tratar para data e horário
            product_created_at = "0" #product_details['merchants'][[products]['lastUpdate']]
            product_created_hour = "0" #product_details['merchants'][[products]['lastUpdate']]

            data = {
                'Coluna(s)': ['name', 'sku', 'department', 'category', 'seller_store', 'seller_player',
                              'price_store', 'price_player', 'discount_store', 'available', 'stock_qty',
                              'url', 'image', 'created_at', 'hour'],
                'Descrição': ['Nome do produto', 'Código Interno do produto', 'Departamento', 'Categoria',
                              'Loja Principal', 'Vendedor', ' ', ' ', 'Desconto do produto',
                              'S = Produto Disponível \n N = Produto Indisponível', 'Qtde de Estoque do produto',
                              'Url do produto', 'Imagem do produto', 'Data da captura', 'Hora da captura'],
                'Valor': [product_name, product_id, product_department_const, product_category,
                          product_seller_store_const, product_seller_player, product_price_store,
                          product_discount_store, product_price_player, product_available_const,
                          product_stock_qty, product_url, product_image,
                          product_created_at, product_created_hour],
                'Tipo': ['string', 'string', 'string', 'string', 'string', 'string', 'numeric', 'numeric',
                         'string', 'string', 'numeric', 'string', 'string', 'date', 'time']
                }

            seller = pd.DataFrame(data, columns=['Coluna(s)', 'Descrição', 'Valor', 'Tipo'])

            seller.to_csv(r'C:\Users\theus\seller_' + product_name + '.csv', index=False, header=True)
