def format_date(date):
    initial_date = date.split('-')
    return "/".join(initial_date[::-1])
