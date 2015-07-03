from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from wkhtmltopdf.views import PDFTemplateResponse

from .models import *

class IndexView(generic.View):

	def get(self, request, *args, **kwargs):
		return render(request,'page/index.html')