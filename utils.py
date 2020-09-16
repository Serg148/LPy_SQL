from flask import Flask, request
import sqlite3

def exec_query(query: str) -> list:
    conn = sqlite3.connect('./chinook.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def creating_request() -> str:
    ordering = request.args.get("ordering", 'Country')
    ordering_list = ordering.split(",")
    parameters_for_request = ""
    for parameter in ordering_list:
        if parameter[0] == "-":
            parameters_for_request += f" {parameter[1::]} DESC,"
        else:
            parameters_for_request += f" {parameter} ASC,"
    ready_request = f"SELECT * FROM customers ORDER BY{parameters_for_request[:-1]};"
    return ready_request
