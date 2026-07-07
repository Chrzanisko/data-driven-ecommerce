import pandas as pd
import os
from sqlalchemy import create_engine

def clean_orders(df):

    date_format = '%Y-%m-%d %H:%M:%S'

    date_colections = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]

    for col in date_colections:

        df[col] = pd.to_datetime(df[col], format=date_format, errors='coerce')

    return df

def clean_order_items(df):

    df['shipping_limit_date'] = pd.to_datetime(
        df['shipping_limit_date'],
        format='%Y-%m-%d %H:%M:%S',
        errors='coerce')

    return df

def clean_products(df):

    df['product_category_name'] = df['product_category_name'].fillna('Other')
    df = df.dropna(subset=['product_weight_g','product_length_cm'])
    df = df.fillna(0)

    return df

def clean_customers(df):
    df['customer_zip_code_prefix'] = df['customer_zip_code_prefix'].astype(str)
    df['customer_zip_code_prefix'] = df['customer_zip_code_prefix'].str.zfill(5)
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

        print(table_name.upper())
        df.info()
        print('-----')

        duplicates = df.duplicated().sum()
        print(f"Duplicates: {duplicates}\n-----")

        df.to_sql(table_name, engine, if_exists='replace', index=False)


if __name__ == "__main__":
    run_ingestion()
