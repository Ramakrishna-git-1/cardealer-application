import frappe
from frappe.utils.pdf import get_pdf
import openpyxl
@frappe.whitelist()
def get_report_data(from_date,to_date,shift):
    print(from_date)
    print(to_date)
    print(shift)
    get_data=frappe.db.sql("""SELECT customer,posting_date, shift,total, total_taxes_and_charges, grand_total FROM `tabSales Invoice`
                                   where posting_date between '{0}' and '{1}' and shift like ''
                                   UNION SELECT customer,posting_date, shift,total, total_taxes_and_charges, grand_total FROM `tabSales Invoice`
                                   where posting_date between '{0}' and '{1}' and shift like '{2}'
                                   """.format(from_date,to_date,shift))

    print(get_data)
    template_render= frappe.render_template("cardealer/public/js/page_templates/sales_invoice_list.html", {'records':get_data})
   
    return template_render
@frappe.whitelist()
def create_pdf(from_date,to_date,shift):
    
    
    print(from_date)
    print(to_date)
    print(shift)
    get_data=frappe.db.sql("""SELECT customer,posting_date, shift,total, total_taxes_and_charges, grand_total FROM `tabSales Invoice`
                                   where posting_date between '{0}' and '{1}' and shift like ''
                                   UNION SELECT customer,posting_date, shift,total, total_taxes_and_charges, grand_total FROM `tabSales Invoice`
                                   where posting_date between '{0}' and '{1}' and shift like '{2}'
                                   """.format(from_date,to_date,shift))

    print(get_data)
    template_render= frappe.render_template("cardealer/public/js/page_templates/page_print_format.html", {'records':get_data})
    pdf = get_pdf(template_render)
    with open('/home/user/Downloads/sales_invoice_report.pdf', 'wb') as file:
        file.write(pdf)
    return pdf
@frappe.whitelist()
def create_excel(from_date,to_date,shift,):
    
    print(from_date)
    print(to_date)
    print(shift)
    data=[]
    get_data=frappe.db.sql("""SELECT customer,posting_date, shift,total, total_taxes_and_charges, grand_total FROM `tabSales Invoice`
                                   where posting_date between '{0}' and '{1}' and shift like ''
                                   UNION SELECT customer,posting_date, shift,total, total_taxes_and_charges, grand_total FROM `tabSales Invoice`
                                   where posting_date between '{0}' and '{1}' and shift like '{2}'
                                   """.format(from_date,to_date,shift))

    print(get_data)
    data.extend(get_data)

    workbook=openpyxl.Workbook()
    sheet=workbook.active
    print(sheet)
    sheet['A1']="Customer Name"
    sheet['B1']="Posting Date"
    sheet['C1']="Shift"
    sheet['D1']="Total"
    sheet['E1']="Total Taxes and Charges"
    sheet['F1']="Grand Total"
    row=2
    for data in data:
        sheet['A'+str(row)]=data[0]
        sheet['B'+str(row)]=data[1].strftime('%d-%m-%Y')
        sheet['C'+str(row)]=data[2]
        sheet['D'+str(row)]=data[3]
        sheet['E'+str(row)]=data[4]
        sheet['F'+str(row)]=data[5]
        row+=1
    workbook.save('/home/user/Downloads/sales_invoice_report.xlsx')




