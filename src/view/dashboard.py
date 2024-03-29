##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: dashboard.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define los elementos visuales de la pantalla
#   del tablero
#
#-------------------------------------------------------------------------
from src.controller.dashboard_controller import DashboardController
import dash_bootstrap_components as dbc
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, State
from datetime import date

class Dashboard:

    def __init__(self):
        pass

    def document(self):
        return dbc.Container(
            fluid = True,
            children = [
                html.Br(),
                self._header_title("Sales Report"),
                html.Div(html.Hr()),
                self._header_subtitle("Sales summary financial report"),
                html.Br(),
                self._highlights_cards(),
                html.Br(),
                html.Br(),
                self._header_subtitle2("Numero de productos vendidos en una fecha dada:",'id-titulo1'),
                html.Div([
                        "Selecciona una fecha de inicio: ",
                         
                         dcc.DatePickerSingle(#input de tip date para elegir la fecha
                            id='input-date-productos-vendidos-1',
                            min_date_allowed=date(1995, 8, 5),
                            initial_visible_month=date(2020, 8, 5),
                            placeholder='Fecha Inicio',
                            clearable=True,
                        ),
                        " Selecciona una fecha final: ",
                         
                         dcc.DatePickerSingle(#input de tip date para elegir la fecha
                            id='input-date-productos-vendidos-2',
                            min_date_allowed=date(1995, 8, 5),
                            initial_visible_month=date(2020, 8, 6),
                            placeholder='Fecha Fin',
                            clearable=True,
                        ),
                ]),
                self.obtener_numero_productos_vendidos_por_fecha(),
                html.Br(),html.Br(),
                self._header_subtitle2("Reporte financiero por fechas",'id-titulo2'),
                html.Div([
                        "Selecciona una fecha de inicio: ",
                         
                         dcc.DatePickerSingle(#input de tip date para elegir la fecha
                            id='input-date-order-sales-1',
                            min_date_allowed=date(1995, 8, 5),
                            initial_visible_month=date(2020, 8, 5),
                            placeholder='Fecha Inicio',
                            clearable=True,
                        ),
                        " Selecciona una fecha final: ",
                         
                         dcc.DatePickerSingle(#input de tip date para elegir la fecha
                            id='input-date-order-sales-2',
                            min_date_allowed=date(1995, 8, 5),
                            initial_visible_month=date(2020, 8, 6),
                            placeholder='Fecha Fin',
                            clearable=True,
                        ),
                ]),
                self.sales_by_date(),
                html.Br(),
                #desde los botones hasta aqui esta lo de las fechas rpm
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._bar_chart_providers_by_location(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                #para que en la pagina se pueda ver la vista de las ventas por proovedor-----------------------------------------------
                html.Br(),
                self._header_subtitle2("Ventas por proveedor en una fecha dada:",'id-titulo-grafica'),
                html.Div([
                        "Selecciona una fecha de inicio: ",
                         
                         dcc.DatePickerSingle(#input de tip date para elegir la fecha
                            id='input-date-ventas-proveedor-1',
                            min_date_allowed=date(1995, 8, 5),
                            initial_visible_month=date(2020, 8, 5),
                            placeholder='Fecha Inicio',
                            clearable=True,
                        ),
                        " Selecciona una fecha final: ",
                         
                         dcc.DatePickerSingle(#input de tip date para elegir la fecha
                            id='input-date-ventas-proveedor-2',
                            min_date_allowed=date(1995, 8, 5),
                            initial_visible_month=date(2020, 8, 6),
                            placeholder='Fecha Fin',
                            clearable=True,
                        ),
                ]),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    #self._bar_chart_sales_per_provider(),
                                    width=12,
                                    id='grafica-ventas-proveedor'
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._bar_chart_sales_per_location(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._bar_chart_orders_per_location(),
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._panel_best_sellers(),
                                    width=6
                                ),
                                dbc.Col(
                                    self._panel_worst_sales(),
                                    width=6
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    self._panel_most_selled_products(),
                                    width=12
                                ),
                                #---------------------------------------------------------------------------------------------------------------------
                                html.Br(),html.Br(),

                self._header_subtitle2("Selecciona una fecha para buscar los productos mas vendidos en dicha fecha:",'id-titulo4'),
                html.Div([
                        "Selecciona una fecha de inicio: ",
                         
                         dcc.DatePickerSingle(#input de tip date para elegir la fecha
                            id='input-date-productos-mas-vendidos-1',
                            min_date_allowed=date(1995, 8, 5),
                            initial_visible_month=date(2020, 8, 5),
                            placeholder='Fecha Inicio',
                            clearable=True,
                        ),
                        " Selecciona una fecha final: ",
                         
                         dcc.DatePickerSingle(#input de tip date para elegir la fecha
                            id='input-date-productos-mas-vendidos-2',
                            min_date_allowed=date(1995, 8, 5),
                            initial_visible_month=date(2020, 8, 6),
                            placeholder='Fecha Fin',
                            clearable=True,
                        ),
                ]),
                                dbc.Col(
                                    #self._panel_most_selled_products_by_date(),
                                    id='lista-mas-vendidos-fecha',
                                    width=12
                                ),
                            ]
                        )
                    ]
                ),
                html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),

            ]
        )

    def _header_title(self, title):
        return dbc.Row(
            [
                dbc.Col(html.H2(title, className="display-4"))
            ]
        )

    def _header_subtitle(self, subtitle):
        return html.Div(
            [
                html.P(
                    subtitle,
                    className="lead",
                ),
            ],
            id="blurb",
        )
    
    #subtitulo delas fechas rpm
    def _header_subtitle2(self, subtitle,id):
        return html.Div(
            [
                html.P(
                    subtitle,
                    className="lead",
                ),
            ],
            id=id,
        )

    def _card_value(self, label, value):
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H2(value, className="card-title"),
                    ]
                ),
                dbc.CardFooter(label),
            ]
        )
    def _card_value_id(self, label, value,id):
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H2(value, className="card-title",id=id),
                    ]
                ),
                dbc.CardFooter(label),
            ]
        )


    def _highlights_cards(self):
        products = DashboardController.load_products()
        orders = DashboardController.load_orders()
        providers = DashboardController.load_providers()
        locations = DashboardController.load_locations()
        sales = DashboardController.load_sales()
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            self._card_value("Products", products["products"])
                        ),
                        dbc.Col(
                            self._card_value("Orders", orders["orders"])
                        ),
                        dbc.Col(
                            self._card_value("Providers", providers["providers"])
                        ),
                        dbc.Col(
                            self._card_value("Locations", locations["locations"])
                        ),
                        dbc.Col(
                            self._card_value("Sales", "$ {:,.2f}".format(float(sales['sales'])))
                        ),
                    ]
                ),
            ]
        )
    
    #aqui deberia estar el @app.callback pero da errores
    #esta clase muestra en pantalla las ventas hechas en un periodo especifico rpm
    def sales_by_date(self):
        #cambia las fechas para obtener diferentes resultados
        #deberia estar start_period y end_period como parametros
        #sales = DashboardController.load_sales_date("2023-01-01","2023-01-20")
        #orders = DashboardController.load_orders_date("2023-01-01","2023-01-20")
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            self._card_value_id("Orders", '2','order-date')
                        ),
                        dbc.Col(
                            self._card_value_id("Sales", "$2 ",'sales-date')
                        ),
                    ]
                ),
            ]
        )
    #este metodo devuelve el card que contendra el numero de productos vendidos en una fecha dada
    def obtener_numero_productos_vendidos_por_fecha(self):
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            self._card_value_id("Numero productos", '2','numero-productos')
                        ),
                    ]
                ),
            ]
        )

    def _bar_chart_providers_by_location(self):
        data = DashboardController.load_providers_per_location()
        bar_char_fig = px.bar(data, x="location", y="providers")
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Providers per location", className="card-title"),
                        dcc.Graph(
                            id='providers-per-location',
                            figure=bar_char_fig
                        ),
                    ]
                ),
            ]
        )

    def _bar_chart_sales_per_location(self):
        data = DashboardController.load_sales_per_location()
        bar_char_fig = px.bar(data, x="location", y="sales")
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Sales per location", className="card-title"),
                        dcc.Graph(
                            id='sales-per-location',
                            figure=bar_char_fig
                        ),
                    ]
                ),
            ]
        )

    def _bar_chart_orders_per_location(self):
        data = DashboardController.load_orders_per_location()
        bar_char_fig = px.bar(data, x="location", y="orders")
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Orders per location", className="card-title"),
                        dcc.Graph(
                            id='orders-per-location',
                            figure=bar_char_fig
                        ),
                    ]
                ),
            ]
        )

    def _panel_best_sellers(self):
        best_sellers = DashboardController.load_best_sellers()
        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Best sellers", className="card-title"),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.H5(f"- [{sale['invoice']}] $ {sale['total']:,.2f}", style={"font-weight":"bold"}),
                                                    ]
                                                ),
                                            ]
                                        )

                                        for sale in best_sellers
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def _panel_worst_sales(self):
        worst_sales = DashboardController.load_worst_sales()
        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Worst sales", className="card-title"),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.H5(f"- [{sale['invoice']}] $ {sale['total']:,.2f}", style={"font-weight":"bold"}),
                                                    ]
                                                ),
                                            ]
                                        )

                                        for sale in worst_sales
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

    def _panel_most_selled_products(self):
        most_selled = DashboardController.load_most_selled_products()
        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Most selled", className="card-title"),
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
    
    
    
    
    
    #Metodo que muesta un panel con los 5 productos mas vendidos en un peridodo especifico
    def _panel_most_selled_products_by_date(self,fecha1,fecha2):
        #Recibe como parametro las fechas del periodo
        most_selled = DashboardController.load_most_selled_products_by_date(fecha1,fecha2)
        print(most_selled)
        if most_selled is None:
            return None
        return html.Div(
            [
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H3("Most selled by date ("+fecha1+","+fecha2+")", className="card-title"),
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
    
    #Se crea la vista para las ventas por proovedor
    def _bar_chart_sales_per_provider(self,fecha1,fecha2):
        data = DashboardController.load_sales_per_provider(fecha1,fecha2)
        bar_char_fig = px.bar(data, x="provider", y="sales")
        return dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("Sales per provider by date ("+fecha1+", "+fecha2+")", className="card-title"),
                        dcc.Graph(
                            id='sales-per-provider',
                            figure=bar_char_fig
                        ),
                    ]
                ),
            ]
        )