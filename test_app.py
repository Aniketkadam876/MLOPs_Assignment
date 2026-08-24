from app import predict_result
def test_pass_student():
    assert predict_result(75) == "PASS"

def test_fail_student():
    assert predict_result(30) == "FAIL"
