import pytest,allure
class Test_001:

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="第一个测试")
    def test_001_1(self):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="测试步骤002")
    def test_001_2(self):
        allure.attach('描述', '我是测试步骤002的描述～～～')
        assert 1