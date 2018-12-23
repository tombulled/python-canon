import ast

def parse_js(js):
    """
    Function to parse the JavaScript variables in 'js'
    ... then return them as a dictionary

    NOTE: Assumes variables seperated by line-feed ('\n')
    """

    data = {}

    for line in js.splitlines():
        line = line.strip().rstrip(';').strip()

        if line.lower().startswith('var'):
            line = line[3:].strip()

        if not line:
            continue

        eq_index = line.index('=')

        key, val = line[:eq_index], line[eq_index+1:]

        key = key.strip()
        val = val.strip()

        plus = False

        if key.endswith('+'):
            plus = True
            key = key[:-1].strip()

        sub_keys = []

        if val.startswith('"') or val.startswith('\''):
            val = val[1:]

            if val.endswith('"') or val.endswith('\''):
                val = val[:-1]

        elif str(val).isdigit():
            val = int(val)

        if str(val).lower() in ('array()', 'new array()', '[]',):
            val = {}

        if str(val).startswith('['):
            val = ast.literal_eval(val)

        if '[' in key:
            key, *sub_keys = key.split('[')
            key = key.strip()

            sub_keys = [ast.literal_eval(sk.strip().rstrip(']').strip()) for sk in sub_keys]

        if sub_keys:
            if len(sub_keys) == 1:
                data[key][sub_keys[0]] = val

                continue

        if not plus:
            data[key] = val
        else:
            data[key] += val

    return data
