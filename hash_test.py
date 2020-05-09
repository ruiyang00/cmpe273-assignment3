
map = {"71fce5174c7ec7657710a1e5726af04e": 0,
       "3b300b5203030208e43c99ab71b812e2": 1}
list = [{'name': 'Dani Washiton', 'email': 'dwashiton@gmail.com', 'age': 25}, {
    'name': 'Jay Nath', 'email': 'jnath@gmail.com', 'age': 29}]


def get(key, max_size):
    if key in map:
        value = list[map[key]]
        list.append(map[key])
        if(len(list) > max_size):
            list.pop(max_size)
        return key

    else:
        
        list.append(map[key])

        
        return None


key = "71fce5174c7ec7657710a1e5726af04e"
print(list[map[key]])
print(list)
