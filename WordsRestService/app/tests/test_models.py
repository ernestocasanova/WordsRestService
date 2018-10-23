from mixer.backend.django import mixer
from app.api.models import Words
import pytest

@pytest.mark.django_db
class TestModels:
    
    def test_words_exists_in(self):
        mixer.blend('app.Words')
        word = Words.objects.get(pk=1)
        assert word != [] 

    def test_words_create_new(self):
        word = mixer.blend('app.Words', words="My test case one")
        assert word != []

    def test_words_get_one(self):
        mixer.blend('app.Words')
        word = Words.objects.get(pk=1)
        assert word != []

    def test_words_delete_one(self):
        mixer.blend('app.Words')
        word = Words.objects.filter(id=1).delete()
        assert word != []

    def test_words_hexa_iscolor(self):
        word = mixer.blend('app.Words', words="My test case one")
        assert word.color != '#D3D3D3' 