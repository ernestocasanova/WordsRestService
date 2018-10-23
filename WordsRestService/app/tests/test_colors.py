from django.urls import reverse, resolve
from mixer.backend.django import mixer
from app.utils.colors import Colors
import pytest

@pytest.mark.django_db
class TestColors:
   
    gray = '#D3D3D3'

    def test_color_nonestring_returns_random(self):
        words=""
        color = Colors.get_color(words, len(words.split(' ')))
        assert color != self.gray

    def test_color_spacesinstring_returns_random(self):
        words="  ksjd jsakd jkasjd       lka s                 "
        color = Colors.get_color(words, len(words.split(' ')))
        assert color != self.gray

    def test_color_spaceinstring_returns_random(self):
        words=" "
        color = Colors.get_color(words, len(words.split(' ')))
        assert color != self.gray

    def test_color_lesshundred_returns_notgray(self):
        words="My test case one"
        color = Colors.get_color(words, len(words.split(' ')))
        assert color != self.gray

    def test_color_lesshundred_returns_random(self):
        words="My test case one"
        color = Colors.get_color(words, len(words.split(' ')))
        assert color != self.gray

    def test_color_overthanhundred_returns_gray(self):
        words="My test case one  My test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case one My test case one  My test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case one"
        color = Colors.get_color(words, len(words.split(' ')))
        assert color == self.gray

    def test_color_equaltohundred_returns_gray(self):
        words="My test case one  My test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case one My test case one  My test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy test case oneMy"
        color = Colors.get_color(words, len(words.split(' ')))
        assert color == self.gray