import psycopg2
def add_user(tg_id, full_name, username):
    try:
        connection=psycopg2.connect(
            user = "postgres",
            password="992686847.axi",
            host="127.0.0.1",
            port="5432",
            database="postgres_db"
        )
        cursor=connection.cursor()
        sql ="""INSERT INTO OpenBudget(tg_id, full_name, username) VALUES (%s, %s, %s);"""
        cursor.execute(sql,(tg_id, full_name,username))
        connection.commit()
        cursor.close()
        connection.close()
    except psycopg2.Error as error:
        print("ERROR",error)


# def db_creat_table():
#     try:
#         connection=psycopg2.connect(
#             user = "postgres",
#             password="992686847.axi",
#             host="127.0.0.1",
#             port="5432",
#             database="postgres_db"
#         )
#         cursor=connection.cursor()
#         sql ="""CREATE TABLE OpenBudget(
#             id SERIAL NOT NULL,
#             tg_id BIGINT NOT NULL UNIQUE,
#             full_name VARCHAR(100) NOT NULL,
#             username VARCHAR(50)
#             );"""
#         cursor.execute(sql)
#         connection.commit()
#         print("Successfully")
#         cursor.close()
#         connection.close()
#     except psycopg2.Error as error:
#         print("ERROR",error)

