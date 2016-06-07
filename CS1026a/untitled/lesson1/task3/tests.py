from test_helper import run_common_tests, failed, passed, get_answer_placeholders,get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":  # TODO: your condition here
        passed()
    else:
        failed()

def testout():
    out = get_file_output()
    if out[0] =="I had such a amazing day. It was awesome so good sigh. It could not have been better but actually though such a great amazing awesome good day. ":
        passed()
    elif out[0] == "I had such a amazing day. It was awesome so good sigh. It could not have been better but actually though such a great amazing awesome good day.":
        passed()
    else:
        failed()
if __name__ == '__main__':
    run_common_tests()
    testout()
    # test_answer_placeholders()       # TODO: uncomment test call


