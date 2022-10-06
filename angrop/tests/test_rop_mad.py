import os
import angr
import sys

sys.path.insert(0,"../..")

import angrop  # pylint: disable=unused-import
import pickle

import logging
l = logging.getLogger("angrop.tests.test_rop")

from IPython import embed

public_bin_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../my_binaries/')
test_data_location = os.path.join(public_bin_location, "..", "tests_data", "angrop_gadgets_cache")

def test_rop_arm_new_mad_mode():
    b = angr.Project(os.path.join(public_bin_location, "vuln_stacksmash_withshell"), load_options={"auto_load_libs": False})
    rop = b.analyses.ROP(only_check_near_rets=False,mad_mode=True)
    rop.find_gadgets_single_threaded(show_progress=False)

    embed()

if __name__ == "__main__":
    logging.getLogger("angrop.rop").setLevel(logging.DEBUG)

    # import sys
    # if len(sys.argv) > 1:
    #     globals()['test_' + sys.argv[1]]()
    # else:
    #     run_all()
    # import sys
    # print(len(sys.argv))
    # if (len(sys.argv)) > 1:
    #     # if sys.argv[2] == 'httpd':
    #     #     test_httpd()
    #     test_rop_arm_new_mad_mode()
    # else:
    #     test_rop_arm_new()
    test_rop_arm_new_mad_mode()