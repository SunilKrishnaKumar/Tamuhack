from flask import current_app as app

import mysql.connector

def find_new_users():
    # print('Hello')
    cnx = get_cnx()
    cursor = cnx.cursor()
    query = ("SELECT name, flightNo, location, telegramId FROM users "
            "WHERE newFlag = 0")

    cursor.execute(query)

    for (name, flightNo, location, telegramId) in cursor:
        print("{}".format(name))

    cursor.close()
    cnx.close()

def notify_users():
    # print('Hello')
    # cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tamuhack')
    cnx = get_cnx()
    cursor = cnx.cursor()

    query = ("SELECT name, flightNo, location, telegramId FROM users "
            "WHERE newFlag = 0")
    
    cursor.execute(query)
    cursor.close()
    cnx.close()

def get_cnx():
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tamuhack')
    return cnx


