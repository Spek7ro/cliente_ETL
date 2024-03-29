##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: repository.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define el acceso e interacción entre el componente
#   y el API
#
#-------------------------------------------------------------------------
from src.data.provider import Provider
from src.data.queries import Queries

class Repository:


     #obtener la respuesta de la consulta de cantidad de productos vendidos
    @staticmethod
    def get_cantidad_productos_vendidos_por_fecha(start_period, end_period):
        response = Provider.execute(Queries.get_cantidad_productos_vendidos_por_fecha(start_period, end_period))
        return response

    @staticmethod
    def get_products():
        response = Provider.execute(Queries.get_total_products())
        return response

    @staticmethod
    def get_providers():
        response = Provider.execute(Queries.get_total_providers())
        return response

    @staticmethod
    def get_locations():
        response = Provider.execute(Queries.get_total_locations())
        return response

    @staticmethod
    def get_orders():
        response = Provider.execute(Queries.get_total_orders())
        return response

    @staticmethod
    def get_sales():
        response = Provider.execute(Queries.get_total_sales())
        return response

    @staticmethod
    def get_providers_by_location():
        response = Provider.execute(Queries.get_providers_per_location())
        return response

    @staticmethod
    def get_sales_by_location():
        response = Provider.execute(Queries.get_sales_per_location())
        return response

    @staticmethod
    def get_orders_by_location():
        response = Provider.execute(Queries.get_orders_per_location())
        return response

    @staticmethod
    def get_best_sellers():
        response = Provider.execute(Queries.get_best_sellers())
        return response

    @staticmethod
    def get_worst_sales():
        response = Provider.execute(Queries.get_worst_sales())
        return response
    
    @staticmethod
    def get_most_selled_products():
        response = Provider.execute(Queries.get_most_selled_products())
        return response
    #obtiene el query que obtiene los porductos mas vendidos sobre fechas especificas rpm
    @staticmethod
    def get_most_selled_products_by_date(start_period, end_period):
        response = Provider.execute(Queries.get_most_selled_products_by_date(start_period, end_period))
        return response
    
    #obtiene el query que obtiene los datos sobre fechas especificas rpm
    @staticmethod
    def get_sales_by_date(start_period, end_period):
        response = Provider.execute(Queries.get_total_sales_date(start_period, end_period))
        return response
    
    #obtiene el query que obtiene los datos de ordenes sobre fechas especificas rpm
    @staticmethod
    def get_orders_by_date(start_period, end_period):
        response = Provider.execute(Queries.get_total_orders_date(start_period, end_period))
        return response
    
    #repositorio del controlador load_sales_per_provider()
    @staticmethod
    def get_sales_per_provider(start_period, end_period):
        response = Provider.execute(Queries.get_sales_per_provider(start_period, end_period))
        return response
    
   
