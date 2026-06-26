{
'name' : 'Inventory Management',
'version' : '5.0',
'summary' : 'Manage your inventory efficiently',
'description' : 'This module helps you manage your inventory, track stock levels, and generate reports.',
'author' : 'Derry Andhika',
'depends' : ['base'],
'data' : [
    'security/ir.model.access.csv',
    'data/sequence_in.xml',
    'data/sequence_out.xml',
    'views/products.xml',
    'views/stock_in.xml',
    'views/stock_out.xml',
],
'installable' : True,
'application' : True,
}