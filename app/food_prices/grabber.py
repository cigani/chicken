import pandas as pd
import requests


def setcols(item):
    item.columns = ["Country", "Price"]
    return item


URL = "https://www.numbeo.com/cost-of-living/country_price_rankings?itemId=19"
TABLE_LOCATION = -1
KWARGS = {
    1: lambda x: x.dropna(how="all"),
    2: lambda x: x.dropna(how="all", axis=1),
    3: lambda x: x.select_dtypes(object),
    4: lambda x: x.apply(lambda y: y.str.replace("$", "")),
    5: lambda x: setcols(x),
    6: lambda x: x.astype({"Country": object, "Price": float}),
}


def scrape(url=None, table_location=None, **kwargs):
    if not url:
        url = URL
    if not table_location:
        table_location = TABLE_LOCATION
    if not kwargs:
        kwargs = KWARGS

    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[table_location]
    for item, op in kwargs.items():
        df = op(df)
    print(df)
    return df


scrape()
