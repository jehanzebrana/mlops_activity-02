from main import mlops

mlopsObj = mlops(10)
def test_get_totalstudents():
    assert mlopsObj.get_totalstudents() == 10

def test_addstudent():
    mlopsObj.addstudent()
    assert mlopsObj.get_totalstudents() == 11

def test_removestudent():
    mlopsObj.removestudent()
    assert mlopsObj.get_totalstudents() == 10

def test_getClassName():
    assert mlopsObj.getClassName() == "MLOps"



