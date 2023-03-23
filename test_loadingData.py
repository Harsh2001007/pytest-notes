import pytest
from BaseClass import BaseContainerLogs
import logging

@pytest.mark.usefixtures("dataProvider")
class TestLoading(BaseContainerLogs):

    def test_loadDataHere(self, dataProvider):
        log = self.getLogger()
        log.info(dataProvider + 10)
        

