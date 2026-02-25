import pytest
from esim_hunter.crew import EsimHunter

def test_crew_initialization():
    """Test that the crew and its components initialize correctly."""
    crew_instance = EsimHunter()
    
    assert crew_instance.agents_config is not None
    assert crew_instance.tasks_config is not None
    
    crew = crew_instance.crew()
    assert len(crew.agents) == 2
    assert len(crew.tasks) == 2
