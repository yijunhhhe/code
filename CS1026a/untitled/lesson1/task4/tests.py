from test_helper import run_common_tests, failed, passed, get_answer_placeholders,get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "":  # TODO: your condition here
        passed()
    else:
        failed()

def outtest():
    out=get_file_output()

    if out[0]=="Cheryl  :  Cherlene" and out[1]== "Cyril  :  Chet" and out[2]== "Lana  :  Truckasaurus" and out[3] == "Pam  :  Cookie Monster" and out[4] =="Ray  :  Gilles de Rais" and out[5] == "Stirling  :  Duchess":
        passed()
    else:
        failed()
if __name__ == '__main__':
    run_common_tests()
    outtest()
    # test_answer_placeholders()       # TODO: uncomment test call


