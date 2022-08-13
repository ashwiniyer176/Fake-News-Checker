"""
This is an example of an exrernal file, Any module which deals with a specfic operation lets say preprossing of the data can be exported to a external modue and 
its contents can then be retrived by doing its import 'packagename.filename' format.

"""


from flask import json, url_for


def JokesFunction():
    data = json.load(open("./analyse/static/files/jokes.json"))
    print(data)
    return data
