import sqlite3
import pandas as pd


conn = sqlite3.connect(r"C:\Users\Administrator\Documents\Python Training\Python\Training\Database\Chinook_Sqlite.sqlite")
curr = conn.cursor()

customer = ('hjj','kkk','jj','ab@gmail.com','IN')
#curr.execute(
#    """
#    INSERT INTO Customer(FirstName,LastName,Company,Email,Country) VALUES(?,?,?,?,?)
#    """,customer
#)
#conn.commit()
print("new customer added")

customer_id = 60
new_email='hh@ust.com'
company = 'UST'
#curr.execute("SELECT * FROM 'Customer'")

# curr.execute("""
# UPDATE Customer
# SET Email = ? ,Company=? where CustomerId=?
# """,(new_email,company,customer_id))

# curr.execute("""
# Delete from Customer where CustomerId=60
# """)
query = """
Select * from Customer Limit 10
"""
#determine the total sales for each country in the invoice table
# query1 = """Select BillingCountry,sum(Total) as TotalPay from Invoice group by BillingCountry """
#query1 = """Select * from summary_sales_by_country"""

df= pd.read_sql_query(query1,conn)


#df = df.groupby('BillingCountry')['Total'].sum()

df.to_sql('summary_sales_by_country',conn,if_exists='replace',index=False)
conn.close()
# curr.execute("Select * from Customer")
# data = curr.fetchall()
# for row in data:
#     print(row)




