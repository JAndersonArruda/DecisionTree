class Subjects():
    def __init__(self):
        self.date = {"ccm": 3, "sit": 2.5, "slw": 4.5, "sdp": 2.5, "ps": 4, "cn": 3.5, "ds": 4.5, "os": 3}
        
        '''
        ccm -->> ConfigurationChangeManagement
        sit -->> SocietyInformationTechnology
        slw -->> scriptingLanguagesWeb
        sdp -->> softwareDevelopmentProcess
        ps -->> probabilityStatistics
        cn ->> computerNetwork
        ds -->> dataStructure
        os -->> operationalSystems
        '''
    
    def dateDict(self):
        return self.date