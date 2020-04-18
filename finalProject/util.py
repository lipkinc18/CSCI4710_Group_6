import json

def parse_pickup(query_result):
	result_list = []
	for element in query_result:
		result_list.append({'store': element.store,'request':element.request, 'status': element.status})
	return json.dumps({'all_pickups':result_list})
