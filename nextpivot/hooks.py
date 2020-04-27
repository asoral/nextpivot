# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "nextpivot"
app_title = "Nextpivot"
app_publisher = "Dexciss"
app_description = "creating custom pivot view"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "dexciss@support.com"
app_license = "Dexciss"

# Includes in <head>
# ------------------
app_include_css=[
    "https://cdn.webdatarocks.com/latest/webdatarocks.min.css"
]
app_include_js =[
    "https://cdn.webdatarocks.com/latest/webdatarocks.toolbar.min.js",
    "https://cdn.webdatarocks.com/latest/webdatarocks.js",
    "https://cdn.webdatarocks.com/latest/webdatarocks.highcharts.js",
    "https://code.highcharts.com/highcharts.js",
    "https://code.highcharts.com/highcharts-more.js"
]
# include js, css files in header of desk.html
# app_include_css = "/assets/nextpivot/css/nextpivot.css"
# app_include_js = "/assets/nextpivot/js/nextpivot.js"

# include js, css files in header of web template
# web_include_css = "/assets/nextpivot/css/nextpivot.css"
# web_include_js = "/assets/nextpivot/js/nextpivot.js"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "nextpivot.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "nextpivot.install.before_install"
# after_install = "nextpivot.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nextpivot.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nextpivot.tasks.all"
# 	],
# 	"daily": [
# 		"nextpivot.tasks.daily"
# 	],
# 	"hourly": [
# 		"nextpivot.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nextpivot.tasks.weekly"
# 	]
# 	"monthly": [
# 		"nextpivot.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "nextpivot.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nextpivot.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "nextpivot.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

