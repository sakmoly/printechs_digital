# Copyright (c) 2026, Printechs and contributors


def execute():
	from printechs_digital.setup.fill_homepage_phase3 import fill_homepage_phase3
	from printechs_digital.setup.fill_website_industries import fill_website_industries
	from printechs_digital.setup.fill_website_solutions import fill_website_solutions

	fill_website_industries()
	fill_website_solutions()
	fill_homepage_phase3()
