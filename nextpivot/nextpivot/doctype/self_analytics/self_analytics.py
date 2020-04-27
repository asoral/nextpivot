# -*- coding: utf-8 -*-
# Copyright (c) 2020, Dexciss and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import json, io

set_data = ('Section Break','HTML','Button','Text Editor','Code','Column Break','Attach','Attach Image','Image','Barcode','Color','Fold','Geolocation','Table','Table MultiSelect','Heading','Time')
class SelfAnalytics(Document):
	def get_fields(self):
		if self.doctype_name:
			result = frappe.db.sql("""select fieldname, label,fieldtype from `tabDocField` where parent =%s 
					and fieldtype not in %s""",(self.doctype_name,set_data),as_dict =True)
			return result
		return False

	def show_pivot(self):
		if self.based_on == 'DocType':
			lst = []
			field_str = ""

			count = 1
			for i in self.field_line:
				if count != len(self.field_line):
					if i.field_type in ['Date', 'Datetime']:
						field_str += "date_format(" + i.field_name + ",'%d-%m-%y') as '" + i.label + "',"
					else:
						field_str += i.field_name + " as '" + i.label + "',"
				else:
					if i.field_type in ['Date', 'Datetime']:
						field_str += "date_format(" + i.field_name + ",'%d-%m-%y') as '" + i.label + "'"
					else:
						field_str += i.field_name + " as '" + i.label + "'"

				lst.append(i.field_name)
				count += 1

			try:
				query = """select {0} from `tab{1}`""".format(field_str, self.doctype_name)
				query_result = frappe.db.sql(query,as_dict=True)
				json_data = json.dumps(query_result)
				return json_data
			except:
				frappe.throw("You have an error in your SQL syntax. Please check Manually")

		if self.based_on == 'Query':
			if not self.query:
				frappe.throw("Please write query First!")
			else:
				try:
					query_result = frappe.db.sql( self.query, as_dict=True)
					json_data = json.dumps(query_result)
					return json_data
				except:
					frappe.throw("You have an error in your SQL syntax. Please check Manually")
