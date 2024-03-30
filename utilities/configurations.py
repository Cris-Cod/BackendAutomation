import configparser
import mysql.connector
from mysql.connector import Error

def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

connet_config = {
    'user' : getConfig()['SQL']['user'],
    'password' : getConfig()['SQL']['password'],
    'host' : getConfig()['SQL']['host'],
    'database' : getConfig()['SQL']['database'],
}


def getPassword():
    return 'xxxxxxx'

def getConection():
    try:
        conn = mysql.connector.connect(**connet_config)
        if conn.is_connected():
            print("Conection is Successful")
            return conn
    except Error as e:
        print(e)

def getQuery(query):
    conn = getConection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row
