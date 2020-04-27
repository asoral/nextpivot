// Copyright (c) 2020, Dexciss and contributors
// For license information, please see license.txt

frappe.ui.form.on('Self Analytics', {
	doctype_name: function(frm) {
		frappe.call({
			method: "get_fields",
			doc: frm.doc,
			callback: function(data){
				frm.fields_dict.field_line.grid.remove_all();
				let objectives = data.message;
				for (var i in objectives) {
					frm.add_child("field_line");
					frm.fields_dict.field_line.get_value()[i].field_name = objectives[i].fieldname;
					frm.fields_dict.field_line.get_value()[i].label = objectives[i].label;
					frm.fields_dict.field_line.get_value()[i].field_type = objectives[i].fieldtype;
				}
				frm.refresh();
			}
		});
	},
	onload:function(frm){
	    frm.trigger('set_properties');

	},
	set_properties:function(frm){
	    if(frm.doc.based_on =='DocType')
	    {
	        frm.set_df_property("doctype_name", "reqd", 1);
	        frm.set_df_property("doctype_name", "hidden", 0);

	        frm.set_df_property("field_line", "reqd", 1);
	        frm.set_df_property("field_line", "hidden", 0);

	        frm.set_df_property("query", "reqd", 0);
	        frm.set_df_property("query", "hidden", 1);
	    }
	    else if(frm.doc.based_on =='Query')
	    {
	        frm.set_df_property("query", "reqd", 1);
	        frm.set_df_property("query", "hidden", 0);

	        frm.set_df_property("doctype_name", "reqd",0);
	        frm.set_df_property("doctype_name", "hidden", 1);

	        frm.set_df_property("field_line", "reqd", 0);
	        frm.set_df_property("field_line", "hidden", 1);
	    }
	    else
	    {
	        frm.set_df_property("query", "reqd", 0);
	        frm.set_df_property("query", "hidden",1);

	        frm.set_df_property("doctype_name", "reqd",0);
	        frm.set_df_property("doctype_name", "hidden", 1);

	        frm.set_df_property("field_line", "reqd", 0);
	        frm.set_df_property("field_line", "hidden", 1);
	    }
	},
	based_on:function(frm){
	    frm.trigger('set_properties');
	    frm.refresh();
	},
	refresh:function(frm){
	    frm.add_custom_button(__('Show Pivot'),function() {
                frappe.call({
                method: "show_pivot",
                doc: frm.doc,
                callback: function(r){

                    frappe.route_options ={'json_data': r.message}
                    frappe.set_route('self-analytics')
                }
            });
	    })
	}
});
