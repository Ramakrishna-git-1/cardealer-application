# Copyright (c) 2013, ramakrishna and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	print(filters.from_date,filters.to_date)
	get_data=frappe.db.sql("""SELECT salutation,posting_date,first_name,status,gender,customer_type,username FROM `tabUser Registration` where date(posting_date) BETWEEN'{0}' and '{1}'""".format(filters.get("from_date"),filters.get("to_date")))
	print("\n\n\ndata is",get_data)
	columns, data = [], []
	data.extend(get_data)
	columns=[
        {
            "fieldname": "salutation",
            "fieldtype": "Data",
            "label": "Salutation"
            
        },
        {
            "fieldname": "posting_date",
            "fieldtype": "Data",
            "label": "Posting Date"
            
        },
        {
            "fieldname": "first_name",
            "fieldtype": "Data",
            "label": "Firstname"
            
        },
        {
            "fieldname": "status",
            "fieldtype": "Data",
            "label": "Status"
            
        },
        {
            "fieldname": "gender",
            "fieldtype": "Data",
            "label": "Gender"
            
        },
        {
            "fieldname": "customer_type",
            "fieldtype": "Data",
            "label": "Customer Type"
            
        },
        {
            "fieldname": "username",
            "fieldtype": "Data",    
            "label": "Username"
            
        }
    ]
   
  
	return columns,data
