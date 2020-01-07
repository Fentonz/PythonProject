import pandas
import psycopg2 as pg

conn = pg.connect(
    database="PC_PARTS", user="pcadmin", password="adminpass", host="127.0.0.1", port="5432")  # TODO check for error
curr = conn.cursor()

# get data frame
# pirmais ir querijs
df = pandas.read_sql('SELECT * FROM products WHERE id=1', conn)
# close connection
conn.close()
df
# df = pandas.read_sql('SELECT * FROM products WHERE id=1', conn)

# self.curr.execute('INSERT INTO products(product_id,name,category,price,shop,date) VALUES (%s, %s, %s, %s, %s, %s)',
#                   (item['id'], item['name'], item['category'], item['price'], item['shop'], datetime.now()))
# self.conn.commit()
# # print("test")
