from django.http import HttpResponse
# from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
import datetime


class Person(object):

    def __init__(self, name , surname):
        self.name = name
        self.surname = surname


def greeting(request):  # First view
    person = Person('Alice', 'Smith')
    course_themes = ['Templates', 'Models', 'Forms', 'Views', 'Deploy']
    # external_doc = open("/Users/f/git/django-basics/Project01/Project01/templates/greetings.html")
    # tmplt = Template(external_doc.read())  # Template
    # external_doc.close()
    # external_doc = loader.get_template('greetings.html')
    # ctxt = Context({'person': person,
    #                 'current_date': datetime.datetime.now(),
    #                 'themes': course_themes
    #                 }
    #                )  # context

    # document = external_doc.render({'person': person,
    #                                 'current_date': datetime.datetime.now(),
    #                                 'themes': course_themes
    #                                 })
    return render(request, "greetings.html", {'person': person,
                                              'current_date': datetime.datetime.now(),
                                              'themes': course_themes
                                              })


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


def c_course(request):
    current_date = datetime.datetime.now()

    return render(request, "course_c.html", {"current_date": current_date})


def css_course(request):
    current_date = datetime.datetime.now()

    return render(request, "course_css.html", {"current_date": current_date})