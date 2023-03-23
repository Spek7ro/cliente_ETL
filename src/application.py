##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: application.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define la aplicación que sirve la UI y la lógica 
#   del componente
#
#-------------------------------------------------------------------------
from src.view.dashboard import Dashboard
import dash_bootstrap_components as dbc
import dash
from dash import Dash, dcc, html, Input, Output, State

from dash import Output, Input
from src.controller.dashboard_controller import DashboardController

app = dash.Dash(
    external_stylesheets=[dbc.themes.LUX],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

app.title = "ETL"

dashboard = Dashboard()

app.layout = dashboard.document()

#calback para manejar la seleecion de fechas en los reportes financieros
@app.callback(
    Output('order-date','children'),#tomamos la salida (lo que se va a hacer apartir de la llamada)
    Output('sales-date','children'),#tomamos la salida (lo que se va a hacer apartir de la llamada)
    Input('input-date-order-sales-1', 'date'),#tomamos la entrada de info
    Input('input-date-order-sales-2', 'date')#tomamos la entrada de info
)
def update_sales_and_orders(input1,input2):
    if input1 is not None and input2 is not None:
        sales = DashboardController.load_sales_date(input1,input2)
        orders = DashboardController.load_orders_date(input1,input2)
        return orders['orders'],'$'+str(sales['sales'])
    return None,None


#callback para manejar la seleccion de fechas para obtener el numero de productos vendidos en dicha fecha
@app.callback(
    Output('numero-productos','children'),#tomamos la salida (lo que se va a hacer apartir de la llamada)
    Input('input-date-productos-vendidos-1', 'date'),#tomamos la entrada de info
    Input('input-date-productos-vendidos-2', 'date')#tomamos la entrada de info
)
def update_count_product(input1,input2):
    if input1 is not None and input2 is not None:
        cantidad_productos_vendidos = DashboardController.get_cantidad_productos_vendidos_por_fecha(input1,input2)
        return cantidad_productos_vendidos["cantidad_productos_vendidos"]


#callback para manejar la seleccion de fechas para obtener los productos mas vendidos en dicha fecha
@app.callback(
    Output('lista-mas-vendidos-fecha','children'),#tomamos la salida (lo que se va a hacer apartir de la llamada)
    Input('input-date-productos-mas-vendidos-1', 'date'),#tomamos la entrada de info
    Input('input-date-productos-mas-vendidos-2', 'date')#tomamos la entrada de info
)
def update_list_most(input1,input2):
    if input1 is not None and input2 is not None:
        most_selled = DashboardController.load_most_selled_products_by_date(input1,input2)
        if most_selled is None:
            return None
        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Most selled by date ("+input1+","+input2+")", className="card-title"),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.H5(f"- {product['product']} [{product['times']} time(s) sold]", style={"font-weight":"bold"}),
                                                    ]
                                                ),
                                            ]
                                        )

                                        for product in most_selled
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    return None