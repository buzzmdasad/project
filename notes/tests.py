from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase,APIClient
from rest_framework.utils import json

# Create your tests here.
class TestCase(APITestCase):
    def setup(self):
        self.client=APIClient()
    def test_craete_notes(self):
        payload={'title':'test title','notes':'test notes'}
        response=self.client.post('/notes/create/',data=payload,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content=response.content.decode('utf8')
        self.assertJSONEqual(response_content,{"id":1,"title":"test title","notes":"test notes"})
        payload={'title':'demo title','notes':'demo notes'}
        response=self.client.post('/notes/create/',data=payload,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content=response.content.decode('utf8')
        self.assertJSONEqual(response_content,{"id":2,"title":"demo title","notes":"demo notes"})

        response=self.client.get('/notes/list/')
        print('()()()')
        print(response.content)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        print('@@@'+response_content)
        self.assertJSONEqual(response.content,[{"id":1,"title":"test title","notes":"test notes"},
                                               {"id":2,"title":"demo title","notes":"demo notes"}])
    def test_delete_notes(self):
        payload={'title':'test title','notes':'test notes'}
        response=self.client.post('/notes/create/',data=payload,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content=response.content.decode('utf8')
        self.assertJSONEqual(response_content,{"id":1,"title":"test title","notes":"test notes"})
        payload={'title':'demo title','notes':'demo notes'}
        response=self.client.post('/notes/create/',data=payload,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_content=response.content.decode('utf8')
        self.assertJSONEqual(response_content,{"id":2,"title":"demo title","notes":"demo notes"})

        response=self.client.delete('/notes/delete/5')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response_content=response.content.decode('utf8')
        self.assertJSONEqual(response_content,{"detail":"Not found."})

        response.self.client.delete('notes/delete/2')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
