from sortedcontainers import SortedSet
import sys

sys.path.append(".")

from src.wikipedia_page import WikipediaPage


class WikipediaSurfer:
    def __init__(self, target_keyword: str) -> None:
        # TODO: Store target_keyword appropriately in WikipediaPage
        # TODO: Ask the user for a start wikipedia page, and keep asking until they
        #       give a keyword that has a wikipedia page. Store it as a
        #       WikipediaPage attribute called "root".
        # TODO: Also create a "current_page" attribute, with the "root" page's value.
        # TODO: Also create a "previous_pages" list, which starts out as an empty list.
        #       As more pages are visited, they will get appended to the end of this list.
        pass

    def list_options(self) -> str:
        # TODO: Return a string message of this format:
        #      "Please select an option:
        #       1: Quit
        #       2: Go back to the previous page
        #       3: <keyword1>
        #       4: <keyword2>
        #       ...""
        #       The <keyword> placeholders should be replaced with all options for wikipedia pages
        #       available on the current_page.
        #       "Go back to the previous page" should only be included as an option if the previous_pages
        #       attribute is not empty.
        pass

    def get_user_choice(self) -> int:
        # TODO: Print the list of options returned by list_options() and get the user's input for their
        #       choice. Keep asking until they enter a valid choice. Return the int for their choice.
        pass

    def update_graph(self, choice: int) -> None:
        # TODO: If the choice is 1, do nothing.
        # TODO: If the choice is 2, update current_page to be the last page in previous_pages.
        #       Remove that page from previous_pages.
        # TODO: If the choice is 3 or higher, update previous_pages to append the current_page,
        #       and get the WikipediaPage corresponding to the chosen option.
        #       Add the chosen option to the children attribute of current_page.
        #       Update current_page to be the WikipediaPage corresponding to the chosen option.
        pass

    def interaction_loop(self) -> None:
        """The main interaction loop for the WikipediaSurfer."""
        quit = False
        while not quit:
            choice = self.get_user_choice()
            quit = choice == 1
            self.update_graph(choice)

    @property
    def webpages_so_far(self) -> SortedSet[WikipediaPage]:
        # TODO: Return the set of all WikipediaPages that have been explored so far.
        #       Do this by traversing the tree of pages, starting from the root.
        #       Avoid getting stuck in cycles by keeping track of which pages have already
        #       been visited. If a page has already been visited, do not visit it again.
        pass

    def __str__(self) -> str:
        # TODO: Return a string containing all keywords that have been explored so far.
        #       The keywords should be in the same order as the WikipediaPages in
        #       webpages_so_far.
        pass

    def __repr__(self) -> str:
        return str(self)
