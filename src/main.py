"""
Tests for WikipediaSurfer class
"""

import pytest
from unittest.mock import patch, MagicMock
import sys

sys.path.append(".")

from src.wikipedia_page import WikipediaPage
from main import WikipediaSurfer


@patch('builtins.input', return_value='Python_(programming_language)')
def test_init_valid_page(mock_input):
    """Test initialization with a valid Wikipedia page."""
    surfer = WikipediaSurfer("test")
    
    assert surfer.root is not None
    assert surfer.current_page == surfer.root
    assert len(surfer.previous_pages) == 0
    assert WikipediaPage.target_word == "test"


@patch('builtins.input', side_effect=['InvalidPage123', 'Python_(programming_language)'])
def test_init_retry_on_invalid(mock_input):
    """Test that init retries when given an invalid page."""
    surfer = WikipediaSurfer("test")
    
    assert surfer.root is not None
    assert mock_input.call_count == 2


def test_list_options_no_previous():
    """Test list_options when there are no previous pages."""
    with patch('builtins.input', return_value='Python_(programming_language)'):
        surfer = WikipediaSurfer("test")
    
    options = surfer.list_options()
    
    assert "1: Quit" in options
    assert "2: Go back" not in options
    assert "2:" in options  # Should have a link at position 2


def test_list_options_with_previous():
    """Test list_options when there are previous pages."""
    with patch('builtins.input', return_value='Python_(programming_language)'):
        surfer = WikipediaSurfer("test")
    
    # Add a page to previous_pages
    surfer.previous_pages.append(surfer.root)
    
    options = surfer.list_options()
    
    assert "1: Quit" in options
    assert "2: Go back to the previous page" in options
    assert "3:" in options  # Links should start at 3


def test_list_options_max_options():
    """Test list_options respects max_options."""
    with patch('builtins.input', return_value='Python_(programming_language)'):
        surfer = WikipediaSurfer("test")
        surfer.max_options = 5
    
    options = surfer.list_options()
    
    # Count number of options (lines with colons)
    option_lines = [line for line in options.split('\n') if ':' in line and line.strip()]
    
    # Should have at most max_options lines
    assert len(option_lines) <= 5


@patch('builtins.input', side_effect=['5'])
def test_get_user_choice_valid(mock_input):
    """Test get_user_choice with valid input."""
    with patch('builtins.input', return_value='Python_(programming_language)'):
        surfer = WikipediaSurfer("test")
    
    with patch('builtins.input', return_value='5'):
        with patch('builtins.print'):
            choice = surfer.get_user_choice()
    
    assert choice == 5


@patch('builtins.input', side_effect=['invalid', '-1', '5'])
def test_get_user_choice_retry(mock_input):
    """Test get_user_choice retries on invalid input."""
    with patch('builtins.input', return_value='Python_(programming_language)'):
        surfer = WikipediaSurfer("test")
    
    with patch('builtins.input', side_effect=['invalid', '-1', '5']):
        with patch('builtins.print'):
            choice = surfer.get_user_choice()
    
    assert choice == 5


def test_update_graph_quit():
    """Test update_graph with quit choice."""
    with patch('builtins.input', return_value='Python_(programming_language)'):
        surfer = WikipediaSurfer("test")
    
    original_page = surfer.current_page
    surfer.update_graph(1)
    
    # Should not change anything
    assert surfer.current_page == original_page
    assert len(surfer.previous_pages) == 0


def test_update_graph_go_back():
    """Test update_graph going back to previous page."""
    with patch('builtins.input', return_value='Python_(programming_language)'):
        surfer = WikipediaSurfer("test")
    
    # Create a fake previous page
    prev_page = WikipediaPage("Test_page")
    surfer.previous_pages.append(prev_page)
    original_current = surfer.current_page
    
    surfer.update_graph(2)
    
    # Should go back to previous page
    assert surfer.current_page == prev_page
    assert len(surfer.previous_pages) == 0


def test_update_graph_navigate_forward():
    """Test update_graph navigating to a new page."""
    with patch('builtins.input', return_value='Python_(programming_language)'):
        surfer = WikipediaSurfer("test")
    
    original_page = surfer.current_page
    original_children_count = len(original_page.children)
    
    # Navigate to first link (choice 2 when no previous pages)
    surfer.update_graph(2)
    
    # Should have moved to new page
    assert surfer.current_page != original_page
    
    # Original page should be in previous_pages
    assert original_page in surfer.previous_pages
    
    # New page should be child of original
    assert len(original_page.children) == original_children_count + 1


def test_webpages_so_far_single_page():
    """Test webpages_so_far with only root page."""
    with patch('builtins.input', return_value='Python_(programming_language)'):
        surfer = WikipediaSurfer("test")
    
    pages = surfer.webpages_so_far
    
    assert len(pages) == 1
    assert surfer.root in pages


def test_webpages_so_far_multiple_pages():
    """Test webpages_so_far after navigating."""
    with patch('builtins.input', return_value='Python_(programming_language)'):
        surfer = WikipediaSurfer("test")
    
    # Navigate to a page
    surfer.update_graph(2)
    
    pages = surfer.webpages_so_far
    
    # Should have at least 2 pages
    assert len(pages) >= 2
    assert surfer.root in pages


def test_str_representation():
    """Test string representation of WikipediaSurfer."""
    with patch('builtins.input', return_value='Python_(programming_language)'):
        surfer = WikipediaSurfer("test")
    
    str_repr = str(surfer)
    
    assert isinstance(str_repr, str)
    assert "Python_(programming_language)" in str_repr or "Python (programming language)" in str_repr


def test_display_page():
    """Test display_page prints correct information."""
    with patch('builtins.input', return_value='Python_(programming_language)'):
        surfer = WikipediaSurfer("effervescence")
    
    with patch('builtins.print') as mock_print:
        surfer.display_page()
        
        # Check that print was called
        assert mock_print.call_count > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])