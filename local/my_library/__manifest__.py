# -*- coding: utf-8 -*-
{
    'name': "My Library",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format
    'author': "Parth Gajjar",
    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base','report_xlsx'],
    # This data files will be loaded at the installation (commented because file is not added in this example)
    'data': [

        'views/library_book.xml',
        'views/library_book_categ.xml',
        'views/library_book_rent.xml',
        'security/groups.xml',
	    'security/ir.model.access.csv',
	    'data/data.xml',
        'wizard/library_book_rent_wizard.xml',
        'views/library_book_statistics.xml',
        'report/report.xml'

    ],
    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    # 'demo': [
      #  'data/demo.xml'
   # ],


}
