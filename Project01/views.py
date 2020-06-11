from django.http import HttpResponse
from django.template import Template, Context
import datetime


class Person(object):

    def __init__(self, name , surname):
        self.name = name
        self.surname = surname


def greeting(request):  # First view
    person = Person('Alice', 'Smith')
    external_doc = open("/Users/f/git/django-basics/Project01/Project01/templates/greetings.html")
    tmplt = Template(external_doc.read())  # Template
    external_doc.close()
    ctxt = Context({'person': person, 'current_date': datetime.datetime.now()})  # context

    document = tmplt.render(ctxt)
    return HttpResponse(document)


def bye(request):  # Second view
    return HttpResponse("Bye bye!")


def get_current_date(request):
    current_date = datetime.datetime.now()

    document = """
    <html>
    <head><title></title></head>
    <body>
    <h2>
    Current date and time : {}
    </h2>
    </body
    </html>
    """.format(current_date)

    return HttpResponse(document)


def calculate_age(request, age, year):
    """
    :param request: a request to server
    :param age: current age
    :param year: year to get the age
    :return: HttpResponse
    """
    period = year-2019
    future_age = age + period
    document = """
        <html>
        <head><title></title></head>
        <body>
        <h2>
        In {} you will be {} years old
        </h2>
        </body
        </html>
        """.format(year, future_age)
    return HttpResponse(document)