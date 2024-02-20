class mlops:
    def __init__(self, totalstudents):
        self.totalstudents = totalstudents

    def get_totalstudents(self):
        return self.totalstudents
    
    def addstudent(self):
        self.totalstudents += 1

    def removestudent(self):
        self.totalstudents -= 1

    def getClassName(self):
        return "MLOps"
    


