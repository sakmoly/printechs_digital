app_name = "printechs_digital"
app_title = "Printechs Digital"
app_publisher = "Printechs"
app_description = "Printechs Digital Experience Platform and B2B Website Content Management"
app_email = "info@printechs.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "printechs_digital",
# 		"logo": "/assets/printechs_digital/logo.png",
# 		"title": "Printechs Digital",
# 		"route": "/printechs_digital",
# 		"has_permission": "printechs_digital.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/printechs_digital/css/printechs_digital.css"
# app_include_js = "/assets/printechs_digital/js/printechs_digital.js"

# include js, css files in header of web template
# web_include_css = "/assets/printechs_digital/css/printechs_digital.css"
# web_include_js = "/assets/printechs_digital/js/printechs_digital.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "printechs_digital/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Item": "public/js/item.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "printechs_digital/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "printechs_digital.utils.jinja_methods",
# 	"filters": "printechs_digital.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "printechs_digital.install.before_install"
# after_install = "printechs_digital.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "printechs_digital.uninstall.before_uninstall"
# after_uninstall = "printechs_digital.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "printechs_digital.utils.before_app_install"
# after_app_install = "printechs_digital.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "printechs_digital.utils.before_app_uninstall"
# after_app_uninstall = "printechs_digital.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "printechs_digital.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"printechs_digital.tasks.all"
# 	],
# 	"daily": [
# 		"printechs_digital.tasks.daily"
# 	],
# 	"hourly": [
# 		"printechs_digital.tasks.hourly"
# 	],
# 	"weekly": [
# 		"printechs_digital.tasks.weekly"
# 	],
# 	"monthly": [
# 		"printechs_digital.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "printechs_digital.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "printechs_digital.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "printechs_digital.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["printechs_digital.utils.before_request"]
# after_request = ["printechs_digital.utils.after_request"]

# Job Events
# ----------
# before_job = ["printechs_digital.utils.before_job"]
# after_job = ["printechs_digital.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"printechs_digital.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

