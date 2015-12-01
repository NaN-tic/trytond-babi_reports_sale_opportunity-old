# This file is part of the babi_reports_sale_opportunity module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class BabiReportsSaleOpportunityTestCase(ModuleTestCase):
    'Test Babi Reports Sale Opportunity module'
    module = 'babi_reports_sale_opportunity'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        BabiReportsSaleOpportunityTestCase))
    return suite