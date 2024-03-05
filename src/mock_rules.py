from pydantic import BaseModel


class MockRules():
    rules = []
    __is_mock = False

    @classmethod
    def set_mock_true(cls):
        cls.__is_mock = True

    @classmethod
    def add_rules(cls, rule):
        cls.rules.append(rule)

    @classmethod
    def get_rules(cls):
        return cls.rules


