# Copyright (c) 2013, ramakrishna and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import getdate

def execute(filters=None):
    from_date=getdate(filters.from_date).strftime('%d-%m-%Y')
    to_date=getdate(filters.to_date).strftime('%d-%m-%Y')
    
    if (filters.from_date==filters.to_date):
        frappe.throw("From Date and To Date should not be same")
    elif (filters.from_date>filters.to_date):
        frappe.throw("From Date exceeds the To Date")
    print(from_date,to_date)
    get_data=frappe.db.sql("""SELECT customer,posting_date, shift,total, total_taxes_and_charges, grand_total FROM `tabSales Invoice`
                                   where posting_date between '{0}' and '{1}' and shift like ''
                                   UNION SELECT customer,posting_date, shift,total, total_taxes_and_charges, grand_total FROM `tabSales Invoice`
                                   where posting_date between '{0}' and '{1}' and shift like '{2}'
                                   """.format(filters.from_date,filters.to_date,filters.shift))
        
                

    
       
    print("data is",get_data)
    columns, data = [], []
    data.extend(get_data)
    columns=[
        {
            "fieldname": "customer",
            "fieldtype": "Data",
            "label": "Customer"
            
        },
       
        {
            "fieldname": "posting_date",
            "fieldtype": "Data",
            "label": "Posting Date"
            
        },
        {
            "fieldname": "shift",
            "fieldtype": "Data",
            "label": "Shift"
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




   
  
	 
