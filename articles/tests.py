from django.test import Client, TestCase
from django.contrib.auth import get_user_model
# from rest_framework.test import APIClient, APIRequestFactory


from .models import Article, Author
# from .views import AdminAuthorViewSet


class ItemTests(TestCase):

    def setUp(self):
        self.user_super = get_user_model().objects.create_superuser(
            username='user_super',
            email='super@email.com',
            password='testpass123',
        )

        self.user_simple = get_user_model().objects.create_user(
            username='user_simple',
            email='simple@email.com',
            password='testpass123',
        )

        self.author1 = Author.objects.create(
            name='author1',
            picture='pic1'
        )
        self.id_aut1 = self.author1.id

        self.article1 = Article.objects.create(
            author=self.author1,
            category='cat1 cat2',
            title='title1',
            summary='summary1',
            firstParagraph='paragraph1',
            body='body1'
        )
        self.id_art1 = self.article1.id

        self.article2 = Article.objects.create(
            author=self.author1,
            category='cat2 cat3',
            title='title2',
            summary='summary2',
            firstParagraph='paragraph2',
            body='body2'
        )

    """Article List (/api/articles/)"""

    def test_article_list_annon(self):
        response = self.client.get('/api/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'title1')
        self.assertNotContains(response, 'firstParagraph')

    def test_article_list_super(self):
        self.client.login(username='user_super', password='testpass123')
        response = self.client.get('/api/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'title1')
        self.assertNotContains(response, 'firstParagraph')

    def test_article_list_filter_one_result(self):
        self.client.login(username='user_super', password='testpass123')
        response = self.client.get('/api/articles/?category=cat1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'title1')
        self.assertNotContains(response, 'title2')

    def test_article_list_filter_two_results(self):
        self.client.login(username='user_super', password='testpass123')
        response = self.client.get('/api/articles/?category=cat2')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'title1')
        self.assertContains(response, 'title2')

    def test_article_list_super_cannot_create_article(self):
        self.client.login(username='user_super', password='testpass123')
        response = self.client.post(
                '/api/articles/',
                {
                    'author': self.id_aut1,
                    'category': 'catx',
                    'title': 'titlex',
                    'summary': 'summaryx',
                    'firstParagraph': 'paragraphx',
                    'body': 'bodyx'
                })
        self.assertEqual(response.status_code, 405)

    """Article Detail (/api/articles/:id/)"""

    def test_article_detail_annon(self):
        response = self.client.get('/api/articles/%s/' % self.id_art1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'firstParagraph')
        self.assertNotContains(response, 'body')

    def test_article_detail_simple(self):
        self.client.login(username='user_simple', password='testpass123')
        response = self.client.get('/api/articles/%s/' % self.id_art1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'firstParagraph')
        self.assertContains(response, 'body')

    """Admin API (/api/admin/)"""

    def test_annon_cannot_access_crud_area(self):
        response = self.client.get('/api/admin/articles/')
        self.assertEqual(response.status_code, 403)

    def test_simple_cannot_access_crud_area(self):
        self.client.login(username='user_simple', password='testpass123')
        response = self.client.get('/api/admin/articles/')
        self.assertEqual(response.status_code, 403)

    def test_super_can_access_crud_area(self):
        self.client.login(username='user_super', password='testpass123')
        response = self.client.get('/api/admin/articles/')
        self.assertEqual(response.status_code, 200)

    def test_super_can_create_author(self):
        self.client.login(username='user_super', password='testpass123')
        response = self.client.post(
            '/api/admin/authors/', {'name': 'author2', 'picture': 'pic2'})
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/api/admin/authors/')
        self.assertContains(response, 'pic2')

    def test_super_can_create_article(self):
        self.client.login(username='user_super', password='testpass123')
        response = self.client.post(
                '/api/admin/articles/',
                {
                    'author': self.id_aut1,
                    'category': 'catx',
                    'title': 'titlex',
                    'summary': 'summaryx',
                    'firstParagraph': 'paragraphx',
                    'body': 'bodyx'
                })
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/api/admin/articles/')
        self.assertContains(response, 'titlex')

    # def test_super_can_update_author(self):
    #     self.factory = APIRequestFactory()
    #     self.client.login(username='user_super', password='testpass123')
    #     response = self.client.get('/api/articles/')
    #     csrftoken = response.cookies['csrftoken']
    #     view = AdminAuthorViewSet.as_view({'put': 'retrieve'})
    #     request = self.factory.put(
    #         '/api/admin/authors/%s/' % self.id_aut1, {'name': 'author9', 'picture': 'pic9'}, headers={'X-CSRFToken': csrftoken})
    #     response = view(request)
    #     response = self.client.get('/api/admin/authors/%s/' % self.id_aut1)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertNotContains(response, 'pic1')
    #     self.assertContains(response, 'pic9')
