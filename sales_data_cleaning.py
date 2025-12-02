import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("messy_sales_dataset.csv")

#  Standardize the column formats
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")

#  clean the column 'region'
df['region'] = df["region"].str.strip().str.title()


# clean the product column

df['product'] = df['product'].str.strip().str.title()
df['product']=df['product'].replace([" ","None"],np.nan)

# clean the salesperson column

df["salesperson"] = df['salesperson'].str.strip().str.title()
df['salesperson'] = df["salesperson"].replace([" ","None"],np.nan)

# clean the quantity column

df["quantity"] = pd.to_numeric(df["quantity"],errors='coerce')
df.loc[df["quantity"]<=0,'quantity'] = np.nan

# clean the unit_price column

df['unit_price'] = pd.to_numeric(df['unit_price'],errors='coerce')
df.loc[df['unit_price']<=0,'unit_price'] = np.nan
df.loc[df['unit_price']>50000,'unit_price'] = np.nan

#  clean and standardize the sale_date column

df['sale_date'] = pd.to_datetime(df['sale_date'],errors='coerce',dayfirst=True)

#  clean and standardize the customer_id column

df['customer_id'] = df['customer_id'].astype(str).str.strip().str.upper()
df['customer_id'] = df['customer_id'].replace("None",np.nan)


# print(df.head(5))
df.drop_duplicates()
# print(df.shape)

df['total_amount'] = df['quantity'] * df['unit_price']
df['total_amount'] = pd.to_numeric(df['total_amount'],errors='coerce')

#  Handling missing values
df['product']=df['product'].fillna('unknown')
df['salesperson']=df['salesperson'].fillna('unknown')
df['quantity']=df['quantity'].fillna(df['quantity'].median())
df['unit_price']=df['unit_price'].fillna(df['unit_price'].median())
# print(df.head(20))
df.to_csv("cleaned_salesdata.csv",index=False)
# print(df.head(5))
df1 = pd.read_csv("cleaned_salesdata.csv")
# print(df1.head(5))
df1['total_amount'] = df1['quantity'] * df1['unit_price']
print(df1.head(5))
df1.to_csv('cleaned_dataset.csv')