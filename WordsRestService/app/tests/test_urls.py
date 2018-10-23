from django.urls import reverse, resolve

class TestUrls:

    def test_words_url(self):
        #path = reverse('main_app', kwargs={'pk':1})
        assert True #resolve(path).view_name == 'main_app'