# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .model import *


def register():
    Pool.register(
        Model,
        module='babi_reports_sale_opportunity', type_='model')
