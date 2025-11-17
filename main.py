from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

# Fake data
invoice_data = {
    'invoice_number': 'INV-2025-001',
    'invoice_date': '16/Nov/2025',
    'due_date': '16/Dec/2025',
    'company': {
        'name': 'ACME Limited',
        'address': '123 Acme Road',
        'city': 'Singapore',
        'postal': '123456',
        'email': 'billing@acme.com'
    },
    'client': {
        'name': 'Enchant Pte Ltd',
        'address': '456 Enchanting Ave',
        'city': 'Singapore',
        'postal': '999000'
    },
    'line_items': [
        {
            'description': 'Brembo BBK',
            'quantity': 4,
            'unit_price': 500.00
        },
        {
            'description': 'Open pod air intake',
            'quantity': 1,
            'unit_price': 1200.00
        },
        {
            'description': 'HKS Exhaust System',
            'quantity': 1,
            'unit_price': 2000.00
        },
        {
            'description': 'Installation & Setup Service',
            'quantity': 1,
            'unit_price': 500.00
        }
    ],
    'notes': 'Payment is due within 30 days. Thank you for your business!',
    'tax_rate': 0.09
}

# Calculate totals
subtotal = sum(item['quantity'] * item['unit_price'] for item in invoice_data['line_items'])
tax_amount = subtotal * invoice_data['tax_rate']
total = subtotal + tax_amount

invoice_data['subtotal'] = subtotal
invoice_data['tax_amount'] = tax_amount
invoice_data['total'] = total

# HTML template with CSS styling
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('invoice.html')

# Render the template with data
html_content = template.render(**invoice_data)

# Ensure output directory exists
Path("outputs").mkdir(parents=True, exist_ok=True)

# Generate PDF
HTML(string=html_content).write_pdf('outputs/invoice.pdf')

print("Invoice generated successfully")
