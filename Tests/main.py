if __name__ == "__main__":

    #pytest.main("-v test_sanity.py".split(" "))

    # trun = TestRunner()
    # print(trun.run_all_tests())

    import pytest
    from pytest_jsonreport.plugin import JSONReport

    plugin = JSONReport()
    #pytest.main(['test_sanity.py'], plugins=[plugin])

    pytest.main(['test_sanity.py'], plugins=[plugin])

    print(plugin.report)




