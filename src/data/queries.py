##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: queries.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define las consultas que permiten obtener información 
#   y realizar el llenado de datos del tablero
#
#-------------------------------------------------------------------------
class Queries:

    @staticmethod
    def get_total_products():
        return """
            {
                response(func: has(description)) {
                    count(uid)
                }
            }
        """

    @staticmethod
    def get_total_providers():
        return """
            {
                response(func: has(pid)) {
                    count(uid)
                }
            }
        """

    @staticmethod
    def get_total_locations():
        return """
            {
                response(func: has(name)) {
                    count(uid)
                }
            }
        """

    @staticmethod
    def get_total_orders():
        return """
            {
                response(func: has(invoice)) {
                    count(uid)
                }
            }
        """

#     {
#   response(func: has(invoice)) @filter(between(date, "2020-01-01", "2020-12-31")) {
#     count(uid)
#   }
# }

    @staticmethod
    def get_total_sales():
        return """
            {
                var(func: has(invoice)) {
                    t as total
                }

                response() {
                    total: sum(val(t))
                }
            }
        """

    @staticmethod
    def get_providers_per_location():
        return """
            {
                response(func: has(name)) {
                    name
                    providers: ~belongs {
                        count(uid)
                    }
                }
            }
        """

    @staticmethod
    def get_sales_per_location():
        return """
            {
                response(func: has(name)){
                    name
                    providers: ~belongs {
                        sold: ~sold {
                            price
                            quantity: count(bought)
                        }
                    }
                }
            }
        """

    @staticmethod
    def get_orders_per_location():
        return """
            {
                response(func: has(name)){
                    name
                    providers: ~belongs {
                        sold: count(~sold)
                    }
                }
            }
        """

    @staticmethod
    def get_best_sellers():
        return """
            {
                var(func: has(description)) {
                    c as count(bought) 
                }
                    
                response(func: has(description), orderdesc: val(c)){
                    description
                    times: val(c)
                    price
                }
            }
        """

    @staticmethod
    def get_worst_sales():
        return """
            {
                var(func: has(description)) {
                    c as count(bought) 
                }
                    
                response(func: has(description), orderasc: val(c)){
                    description
                    times: val(c)
                    price
                }
            }
        """

    @staticmethod
    def get_most_selled_products():
        return """
            {
                var(func: has(description)) {
                    c as count(bought) 
                }
                    
                response(func: has(description), orderdesc: val(c)){
                    description
                    times: val(c)
                }
            }
        """
    #Consulta que devuelve la decripcion de un producto y las veces que se ha vendido, 
    #   filtrado por un periodo especifico
    @staticmethod
    def get_most_selled_products_by_date(start_period, end_period):
        return f"""
            {{
                var(func: has(date))@filter(ge(date, "{start_period}") AND le(date, "{end_period}")) {{ 
                    product: ~bought{{ 
                        c as count(bought)
                    }} 
                }}
                
                response(func: has(description), orderdesc: val(c))  {{ 
                    description
                    times: val(c)
                }}
            }}
        """
    
    #query que filtra los datos de las ventas hechas por los clientes para que se muestren solamente
    #los que estan entre dos fechas o periodos especificados 
    #ej 2023-01-01T00:00:00Z o solo 2023-01-01 el primero permite tambien especificar la hora rpm

    @staticmethod
    def get_total_sales_date(start_period, end_period):
        return f"""
            {{
                var(func: has(date)) @filter(ge(date, "{start_period}") AND le(date, "{end_period}")) {{
                    t as total
                }}
                response() {{
                    total: sum(val(t))
                }}
            }}
        """
    
    #query que filtra los datos de las ordenes hechas por los clientes para que se muestren solamente
    #los que estan entre dos fechas o periodos especificados 
    #ej 2023-01-01T00:00:00Z o solo 2023-01-01 el primero permite tambien especificar la hora rpm
    @staticmethod
    def get_total_orders_date(start_period, end_period):
        return f"""
            {{
                response(func: has(invoice)) @filter(between(date, "{start_period}", "{end_period}")) {{
                    count(uid)
                }}
            }}
        """
