def get_nested_obj_value(obj, key):
    # check for object
    if not isinstance(obj, dict) or not obj:
        raise ValueError('object type is invalid and expected dictionary')
    # check for key type
    if not isinstance(key, str) or not key:
        raise ValueError("key type is invalid and must be a non-empty string")

    split_keys = key.split('/')

    k1 = split_keys[0]

    if k1 in obj:
        if len(split_keys) == 1:
            return obj[k1]
        else:
            return get_nested_obj_value(obj[k1], '/'.join(split_keys[1:]))
    else:
        return None


        