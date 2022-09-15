from asyncio.log import logger
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

import csv
import logging

def home(request):
    # temporary table
    csv_data = csv.reader(open('./assets/21TCLC_Nhat1.csv'), delimiter = ',')
    logger = logging.getLogger('root')
    content = ''
    for line in csv_data:
        row = render_to_string('Table/StudentTableRow.html', {'TABLE_ID':line[0], 'NAME':line[2], 'CLASS':line[3], 'ID':line[1]})
        content += row
        # logger.debug(line)
    return render(request, 'index.html', {'CONTENT':content})

def login(request):
    return render(request, 'login.html')