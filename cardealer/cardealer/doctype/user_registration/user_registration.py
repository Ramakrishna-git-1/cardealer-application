# -*- coding: utf-8 -*-
# Copyright (c) 2021, ramakrishna and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class UserRegistration(Document):
     

    def before_insert(self):
        self.create_user()
        if self.status=="Lead":
            self.create_lead()
        elif self.status=="Customer":
            self.create_customer()
        elif self.status=="Opportunity":
            self.create_opportunity()
    def on_update(self):
        
        if self.status=="Customer":
            self.create_customer()
        elif self.status=="Opportunity":
            self.create_opportunity()
    
            


    def create_user(self):
        validate_email(self.email)
        username=self.username
        user_password=self.password
        
        new_user=frappe.get_doc({
            "doctype":"User",
            "email":self.email,
            "user_name":self.username,
            "first_name":self.first_name,
            "send_welcome_email":0,
            "new_password":user_password
        })
        new_user.flags.ignore_permission=True
        new_user.insert()
        send_email(self.email,self.username,self.password)


    def create_lead(self):
        person_name=self.first_name+" "+self.last_name
        new_lead=frappe.get_doc({
            "doctype":"Lead",
            "salutation":self.salutation,
            "lead_name":person_name,
            "status":"Lead",
            "gender":self.gender,
            "email_id":self.email,
            "mobile_no":self.mobile_no,

            "address_line1":self.address_line1,
            "address_line2":self.address_line2,
            "city":self.city,
            "state":self.state,
            "county":self.country,
            "territory":self.territories
        })



        new_lead.insert()
        print("Lead Created")
        # self.create_address()

    def create_customer(self):
        lead_data=frappe.db.exists({"doctype":"Lead","email_id":self.email})
            # customer_data=frappe.db.exists({"doctype":"Customer","party_name":lead_data[0][0]})
        cust_name=self.first_name+" "+self.last_name
        new_customer=frappe.get_doc({
                "doctype":"Customer",
                "salutation":self.salutation,
                "customer_name":cust_name,
                "lead_name":lead_data[0][0],
                "gender":self.gender,
                "customer_type":self.customer_type,
                "customer_group":self.customer_group,
                "territory":self.territories
        })
        new_customer.insert()
        print("Customer Created")
    

    def create_opportunity(self):
        # customer_name=frappe.db.exists()


        new_opportunity=frappe.get_doc({
           

            "doctype":"Opportunity",
            "opportunity_from":"Customer",
            "party_name":self.first_name+" "+self.last_name
        })
        new_opportunity.insert()
        print("opportunity created")





def validate_email(email):
    if frappe.db.exists("User",email):
        frappe.throw("Email already exists")






def send_email(email,username,password):  
    subject="credentials to acess the system"
    context={
    "user_name":username,
    "login_id":email,
    "password":password
    }
    print(subject)
    msg=frappe.render_template("cardealer/public/js/email_template/user_login.html",context)
    frappe.sendmail(recipients=email,
                  sender=frappe.session.user, 
                  subject=subject, 
                  message=msg,
                  reference_doctype="User",
                  reference_name=username
    )
    frappe.msgprint("Email Sent")