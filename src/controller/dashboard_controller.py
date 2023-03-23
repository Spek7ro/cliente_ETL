##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: dashboard_controller.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define la funcionalidad del componente
#
#-------------------------------------------------------------------------
from src.data.repository import Repository
import json

class DashboardController:

    #este metodo regresa la cantidad de productos vendidos
    @staticmethod
    def get_cantidad_productos_vendidos_por_fecha(start_period, end_period):
        response = Repository.get_cantidad_productos_vendidos_por_fecha(start_period, end_period)
        if response.status_code != 200:
            return {"cantidad_productos_vendidos": 0}
        
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())
        if json_response["data"]["response"][0]["count"] is None:
            return {"cantidad_productos_vendidos":"0"}

        return {
            "cantidad_productos_vendidos": json_response["data"]["response"][0]["count"]
        }
    


    @staticmethod
    def load_products():
        response = Repository.get_products()
        if response.status_code != 200:
            return {"products": 0} 
        
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        return {
            "products": json_response["data"]["response"][0]["count"]
        }

    @staticmethod
    def load_providers():
        response = Repository.get_providers()
        if response.status_code != 200:
            return {"providers": 0}
        
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        return {
            "providers": json_response["data"]["response"][0]["count"]
        }

    @staticmethod
    def load_locations():
        response = Repository.get_locations()
        if response.status_code != 200:
            return {"locations": 0}
        
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        return {
            "locations": json_response["data"]["response"][0]["count"]
        }

    @staticmethod
    def load_orders():
        response = Repository.get_orders()
        if response.status_code != 200:
            return {"orders": 0}
        
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        return {
            "orders": json_response["data"]["response"][0]["count"]
        }

    @staticmethod
    def load_sales():
        response = Repository.get_sales()
        if response.status_code != 200:
            return {"sales": 0}
        
        json_response = json.loads(response.text)
        
        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        return {
            "sales": json_response["data"]["response"][0]["total"]
        }

    @staticmethod
    def load_providers_per_location():
        response = Repository.get_providers_by_location()
        if response.status_code != 200:
            return {
                "providers": [],
                "location": []
            }
        result = {
            "providers": [],
            "location": []
        }

        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for entry in json_response["data"]["response"]:
            result["providers"].append(entry["providers"][0]["count"])
            result["location"].append(entry["name"])
        return result

    @staticmethod
    def load_sales_per_location():
        response = Repository.get_sales_by_location()
        if response.status_code != 200:
            return {
                "sales": [],
                "location": []
            }
        result = {
            "sales": [],
            "location": []
        }
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for entry in json_response["data"]["response"]:
            result["location"].append(entry["name"])
            total = 0
            for sold in entry["providers"]:
                for order in sold["sold"]:
                    total += (int(order["quantity"]) * float(order["quantity"]))
            result["sales"].append(total)
            
        return result

    @staticmethod
    def load_orders_per_location():
        response = Repository.get_orders_by_location()
        if response.status_code != 200:
            return {
                "orders": [],
                "location": []
            }
        result = {
            "orders": [],
            "location": []
        }
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for entry in json_response["data"]["response"]:
            result["location"].append(entry["name"])
            total = 0
            for sold in entry["providers"]:
                total += int(sold["sold"])
            result["orders"].append(total)
        return result

    @staticmethod
    def load_best_sellers():
        response = Repository.get_best_sellers()
        if response.status_code != 200:
            return []
        result = []
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for product in json_response["data"]["response"][0:5]:
            result.append({
                "invoice": product["times"],
                "total": int(product["times"]) * float(product["price"])
            })
        return result

    @staticmethod
    def load_worst_sales():
        response = Repository.get_worst_sales()
        if response.status_code != 200:
            return []
        result = []
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for product in json_response["data"]["response"][0:5]:
            result.append({
                "invoice": product["times"],
                "total": int(product["times"]) * float(product["price"])
            })
        return result

    @staticmethod
    def load_most_selled_products():
        response = Repository.get_most_selled_products()
        if response.status_code != 200:
            return []
        result = []
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for product in json_response["data"]["response"][0:5]:
            result.append({
                "product": product["description"],
                "times": product["times"]
            })
        return result
    #Método que recorre el json creado por la consulta y 
    # agrega a una lista los productos y las veces que se ha vendido
    @staticmethod
    def load_most_selled_products_by_date(start_period,end_period):
        response = Repository.get_most_selled_products_by_date(start_period,end_period)
        if response.status_code != 200:
            return []
        result = []
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for product in json_response["data"]["response"][0:5]:
            result.append({
                "product": product["description"],
                "times": product["times"]
            })
        return result
    

    #manda al repositorio dos fechas para que obtenga los datos de las ventas hechas entre dos fechas rpm
    @staticmethod
    def load_sales_date(start_period,end_period):
        response = Repository.get_sales_by_date(start_period,end_period)
        if response.status_code != 200:
            return {"sales": 0}
        
        json_response = json.loads(response.text)
        
        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())
        if json_response["data"]["response"][0]["total"] is None:
            return {"sales":"0"}

        return {
            "sales": json_response["data"]["response"][0]["total"]
        }
    
    #manda al repositorio dos fechas para que obtenga los datos de las ordenes hechas entre dos fechas rpm
    @staticmethod
    def load_orders_date(start_period,end_period):
        response = Repository.get_orders_by_date(start_period,end_period)
        if response.status_code != 200:
            return {"orders": 0}
        
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        return {
            "orders": json_response["data"]["response"][0]["count"]
        }
    
    #Se utiliza el bucle for sold in entry["providers"]: para recorrer la lista de proveedores
    # de cada ubicación y se calcula la suma total de las ventas de cada proveedor dentro de este bucle.
    # Se almacena el total de ventas en una lista de resultados junto con el ID del proveedor correspondiente. 
    # Finalmente, se devuelve el diccionario result que contiene los totales de ventas por proveedor y su respectivo ID.
    @staticmethod
    def load_sales_per_provider(start_period, end_period):
        response = Repository.get_sales_per_provider(start_period, end_period)
        if response.status_code != 200:
            return {
                "sales": [],
                "provider": []
            }
        result = {
            "sales": [],
            "provider": []
        }
        json_response = json.loads(response.text)

        assert('data' in json_response.keys())
        assert('response' in json_response['data'].keys())

        for entry in json_response["data"]["response"]:
            result["provider"].append(entry["pid"])
            total = 0
            for sold in entry["sold"]:
                total += (int(sold["quantity"]) * float(sold["price"]))
            result["sales"].append(total)

        return result
        
