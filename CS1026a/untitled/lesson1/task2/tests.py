from test_helper import run_common_tests, failed, passed, get_answer_placeholders,get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":  # TODO: your condition here
        passed()
    else:
        failed()
def testout():
    out= get_file_output()

    if out[0] =="T-Rex Velociraptor Stegosaurus":
        passed()
    else:
        failed()

if __name__ == '__main__':
    run_common_tests()
    testout()
    # test_answer_placeholders()       # TODO: uncomment test call


