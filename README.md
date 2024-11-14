# Browser History Stack Implementation

A Python implementation of a browser history manager using a stack data structure.

## Features

- Add new pages to browsing history
- Remove recently visited pages
- View total page count
- Check if history is empty

## Usage

```python
from history import BrowsingHistory

# Create a new browsing history instance
history = BrowsingHistory()

# Add pages to history
history.add_page("https://example.com")
history.add_page("https://example.com/about")

# Check page count
history.view_page_count()  # Returns: 2

# Remove last visited page
history.remove_page()  # Removes: "https://example.com/about"

# Check if history is empty
history.is_empty()  # Returns: False
