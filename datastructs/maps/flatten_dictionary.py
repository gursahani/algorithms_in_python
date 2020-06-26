def flatten_dictionary(dictionary):
    final = {}

    def _flatten_dict(obj, parent_keys=[]):
        for k, v in obj.items():
            if isinstance(v, dict):
                _flatten_dict(v, parent_keys + [k])
            else:
                key = '.'.join(parent_keys + [k])
                final[key] = v

    _flatten_dict(dictionary)
    return final

print(flatten_dictionary(
    {"Key1": "1",
     "Key2": {
         "a": "2",
         "b": "3",
         "c": {
             "d": "3",
             "e": "1"
         }
     }
     }
)
)