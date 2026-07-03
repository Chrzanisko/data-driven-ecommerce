import pandas as pd
import os
from sqlalchemy import create_engine

def clean_orders(df):
    return df

def clean_order_items(df):
    return df

def clean_products(df):
    return df

def clean_customers(df):
    return df


def run_ingestion():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    db_path = os.path.join(base_dir, 'database', 'ecommerce.db')
    os.makedirs(os.path.join(base_dir, 'database'), exist_ok=True)
    engine = create_engine(f'sqlite:///{db_path}')

    files_to_load = {
        'orders': 'olist_orders_dataset.csv',
        'order_items': 'olist_order_items_dataset.csv',
        'products': 'olist_products_dataset.csv',
        'customers': 'olist_customers_dataset.csv'
    }

    clear = {
        'orders': clean_orders,
        'order_items': clean_order_items,
        'products': clean_products,
        'customers': clean_customers
    }


    for table_name, file_name in files_to_load.items():
        df = pd.read_csv(os.path.join(data_dir, file_name))

        if table_name in clear:
            df = clear[table_name](df)

        df.to_sql(table_name, engine, if_exists='replace', index=False)


if __name__ == "__main__":
    run_ingestion()