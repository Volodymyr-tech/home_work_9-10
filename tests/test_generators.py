import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transaction, currency, sorted_dict):
    result = list(filter_by_currency(transaction, currency))
    assert result == sorted_dict


def test_transaction_descriptions(transaction, transaction_descriptions_fixture):
    result = list(transaction_descriptions(transaction))
    assert result == transaction_descriptions_fixture
