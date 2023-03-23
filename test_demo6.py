import pytest
from BaseClass import BaseContainerLogs


@pytest.mark.usefixtures("conf_demo")
class TestExample(BaseContainerLogs):

    def test_demo(self):
        log = self.getLogger()
        a = 'hey'
        log.info(a)
        print("i am demo0")
    
    def test_demo1(self):
        print("i am demo1")
        log = self.getLogger()
        log.critical("critical error is observed")

    def test_demo2(self):
        print('i am demo2')

    def test_demo3(self):
        print("i am demo3")

    def test_loadDataHere(self):
        print('hi')

    
@pytest.mark.usefixtures("dataProvider")
class DataLoading:

    def test_loadDataHere(self):
        print('hi')