from test_helper import run_common_tests, failed, passed, get_answer_placeholders,get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":  # TODO: your condition here
        passed()
    else:
        failed()

def testout():
    output= get_file_output()
    if output[0]=="This banana has an id of 1" and output[1] =="This banana has an id of 2":
        passed()
    else:
        failed()
if __name__ == '__main__':
    run_common_tests()
    testout()
    # test_answer_placeholders()       # TODO: uncomment test call


