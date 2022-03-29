"""Python module that contains absolute paths constants"""


def get_abs_path_of_type(type_name: type) -> str:
    """
    Returns absolute path of given class/function type.


    :param type_name: type name class/function reference
    :type type_name: type
    :returns: string with class/function type absolute path
    :rtype: str
    """
    return f"{type_name.__module__}.{type_name.__qualname__}"


READ_FUNC_ABS_PATH = "builtins.open"
