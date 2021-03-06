import os


def get_bool_from_env(var_name):
    import os
    val = os.getenv(var_name, None)
    return val not in (None, "0", "None", "False")


def split_colon_env(varname):
    if os.getenv(varname) is None:
        return None
    if os.getenv(varname).strip() == "":
        return []
    return [a.strip() for a in list(filter(None, os.getenv(varname, "").split(",")))]


def transform_list_options_to_dict(list_options):
    assert isinstance(list_options, list)
    dict_options = {}
    for option in list_options:
        if '=' not in option:
            raise RuntimeError("Option %s does not contain '='" % option)
        option_obj = option.split('=')
        dict_options[option_obj[0]] = option_obj[1]
    return dict_options
