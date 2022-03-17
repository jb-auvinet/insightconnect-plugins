from typing import Any, Dict


def return_non_empty(input_dict: Dict[str, Any]) -> Dict[Any, Any]:
    """return_non_empty. Cleans up recusively the dictionary

    :param input_dict:
    :type input_dict: Dict[str, Any]
    :rtype: Dict[Any, Any]
    """
    temp_dict = {}
    for key, value in input_dict.items():
        if value is not None:
            if isinstance(value, dict):
                return_dict = return_non_empty(value)
                if return_dict:
                    temp_dict[key] = return_dict
            else:
                temp_dict[key] = value
    return temp_dict
