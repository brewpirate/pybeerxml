# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from pybeerxml import Parser
import json
import os

path_to_beerxml_file = "SimcoeIPA.xml"
#path_to_beerxml_file = "rojo-chango.xml"
parser = Parser()

recipes = parser.parse(path_to_beerxml_file)

test = recipes[0]

print json.dumps(test, default=lambda o: o.__dict__)



# for recipe in recipes:
#
#
#
#     # some general recipe properties
#     print "Name: " + str(recipe.name)
#     print "Brewer: " + str(recipe.brewer)
#     # print "Style: " + str(recipe.style)
#     print "og_plato: " + str(recipe.og_plato)
#     print "fg_plato: " + str(recipe.fg_plato)
#     print "mash: " + str(recipe.mash)
#
#     # calculated properties
#     print "og: " + str(recipe.og)
#     print "fg: " + str(recipe.fg)
#     print "ibu: " + str(recipe.ibu)
#     print "abv: " + str(recipe.abv)
#
#     # iterate over the ingredients
# #     print "Hops: " + str(recipe.hops)
#     for hop in recipe.hops:
#         print "Hop: " + hop.name
#
#     for fermentable in recipe.fermentables:
#         print "Fermentable: " + fermentable.name
#
#     for yeast in recipe.yeasts:
#         print "Yeast: " + yeast.name
#
#     print recipe.mash
#     # for m in recipe.mash:
#     #     print "Mash: " + m.name
#
#     # print recipe.style.__dict__
#     # style = recipe.style
# #     print style.__dict__
#     # for styl in recipe.style:
#         # print styl.__dict__
#     print recipe.style.style_guide
#     print recipe.style.version
#     print recipe.style.category
#     print recipe.style.og_min
#     print recipe.style.og_max
#     print recipe.style.fg_min
#     print recipe.style.fg_max
#     print recipe.style.ibu_min
#     print recipe.style.ibu_max
#     print recipe.style.color_min
#     print recipe.style.color_max
#     print recipe.style.abv_min
#     print recipe.style.abv_max
#     print recipe.style.carb_min
#     print recipe.style.carb_max
#     print recipe.style.notes
#
    #
    # print "name: " + recipe.name
    # print "brewer: " + recipe.brewer
    # print "batch_size: " + str(recipe.batch_size)
    # print "boil_time: " + str(recipe.boil_time)
    # print "efficiency: " + str(recipe.efficiency)
    # print "primary_age: " + str(recipe.primary_age)
    # print "primary_temp: " + str(recipe.primary_temp)
    # print "secondary_age: " + str(recipe.secondary_age)
    # print "secondary_temp: " + str(recipe.secondary_temp)
    # print "tertiary_age: " + str(recipe.tertiary_age)
    # print "tertiary_temp: " + str(recipe.tertiary_temp)
    # print "carbonation: " + str(recipe.carbonation)
    # print "carbonation_temp: " + str(recipe.carbonation_temp)
    # print "age: " + str(recipe.age)
    # print "age_temp: " + str(recipe.age_temp)
    # print type(recipe.style)
    # # print "name: " + recipe.hops
    # # print "name: " + recipe.yeasts
    # # print "name: " + recipe.fermentables
    # print "name: " + str(recipe.mash)
