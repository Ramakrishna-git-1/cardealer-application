// Copyright (c) 2021, ramakrishna and contributors
// For license information, please see license.txt

 
frappe.ui.form.on("User Registration",{
	// cur_frm.set_query( "vehicle_type", "User Registration",function (frm) {
 //        return {
    
 //            filters: {
 //                "item_group": cur_frm.doc.vehicle_type
 //            }
 //        };
 //    });
    
    status:function(frm){
    	if (frm.doc.status==="Lead"){
    		if (frappe.db.exists("Lead",{'email_id':frm.email})){
    			msgprint("Lead cannot be converted again")
    		}

    	}

    		
    	
    },
	mobile_no: function (frm){
		var mobile_no=frm.doc.mobile_no;
		var validate_mobile_no =  /^\d{10}$/;
		if (validate_mobile_no.test(mobile_no)){
			msgprint("number is valid")
		}
		else{
			msgprint('Mobile no is not valid');
		}
	},

	email: function (frm){
		var email=frm.doc.email;
		var validate_email=/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.com$/;
		if(validate_email.test(email)){
			msgprint("email is valid")
		}
		else{
			msgprint("email is not valid");
		}
	},
	vehicle_type: function(frm){
		 
		frm.fields_dict["vehicle_name"].get_query=function(){
			return{
				filters:{
					"item_group":frm.doc.vehicle_type
				}
			}
		}
	},

   
	
	 

 
});

