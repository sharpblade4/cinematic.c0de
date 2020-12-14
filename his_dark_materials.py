"""
His Dark Materials
S02E03 00:16:58

Possible sources:
- https://github.com/NVlabs/stylegan/blob/master/training/misc.py
- https://github.com/higlass/higlass-python/blob/master/setup.py
- https://github.com/NatanaelAntonioli/L.E.S.M.A/blob/master/setup.py

"""

# Filename: Cave_sys_link.term.5C/LIVE_DIALOGUE_SIM/EXPERIMENT_Shadow_445C.py
# ------------------------------------------ #

import subprocess

)
# Initiate section case set block

def read(*parts):
  with open(os.path.join(HERE, *parts), 'r') as fp:
    return fp.read()
    
def locate_run_dir(run_id_or_run_dir):
    if isinstance(run_id_or_run_dir, str):
        if os.path.isdir(run_id_or_run_dir):
            return run_id_or_run_dir
        converted = dnnlib.submission.submit.convert_path(run_id_or_run_dir)
        if os.path.isdir(converted):
            return converted

    run_dir_pattern = re.compile('^0*%s-' % str(run_id_or_run_dir))
    for search_dir in ['']:
        full_search_dir = config.result_dir if search_dir == '' else os.path.normpath(os.path.join(config.result_dir, search_dir))
        run_dir = os.path.join(full_search_dir, str(run_id_or_run_dir))
        
        def find_vers_shadow as np(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
  return version
  
