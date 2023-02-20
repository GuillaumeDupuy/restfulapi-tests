import json
from bson.objectid import ObjectId
from fastapi.testclient import TestClient
import aiohttp
import sys
import os
#cwd = os.getcwd()
#sys.path.append(cwd + '/app')
import app

client = TestClient(app)
print("Hey !:"+client)
def test_retrieve_students():
    response = client.get("/student")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0


# class TestAPI(asynctest.TestCase):

#     # On utilise setUp et tearDown pour préparer et nettoyer les tests
#     # dans notre cas, on insère des données de test avant les tests, et on les supprime après.
#     async def setUp(self):
#         self.client = TestClient(app)

#         # Insérer des données de test
#         file = "json/test.json"
#         data = json.load(open(file))
#         for item in data:
#             response = await self.client.post("/student", json=item)


#     async def tearDown(self):
#         # Supprimer les données de test
#         await self.client.delete("/student")


#     # Tester la récupération de tous les étudiants
#     async def test_retrieve_students(self):
#         response = await client.get("/student")
#         self.assertEqual(response.status_code, 200)
#         data = response.json()
#         self.assertTrue(len(data) > 0)

#     # Tester la récupération d'un étudiant avec un ID correspondant
#     async def test_retrieve_student(self):
#         response = await client.post("/student", json={
#             "fullname": "Test Student",
#             "email": "test@student.com",
#             "course_of_study": "Test Course",
#             "year": 5
#         })
#         data = response.json()
#         id = data["_id"]
#         response = await client.get(f"/student/{id}")
#         self.assertEqual(response.status_code, 200)
#         data = response.json()
#         self.assertEqual(data["fullname"], "Test Student")
#         self.assertEqual(data["email"], "test@student.com")
#         self.assertEqual(data["course_of_study"], "Test Course")
#         self.assertEqual(data["year"], 5)

#     # Tester l'ajout d'un étudiant
#     async def test_add_student(self):
#         response = await client.post("/student", json={
#             "fullname": "Test Student",
#             "email": "test@student.com",
#             "course_of_study": "Test Course",
#             "year": 5
#         })
#         self.assertEqual(response.status_code, 200)
#         data = response.json()
#         self.assertTrue("_id" in data)
#         self.assertEqual(data["fullname"], "Test Student")
#         self.assertEqual(data["email"], "test@student.com")
#         self.assertEqual(data["course_of_study"], "Test Course")
#         self.assertEqual(data["year"], 5)

#     # Tester la mise à jour d'un étudiant
#     async def test_update_student(self):
#         response = await client.post("/student", json={
#             "fullname": "Test Student",
#             "email": "test@student.com",
#             "course_of_study": "Test Course",
#             "year": 5
#         })
#         data = response.json()
#         id = data["_id"]
#         response = await client.put(f"/student/{id}", json={
#             "fullname": "New Test Student",
#             "email": "newtest@student.com",
#             "course_of_study": "New Test Course",
#             "year": 6
#         })
#         self.assertEqual(response.status_code, 200)
#         data = response.json()
#         self.assertEqual(data["_id"], id)
#         self.assertEqual(data["fullname"], "New Test Student")
#         self.assertEqual(data["email"], "newtest@student.com")
#         self.assertEqual(data["course_of_study"], "New Test Course")
#         self.assertEqual(data["year"], 6)

#     # Tester la suppression d'un étudiant
#     async def test_delete_student(self):
#         # Ajouter un étudiant pour le supprimer ensuite
#         response = await client.post("/student", json={
#             "fullname": "Test Student",
#             "email": "test@student.com",
#             "course_of_study": "Test Course",
#             "year": 5
#         })
#         student_id = response.json()["_id"]

#         # Supprimer l'étudiant ajouté précédemment
#         response = await client.delete(f"/student/{student_id}")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), {"message": "Student deleted"})

#         # Vérifier que l'étudiant a bien été supprimé
#         response = await client.get(f"/student/{student_id}")
#         self.assertEqual(response.status_code, 404)

