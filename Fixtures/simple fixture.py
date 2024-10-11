# test_rules.py
import pytest

# Define fixtures
@pytest.fixture
def setup_state_rule():
    # Setup code for state_rule
    print("Setting up state rule")
    return "State setup done"

@pytest.fixture
def setup_country_rule():
    # Setup code for country_rule
    print("Setting up country rule")
    return "Country setup done"

# Tests using fixtures
def test_state_rule(setup_state_rule):
    print("Testing state rule")
    assert setup_state_rule == "State setup done"

def test_country_rule(setup_country_rule):
    print("Testing country rule")
    assert setup_country_rule == "Country setup done"
