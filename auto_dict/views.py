from django.shortcuts import render
from django.http import HttpResponse
from .dictionary_api_setup import *

# Create your views here.
def word_search(request,word):

    #code that gets word and definition
    word = word
    xml_string = get_xml_string(word)
    definition = get_definition(xml_string)
    context = {'word':word, 'definition':definition}




    return render(request,'auto_dict/blank.html',context)

