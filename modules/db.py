import psycopg2
from psycopg2 import sql

def conenct_db(config):
    con = psycopg2.connect(config["user"], config["password"], config["host"], config["port"], config["database"])
    return con

def check_db_exist(con, db):
    con.autocommit = True
    cur = con.cursor()
    q = """ SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s; """
    cur.execute(q, (db,))
    return cur.fetchone()

def check_user_exist(u):
    con.autocommit = True
    cur = con.cursor()
    q = """ SELECT 1 FROM pg_roles WHERE rolname = %s; """
    cur.execute(q, (u,))
    return cur.fetchone()

def check_table_exist(tb):
    con.autocommit = True
    cur = con.cursor()
    q = """ SELECT 1 FROM information_schema.tables WHERE table_name = %s; """
    cur.execute(q, (tb,))
    return cur.fetchone()

def create_db(con, db):
    con.autocommit = True
    cur = con.cursor()
    q = sql.SQL("CREATE DATABASE {};").format(sql.Identifier(db))
    cur.execute(q)

def create_table(con, tb, cols):
    con.autocommit = True
    cur = con.cursor()
    q = """ CREATE TABLE {} ({}); """.format(tb, ",".join(cols))
    cur.execute(q)

def create_user(u, pwd):
    con.autocommit = True
    cur = con.cursor()
    q = sql.SQL("CREATE USER {} with encrypted password {};").format(sql.Identifier(u), sql.Literal(pwd))
    cur.execute(q)

def grant_all_priv(u, db):
    con.autocommit = True
    cur = con.cursor()
    q = sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {}").format(sql.Identifier(db), sql.Identifier(u))
    cur.execute(q)

def update_query(con, table, data, cond):
    cur = con.cursor()
    data_s = ""
    for k,v in data.items():
        data_s = data_s + "{} = {},".format(k,v)
    data_s = data_s[:-1]
    cond_s = "{} = {}".format(cond_s["key"], cond_s["value"])
    q = """ UPDATE %s SET %s WHERE %s """
    cur.execute(q, (table, data_s, cond_s))
    con.commit()

def insert_query(con, table, data):
    cur = con.cursor()
    keys_s = ""
    values_s = ""
    for k,v in data.items():
        keys_s = keys_s + "{},".format(k)
        values_s = values_s + "{},".format(k)
    keys_s = keys_s[:-1]
    values_s = values_s[:-1]
    q = """ INSERT INTO %s (%s) VALUES (%s) """
    cur.execute(q, (table, keys_s, values_s))
    con.commit()

def get_query(con, table, cols, cond):
    cur = con.cursor()
    col_s = ",".join(cols)
    cond_s = "{} = {}".format(cond_s["key"], cond_s["value"])
    q = """ SELECT %s FROM %s WHERE %s """
    cur.execute(q, (cols_s, table, cond_s))