#! python3
# from https://github.com/rougier/numpy-100/blob/master/generators.py


def ktx_to_dict(input_file, keystarter='<'):
    """ parsing keyed text to a python dictionary. """
    answer = dict()

    with open(input_file, 'r+', encoding='utf-8') as f:
        lines = f.readlines()

    k, val = '', ''
    for line in lines:
        if line.startswith(keystarter):
            k = line.replace(keystarter, '').strip()
            val = ''
        else:
            val += line.strip()

        if k:
            answer.update({k: val})

    return answer


def dict_to_ktx(input_dict, output_file, keystarter='<'):
    """ Store a python dictionary to a keyed text"""
    with open(output_file, 'w+') as f:
        for k, val in input_dict.items():
            f.write(f'{keystarter} {k}\n')
            f.write(f'{val}\n\n')
