{
    'name': "Team Manager",
    'version': '1.0',
    'depends': ['base'],
    'author': "Drew Fisher",
    'category': 'Extra Tools',
    'description': """
    A simple Team management app
    """,
    # data files always loaded at installation
    'data': [
        'views/TeamManager_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}