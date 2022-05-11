from flask import Blueprint
from controllers.personsControllers import (
    PageHome,
    PersonswithOutParameters,
    PersonswithParameters,
)


persons = Blueprint("person", __name__)

routes = {
    "homepage": "/",
    "homeController": PageHome.as_view("home"),
    "person_get_add": "/persona",
    "get_post_Persons": PersonswithOutParameters.as_view("person_get_add"),
    "person_get_up_de": "/persona/<int:pk>",
    "get_up_de_Person": PersonswithParameters.as_view("person_get_up_de"),
}

persons.add_url_rule(routes["homepage"], view_func=routes["homeController"])
persons.add_url_rule(routes["person_get_add"], view_func=routes["get_post_Persons"])
persons.add_url_rule(routes["person_get_up_de"], view_func=routes["get_up_de_Person"])
