select_all_female_bears_return_name_and_age = """
    SELECT name,Age FROM Bears WHERE SEX='F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT name FROM Bears ORDER BY Name ASC;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT name,Age FROM Bears WHERE Alive = 1 ORDER BY Age ASC;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT name,age FROM Bears ORDER BY age DESC LIMIT 1;
"""
select_youngest_bear_and_returns_name_and_age = """
    SELECT name,age FROM Bears ORDER BY AGE ASC LIMIT 1;
"""