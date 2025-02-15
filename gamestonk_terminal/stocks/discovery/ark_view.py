""" ARK View """
__docformat__ = "numpy"

import os
import pandas as pd
from tabulate import tabulate
from colorama import Fore, Style

from gamestonk_terminal import feature_flags as gtff
from gamestonk_terminal.helper_funcs import export_data
from gamestonk_terminal.stocks.discovery import ark_model


def direction_color_red_green(val: str) -> str:
    """Adds color tags to the Direction information: Buy -> Green, Sell -> Red

    Parameters
    ----------
    val : str
        Direction string - either Buy or Sell

    Returns
    -------
    str
        Direction string with color tags added
    """

    if val == "Buy":
        ret = Fore.GREEN + val + Style.RESET_ALL
    elif val == "Sell":
        ret = Fore.RED + val + Style.RESET_ALL
    else:
        ret = val

    return ret


def ark_orders_view(num: int, export: str):
    """Prints a table of the last N ARK Orders

    Parameters
    ----------
    num: int
        Number of stocks to display
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    df_orders = ark_model.get_ark_orders()

    if df_orders.empty:
        print("The ARK orders aren't available at the moment.\n")
        return

    pd.set_option("mode.chained_assignment", None)
    df_orders = ark_model.add_order_total(df_orders.head(num))

    if gtff.USE_COLOR:
        df_orders["direction"] = df_orders["direction"].apply(direction_color_red_green)

    # df_orders["link"] = "https://finviz.com/quote.ashx?t=" + df_orders["ticker"]

    print("Orders by ARK Investment Management LLC")
    print(
        tabulate(
            df_orders,
            headers=df_orders.columns,
            floatfmt=".2f",
            showindex=False,
            tablefmt="fancy_grid",
        ),
    )
    print("")

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "arkord",
        df_orders,
    )
