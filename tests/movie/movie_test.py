from pages.movie.movie_page import MoviePage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time

@pytest.mark.usefixtures("oneTimeSetUp","setUp")

class MovieTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.movie = MoviePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_ValidMoviePage(self):
        self.movie.SearchBox()
        time.sleep(5)
        self.movie.MovieTickets("Thalaivan Thalaivii")
        time.sleep(5)
        self.movie.Moviebox()
        time.sleep(5)
        self.movie.BookTickets()
        time.sleep(5)