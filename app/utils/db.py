"""
Collection of functions to help establish the database
"""
import mysql.connector


# Connect to MySQL and the task database
def connect_db(config):
    conn = mysql.connector.connect(
        host=config["DBHOST"],
        user=config["DBUSERNAME"],
        password=config["DBPASSWORD"],
        database=config["DATABASE"]
    )
    return conn


# Setup for the Database
#   Will erase the database if it exists
def init_db(config):
    conn = mysql.connector.connect(
        host=config["DBHOST"],
        user=config["DBUSERNAME"],
        password=config["DBPASSWORD"]
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"DROP DATABASE IF EXISTS {config['DATABASE']};")
    cursor.execute(f"CREATE DATABASE {config['DATABASE']};")
    cursor.execute(f"use {config['DATABASE']};")
    cursor.execute(
        f""" 
        CREATE TABLE tasks
        (
            id SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL,
            description VARCHAR(50),
            creation_datetime timestamp,
            completed TINYINT(1),
            CONSTRAINT pk_todo PRIMARY KEY (id)
        );
        """
    )

    cursor.execute(
        f"""
        CREATE TABLE users
        (
            id SMALLINT UNSIGNED AUTO_INCREMENT NOT NULL,
            username VARCHAR(20) NOT NULL,
            password VARCHAR(30) NOT NULL,
            points INT(3) NOT NULL,
            CONSTRAINT pk_user PRIMARY KEY (id)
        );
        """
    )
    
    cursor.close()
    conn.close()
