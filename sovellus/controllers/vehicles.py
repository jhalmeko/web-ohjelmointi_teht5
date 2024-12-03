from flask import jsonify

from decorators.db_conn import get_db_conn
from decorators.repository_decorator import init_repository
from models_mysql import Vehicle


# Nyt jokaista controlleria vastaa yksi tiedosto. Tiedostot sisältävät kaikki funktiot,jotka pitävät
# huolen requestin vastaanottamisesta ja responsen lähettämisestä.

@get_db_conn
@init_repository('Vehicle')
def get_all_vehicles(repo):

    vehicles =  repo.get_all()
    vehicles_json = []
    for vehicle in vehicles:
        vehicles_json.append({
            'id': vehicle.id,
            'vehiclename': vehicle.vehiclename,
            'vehicleprice': vehicle.vehicleprice
        })
    return jsonify(vehicles_json)