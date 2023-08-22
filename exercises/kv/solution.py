def swap_key_value(map):
    data = map.to_dict()
    for key in data:
        map.unset_(key)

    for key, value in data.items():
        map.set_(value, key)
