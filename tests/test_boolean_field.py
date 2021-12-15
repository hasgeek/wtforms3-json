from wtforms import BooleanField, Form
import pytest


class TestBooleanField(object):
    @pytest.mark.parametrize('value', ('', 'false', False))
    def test_falsy_value(self, value):
        class MyForm(Form):
            a = BooleanField()

        assert MyForm.from_json({'a': value}).a.data is False
