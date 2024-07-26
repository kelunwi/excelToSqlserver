# 安装pip包 pandas,sqlalchemy
# pip install pandas
# pip install sqlalchemy
import pandas as pd
from sqlalchemy import create_engine, NVARCHAR
#链接数据库(用户名、密码、主机名、数据库名)
sql_user = "sa"
sql_password = "181026"
sql_host = "localhost"
sql_dbname = "test"
con_string = (
    "mssql+pyodbc://"
    + sql_user
    + ":"
    + sql_password
    + "@"
    + sql_host
    + "/"
    + sql_dbname
    + "?driver=ODBC+Driver+17+for+SQL+Server"
)
engine = create_engine(con_string)  # 可用于to_sql和read_sql
conn = engine.connect()
# 读取 Excel 文件
path = input('请输入excel文件所在路径：')
df = pd.read_excel(path)


# df = pd.read_sql("select * from Table_1", engine)
tabel_name = input("请输入要导入的表名：")
df.to_sql(
    tabel_name, engine, if_exists="replace", index=False, schema="dbo"
)
engine.dispose()
