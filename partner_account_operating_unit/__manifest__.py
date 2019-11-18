# © 2019 brain-tec AG
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": 'Accounting & Partners with Operating Units',
    "summary": "Introduces Operating Unit (OU) in invoices and "
               "Accounting Entries with clearing account",
    "version": "12.0.1.0.0",
    "author": "brain-tec AG,"
              "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/operating-unit",
    "category": "Accounting & Finance",
    "depends": [
        'partner_operating_unit',
        'account_operating_unit',
    ],
    "license": "LGPL-3",
    "data": [
        "security/account_security.xml",
    ],
    "auto_install": True,
}
