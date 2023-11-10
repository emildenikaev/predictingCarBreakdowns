def process_result_dynamic_multiple_data(
        series_data: list, dates_receipt: list
) -> dict:
    """
    Формирование данных для построения графика
    динамики с множественным выбором.
    """

    data = {
        "series": series_data[0]['series'],

        "chart_options":
            {
                "chart": {
                    "height": 500,
                    "type": "line",
                    "stacked": False,
                },
                "dataLabels": {
                    "enabled": False,
                },
                "stroke": {
                    "width": [5, 5, 5, 5, 3],
                    "curve": "straight",
                },
                "colors": ["#02458d", "#f37b09", "#ce003d", "#8a8b99"],
                "grid":
                    {
                        "borderColor": "#e7e7e7",
                        "row": {
                            "colors": ["#f3f3f3", "transparent"],
                            "opacity": 0.5,
                        },
                    },

                "xaxis": {
                    "type": "datetime",
                    "categories": dates_receipt,
                },
                "yaxis": [
                    {
                        "show": True,
                        "showAlways": False,
                        "showForNullSeries": True,
                        "opposite": False,
                        "reversed": False,
                        "logarithmic": False,
                        "logBase": 10,
                        "tickAmount": 10,
                        "forceNiceScale": False,
                        "floating": False,
                        "labels": {
                            "show": True,
                            "minWidth": 0,
                            "maxWidth": 160,
                            "offsetX": 0,
                            "offsetY": 0,
                            "rotate": 0,
                            "padding": 20,
                            "style": {
                                "colors": "black",
                                "fontSize": "11px",
                                "fontWeight": 400,
                                "cssClass": "",
                            },
                            "tooltip": {
                                "enabled": True,
                            },
                        },
                        "axisBorder": {
                            "show": True,
                            "color": "black",
                            "width": 1,
                            "offsetX": 0,
                            "offsetY": 0,
                        },
                        "axisTicks": {
                            "show": True,
                            "color": "black",
                            "width": 6,
                            "offsetX": 0,
                            "offsetY": 0,
                        },
                        "title": {
                            "rotate": -90,
                            "offsetY": 0,
                            "offsetX": 0,
                            "style": {
                                "fontSize": "11px",
                                "fontWeight": 900,
                                "cssClass": "",
                            },
                        },
                    },
                ],
                "tooltip": {
                    "enabled": True,
                    "shared": True,
                    "intersect": False,
                    "followCursor": True,
                    "marker": {
                        "show": False,
                    },
                    "x": {
                        "format": "dd MMM yyyy",
                    },
                    "fixed": {
                        "enabled": True,
                        "position": "topLeft",
                        "offsetY": 30,
                        "offsetX": 60,
                    },
                },
                "legend": {
                    "horizontalAlign": "left",
                    "offsetX": 40,
                    "fontSize": "17px",
                },
            },
    }

    return data


def process_result_dynamic_single_data(
        series_data: list, dates_receipt: list
) -> dict:
    """
    Формирование данных для построения графика динамики
    с одиночным выбором.
    """

    data = {
        "series": series_data[0]['series'],
        "chart_options": {
            "chart": {
                "height": 500,
                "type": "line",
                "stacked": False,
            },
            "dataLabels": {
                "enabled": False,
            },
            "stroke": {
                "width": [6, 1, 3],
                "curve": "straight",
            },
            "colors": ["#f37b09", "#02458d"],
            "grid": {
                "borderColor": "#e7e7e7",
                "row": {
                    "colors": ["#f3f3f3", "transparent"],
                    "opacity": 0.5,
                },
            },

            "xaxis": {
                "type": "datetime",
                "categories": dates_receipt,
            },
            "yaxis": [
                {
                    "axisTicks": {
                        "show": True,
                    },
                    "axisBorder": {
                        "show": True,
                        "color": "#f37b09",
                    },
                    "labels": {
                        "style": {
                            "colors": "#f37b09",
                        },
                    },
                    "tooltip": {
                        "enabled": True,
                    },
                },
                {
                    "opposite": True,
                    "axisTicks": {
                        "show": True,
                    },
                    "axisBorder": {
                        "show": True,
                        "color": "#02458d",
                    },
                    "labels": {
                        "style": {
                            "colors": "#02458d",
                        },
                    },
                    "tooltip": {
                        "enabled": True,
                    },
                },
            ],
            "tooltip": {
                "enabled": True,
                "shared": True,
                "intersect": False,
                "followCursor": True,
                "marker": {
                    "show": False,
                },
                "x": {
                    "format": "dd MMM yyyy",
                },
                "fixed": {
                    "enabled": True,
                    "position": "topLeft",
                    "offsetY": 30,
                    "offsetX": 60,
                },
            },
            "legend": {
                "horizontalAlign": "left",
                "offsetX": 40,
                "fontSize": "17px",
            },
        },
    }

    return data


def process_result_season_data(
        series_data: list, dates_receipt: list
) -> dict:
    """
    Формирование данных для построения графика сезонов.
    """
    data = {
        "series": series_data[0]['series'],
        "chart_options": {
            "chart": {
                "height": 500,
                "type": "line",
                "stacked": True,
                "animations": {
                    "enabled": False
                }
            },
            "plotOptions": {
                "bar": {
                    "columnWidth": "100%"
                }
            },
            "dataLabels": {
                "enabled": False
            },
            "stroke": {
                "width": [3],
                "curve": "straight"
            },
            "noData": "Данных нет",
            "colors": [
                "#ce003d",
                "#de7008",
                "#578ad6",
                "#d4470f",
                "#7f7f7e",
                "#de8703",
                "#d9d6d1",
                "#003896",
                "#b3c7e3",
                "#d2cbbf",
                "#f25900",
                "fa9e0d",
                "#002469",
                "1c1475",
                "#8a8b99"
            ],
            "xaxis": {
                "type": "datetime",
                "categories": dates_receipt,
            },
            "yaxis": [
                {
                    "tickAmount": 10,
                    "axisTicks": {
                        "show": True
                    },
                    "axisBorder": {
                        "show": True,
                        "color": "#02458d"
                    },
                    "labels": {
                        "style": {
                            "colors": "#02458d"
                        }
                    }
                }
            ],
            "tooltip": {
                "enabled": True,
                "shared": False,
                "intersect": False,
                "followCursor": True,
                "marker": {
                    "show": False
                },
                "fixed": {
                    "enabled": True,
                    "position": "topLeft",
                    "offsetY": 30,
                    "offsetX": 60
                }
            }
        }
    }

    return data


def process_result_demand_forecast_data(
        series_data: list, dates_receipt: list
) -> dict:
    """
    Формирование данных для построения графика предсказаний.
    """
    data = {
        "series": series_data[0]['series'],
        "chart_options": {
            "chart": {
                "height": 500,
                "type": "line",
                "stacked": False,
            },
            "dataLabels": {
                "enabled": False,
            },
            "stroke": {
                "width": [5, 5, 5, 5, 3],
                "curve": "straight",
            },
            "colors": ["#02458d", "#f37b09", "#ce003d", "#8a8b99"],
            "grid": {
                "borderColor": "#e7e7e7",
                "row": {
                    "colors": ["#f3f3f3", "transparent"],
                    "opacity": 0.5,
                },
            },

            "xaxis": {
                "type": "datetime",
                "categories": dates_receipt,
            },
            "yaxis": [
                {
                    "axisTicks": {
                        "show": True,
                    },
                    "axisBorder": {
                        "show": True,
                        "color": "#02458d",
                    },
                    "labels": {
                        "style": {
                            "colors": "#02458d",
                        },
                    },
                    "tooltip": {
                        "enabled": True,
                    },
                },
            ],
            "tooltip": {
                "enabled": True,
                "shared": True,
                "intersect": False,
                "followCursor": True,
                "marker": {
                    "show": False,
                },
                "x": {
                    "format": "dd MMM yyyy",
                },
                "fixed": {
                    "enabled": True,
                    "position": "topLeft",
                    "offsetY": 35,
                    "offsetX": 70,
                },
            },
            "legend": {
                "horizontalAlign": "left",
                "offsetX": 40,
                "fontSize": "17px",
            },
        },
    }

    return data


def get_fly_numbers_by_direction():
    """Номер рейса в зависимости от маршрута."""
    data = {
        "Сочи - Москва": [
            1117, 1119, 1121, 1123, 1125, 1127, 1129, 1131, 1133, 1135, 1137, 1139, 1141, 1151, 1153,
            1741, 1771, 1773, 1781, 1783, 1785, 1787, 1789, 1791, 1793, 1795, 1797, 1799, 2957, 2981,
            2985, 6180, 6182, 6186
        ],
        "Москва - Сочи": [
            1116, 1118, 1120, 1122, 1124, 1126, 1128, 1130, 1132, 1134, 1136, 1138, 1140, 1148, 1152,
            1740, 1772, 1780, 1782, 1784, 1786, 1788, 1790, 1792, 1794, 1796, 1798, 2980, 2990, 6179,
            6181, 6185
        ],
        "Москва - Астрахань": [1172, 1174, 1642],
        "Астрахань - Москва": [1173, 1175, 1643, 1775],
    }

    return data


def get_fly_directions():
    """Направления полетов."""
    return ['Москва - Сочи', 'Сочи - Москва', 'Москва - Астрахань', 'Астрахань - Москва']
