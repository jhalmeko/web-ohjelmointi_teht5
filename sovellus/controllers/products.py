from flask import jsonify

from decorators.db_conn import get_db_conn
from decorators.repository_decorator import init_repository
from models_mysql import Product


# Nyt jokaista controlleria vastaa yksi tiedosto. Tiedostot sisältävät kaikki funktiot,jotka pitävät
# huolen requestin vastaanottamisesta ja responsen lähettämisestä.

@get_db_conn
@init_repository('Product')
def get_all_products(repo):

    products =  repo.get_all()
    products_json = []
    for product in products:
        products_json.append({
            'id': product.id,
            'productname': product.productname,
            'productprice': product.productprice
        })
    return jsonify(products_json)