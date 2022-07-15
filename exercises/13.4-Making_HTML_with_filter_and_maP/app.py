all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(lista):
	new_list = list(filter(lambda color: color["sexy"],lista))
	return new_list

def generate_li(listaFiltrada):
	html = list(map(lambda color: "<li>" + color["label"]+ "</li>",listaFiltrada))
	return html

print(generate_li(filter_colors(all_colors)))
