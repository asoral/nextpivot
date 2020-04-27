frappe.pages['self-analytics'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Self Analytics',
		single_column: true
	});
	page.chart_type = page.add_field({
		fieldname: 'chart_type',
		label: __('Chart Type'),
		fieldtype:'Select',
		options: ['line','pie','arearange','areaspline','bar','area','areasplinerange','column','pyramid','spline','waterfall'],
		default:'line',
		reqd: 1,
		onchange: function() {
		    if(frappe.route_options.json_data)
            {
                $($(frappe.render_template("self_analytics", {j_data :frappe.route_options.json_data,chart_type:page.chart_type.get_value()}))).appendTo($(wrapper).find(".page-content"));
            }
		}
	});

	if(frappe.route_options.json_data)
	{
	    $($(frappe.render_template("self_analytics", {j_data :frappe.route_options.json_data,chart_type:page.chart_type.get_value()}))).appendTo($(wrapper).find(".page-content"));
	}
}