import frappe

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_item_uoms(doctype, txt, searchfield, start, page_len, filters):
	items = [filters.get("value")]
	if filters.get("apply_on") != "Item Code":
		field = frappe.scrub(filters.get("apply_on"))
		items = [d.name for d in frappe.db.get_all("Item", filters={field: filters.get("value")})]

	return frappe.get_all(
		"UOM Conversion Detail",
		filters={"parent": ("in", items), "uom": ("like", "{0}%".format(txt))},
		fields=["distinct uom"],
		as_list=1,
	)