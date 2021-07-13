# Copyright (c) 2013, ramakrishna and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import getdate

def execute(filters=None):
	from_date=getdate(filters.from_date).strftime('%d-%m-%Y')
	to_date=getdate(filters.to_date).strftime('%d-%m-%Y')
	print(from_date,to_date)
	if (filters.from_date==filters.to_date):
		frappe.throw("From Date and To Date should not be same")
	elif (filters.from_date>filters.to_date):
		frappe.throw("From Date exceeds the To Date")
	get_data=frappe.db.sql("""SELECT  quotation_to, customer_name, transaction_date,valid_till, contact_mobile, total, total_taxes_and_charges, grand_total FROM `tabQuotation` where transaction_date BETWEEN'{0}' and '{1}'""".format(filters.get("from_date"),filters.get("to_date")))
	print("\n\n\ndata is",get_data)
	columns, data = [], []
	data.extend(get_data)
	columns=[
        {
            "fieldname": "quotation_to",
            "fieldtype": "Data",
            "label": "Quotation To"
            
        },
        {
            "fieldname": "customer_name",
            "fieldtype": "Data",
            "label": "Customer Name"
            
        },
        {
            "fieldname": "transaction_date",
            "fieldtype": "Data",
            "label": "Transaction Date"
            
        },
        {
            "fieldname": "valid_till",
            "fieldtype": "Data",
            "label": "Valid Till"
            
        },
        {
            "fieldname": "contact_mobile",
            "fieldtype": "Data",
            "label": "Mobile No"
            
        },
        {
            "fieldname": "total",
            "fieldtype": "Currency",
            "label": "Total"
            
        },
        {
            "fieldname": "total_taxes_and_charges",
            "fieldtype": "Currency",
            "label": "Total Taxes and Charges"
            
        },
        {
            "fieldname": "grand_total",
            "fieldtype": "Currency",    
            "label": "Grand Total"
            
        },

    ]
    
   
  
	return columns,data
	 
   
  
	 

