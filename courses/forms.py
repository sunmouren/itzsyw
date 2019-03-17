# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2019/3/3 17:05
@desc: 
"""

from django import forms


class SearchForm(forms.Form):
    query = forms.CharField()
