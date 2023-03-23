from BaseClass import BaseContainerLogs

class TestAnimal(BaseContainerLogs):

    def test_methodone(self):
        log = self.getLogger()
        log.info("hello there")
        print("logs printed")

