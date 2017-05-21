#!/usr/bin/python


def print_dict(dct, dict_property="Property", wrap=0):
    """Print a `dict` as a table of two columns.

    :param dct: `dict` to print
    :param dict_property: name of the first column
    :param wrap: wrapping for the second column
    """
    pt = prettytable.PrettyTable([dict_property, 'Value'])
    pt.align = 'l'
    for k, v in six.iteritems(dct):
        # convert dict to str to check length
        if isinstance(v, dict):
            v = six.text_type(v)
        if wrap > 0:
            v = textwrap.fill(six.text_type(v), wrap)
        # if value has a newline, add in multiple rows
        # e.g. fault with stacktrace
        if v and isinstance(v, six.string_types) and r'\n' in v:
            lines = v.strip().split(r'\n')
            col1 = k
            for line in lines:
                pt.add_row([col1, line])
                col1 = ''
        else:
            pt.add_row([k, v])

    if six.PY3:
        print(encodeutils.safe_encode(pt.get_string()).decode())
    else:
        print(encodeutils.safe_encode(pt.get_string()))
