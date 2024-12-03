import mysql.connector

from decorators.db_conn_factory import init_db_conn


# route_handler_func on funktio,
# jonka yläpuolella dekoraattoria kutsutaan
# python huolehtii siitä, että dekoraattori saa
# sen alapuolella olevan funktio itselleen autom. parametrina
def get_db_conn(route_handler_func):
    # dekoraattori on siitä erikoinen,
    # että sen sisälle luodaan toinen funktio
    # tämä wrapper ottaa parametrikseen *args ja **kwargs
    def wrapper(*args, **kwargs):
        # kun tietokantayhteys avataan
        # ennen alkuperäisen funktion palauttamista, voimme
        # normaalisti laittaa con-muuttujan (tietokantayhteys)
        # routehandlerille parametrinä
        with init_db_conn() as con:
            return route_handler_func(con, *args, **kwargs)

    # huom dekoraattorin pitää palauttaa sen sisäpuolella luotu funktio
    # mutta palautukseen ei tule sulkuja perään
    return wrapper
