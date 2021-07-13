frappe.pages['sales-invoice-report'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Sales Invoice Report',
		single_column: true,

	  
	});
	page.add_menu_item("Create PDF",()=>create_pdf())
	page.add_menu_item("Export Excel",()=>export_excel())
	page.set_secondary_action("Refresh",()=>refresh())
   
	let from_date = page.add_field({
		label: "From Date",
		fieldtype: "Date",
		fieldname: "from_date",
		reqd: 1,
		change() {
			console.log(from_date);
		    make_report();
	        
 
		    
	}
	})
	 
	let to_date = page.add_field({
		label: "To Date",
		fieldtype: "Date",
		fieldname: "to_date",
		reqd: 1,
		change() {
			console.log(to_date);
			make_report();
			 
		 
	        
	
	}
	})
	 
	let shift = page.add_field({
		label: "Shift",
		fieldtype: "Select",
		fieldname: "shift",
		reqd: 1,
		options: ['Morning','Evening'],
		change() {
			console.log(shift);
			make_report();

			
		 
	         
	

		 
	}
	})

	

	function make_report() {
		var from_date_1=from_date.get_value()
	    var to_date_1=to_date.get_value()
	    var shift_1=shift.get_value()
		if (from_date_1,to_date_1,shift_1) {
			 
			if (from_date_1 < to_date_1) {

					 
				frappe.call({
					method: "cardealer.cardealer.page.sales_invoice_report.sales_invoice_report.get_report_data",
					args: {
						"from_date": from_date_1,
						"to_date": to_date_1,
						"shift": shift_1,
							
					},
					callback: function (r) {
						console.log(r.message)
						body = $(r.message).appendTo(page.main);
					}
				})
			}
			else{
				frappe.throw("Invalid Dates")
			}
		}

	}
    
	function create_pdf(){
		var from_date_1=from_date.get_value()
		var to_date_1=to_date.get_value()
		var shift_1=shift.get_value()
		if (from_date_1, to_date_1,shift_1) {
			if (from_date_1 < to_date_1) {
				frappe.call({
					method: "cardealer.cardealer.page.sales_invoice_report.sales_invoice_report.create_pdf",
					args: {
						"from_date":from_date_1,
					 
					    "to_date": to_date_1,
					    "shift":shift_1,
				    }
			    })
		    }
		    else {
		    	frappe.throw("Invalid Dates")
		    }
	    }
	    frappe.msgprint("pdf created")
	}
    
    function export_excel(){
		var from_date_1=from_date.get_value()
		var to_date_1=to_date.get_value()
		var shift_1=shift.get_value()
		if (from_date_1, to_date_1,shift_1) {
			if (from_date_1 < to_date_1) {
				frappe.call({
					method: "cardealer.cardealer.page.sales_invoice_report.sales_invoice_report.create_excel",
					args: {
						"from_date":from_date_1,
					 
					    "to_date": to_date_1,
					    "shift":shift_1,
				    }
			    })
		    }
		    else {
		    	frappe.throw("Invalid Dates")
		    }
	    }
	    frappe.msgprint("excel is created")
	}

	function refresh(){
		location.reload(true);
		

	}
}
 
	


	 


