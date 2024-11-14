class BrowsingHistory:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.history_stack = []

    def add_page(self, page_url):
        """Adds a new page to the browsing history."""
        self.history_stack.append(page_url)
        print(f"Page '{page_url}' added to browsing history.")

    def remove_page(self):
        """Removes the most recently visited page from the browsing history."""
        if not self.is_empty():
            removed_page = self.history_stack.pop()
            print(f"Page '{removed_page}' removed from browsing history.")
            return removed_page
        else:
            print("Browsing history is empty. No page to remove.")
            return None

    def view_page_count(self):
        """Returns the number of pages in the browsing history."""
        count = len(self.history_stack)
        print(f"You have viewed {count} pages in this session.")
        return count

    def is_empty(self):
        """Checks if the browsing history is empty."""
        empty = len(self.history_stack) == 0
        if empty:
            print("The browsing history is currently empty.")
        else:
            print("The browsing history is not empty.")
        return empty
