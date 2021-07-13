// Copyright (c) 2016, ramakrishna and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Quotation Report"] = {
	 "filters": [
           {
               "fieldname": "from_date",
               "fieldtype": "Date",
               "label": __("From Date"),
               
               "reqd": 1
               
           },
           {
               "fieldname": "to_date",
               "fieldtype": "Date",
               "label": __("To Date"),
            
               "reqd": 1
               
            }

	]
};
