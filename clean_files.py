from __future__ import print_function
import os, sys, json


DOCS_DIR = 'docs/'
KEYS_TO_REMOVE = [
    '/spore',
    '/health',
    '/swagger',
]


def get_dict_from_json_file(filename):
    with open(filename, mode='r') as f:
        file_content = f.read()
        json_dict = json.loads(file_content)

    return json_dict


def remove_service_url_docs_keys(json_dict):
    for key in KEYS_TO_REMOVE:
        try:
            del json_dict['paths'][key]
        except KeyError:
            print('Tried to delete key, but it doesn\'t exist')
    
    return json_dict


def rewrite_file_with_new_json(filename, json_dict):
    json_str = json.dumps(json_dict)

    with open(filename, mode='w') as f:
        f.write(json_str)


def clean_files():
    files = [f for f in os.listdir(DOCS_DIR) if os.path.isfile(os.path.join(DOCS_DIR, f))]

    for filename in files:
        from pdb import set_trace; set_trace
        relative_filename = os.path.join(DOCS_DIR, filename)
        json_dict = get_dict_from_json_file(relative_filename)
        clean_json_dict = remove_service_url_docs_keys(json_dict)
        rewrite_file_with_new_json(relative_filename, clean_json_dict)


if __name__ == '__main__':
    sys.exit(clean_files())

