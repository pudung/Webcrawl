#-*- coding: utf-8

import sqlite3
from socket import create_connection


class DB:
    def __init__(self):
        pass

    def create_connection(db_file):
        """ create a database connection to the SQLite database
                specified by db_file
            :param db_file: database file
            :return: Connection object or None
            """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except sqlite3.Error as e:
            print(e)

    def create_project(conn, Quotes):
        """
            Create a new project into the projects table
            :param conn:
            :param Quotes:
            :return: Quotes id
            """
        sql = ''' INSERT INTO Quotes(Title,link,description,pubDate)
              VALUES(?,?,?,?) '''

        cur = conn.curser()
        cur.execute(sql, Quotes)
        return cur.lastrowid

    def main(self):
        database = "C:\\sqlite\db\pythonsqlite.db"

         # create a database connection
        conn = create_connection(database)
        with conn:
         # Create a new project

            Quotes = ('대선 기사 제목', 'http://search.naver.com','Naver Search Result','2017-1-10')
