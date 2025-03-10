{
    'name': 'Money Management App',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Manage your income and expenses with ease',
    'description': """
        This module provides a user-friendly interface for managing your income and expenses.
    """,
    'author': 'Shaiful Islam',
    'depends': ['base', 'web', 'website'],
    'data': [
      'security/ir.model.access.csv',
      'views/money_entry_views.xml',
    ],
     
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    
}
