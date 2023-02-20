import unittest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd + '/app')
from server.app import app
from server.database import database, add_student, retrieve_students, retrieve_student, update_student, delete_student,student_helper,student_collection

class TestAPI(unittest.TestCase):
    async def setUp(self):
        self.client = TestClient(app)
        self.student_data = {
            "fullname": "Test Student",
            "email": "test@student.com",
            "course_of_study": "Test Course",
            "year": 2022,
        }
        self.student = database.students_collection.find_one(self.student_data)
        self.student_id = str(self.student["id"])

    async def test_student_helper(self):
        student = student_helper(self.student)
        self.assertIsInstance(student, dict)
        self.assertEqual(student["_id"], self.student_id)
        self.assertEqual(student["fullname"], self.student_data["fullname"])
        self.assertEqual(student["email"], self.student_data["email"])
        self.assertEqual(student["course_of_study"], self.student_data["course_of_study"])
        self.assertEqual(student["year"], self.student_data["year"])

    async def test_add_student(self):
        # test if student is successfully added to the database
        response = self.client.post("/student/", json=self.student_data)
        self.assertEqual(response.status_code, 200)
        student = response.json()
        self.assertIsInstance(student, dict)
        self.assertEqual(student["fullname"], self.student_data["fullname"])
        self.assertEqual(student["email"], self.student_data["email"])
        self.assertEqual(student["course_of_study"], self.student_data["course_of_study"])
        self.assertEqual(student["year"], self.student_data["year"])

    async def test_retrieve_students(self):
        # test if all students are successfully retrieved from the database
        response = self.client.get("/student/")
        self.assertEqual(response.status_code, 200)
        students = response.json()
        self.assertIsInstance(students, list)
        self.assertGreater(len(students), 0)

    async def test_retrieve_student(self):
        # test if a student is successfully retrieved from the database
        response = self.client.get(f"/student/{self.student_id}")
        self.assertEqual(response.status_code, 200)
        student = response.json()
        self.assertIsInstance(student, dict)
        self.assertEqual(student["fullname"], self.student_data["fullname"])
        self.assertEqual(student["email"], self.student_data["email"])
        self.assertEqual(student["course_of_study"], self.student_data["course_of_study"])
        self.assertEqual(student["year"], self.student_data["year"])

    async def test_update_student(self):
        # test if a student is successfully updated in the database
        data = {"year": 4}
        response = self.client.put(f"/student/{self.student_id}", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"detail": "Student updated successfully"})

    async def test_update_student_empty_data(self):
        # test if an empty request body returns False
        data = {}
        result = update_student(self.student_id, data)
        self.assertFalse(result)

    async def test_delete_student(self):
        # test if a student is successfully deleted from the database
        response = self.client.delete(f"/student/{self.student_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"detail": "Student deleted successfully"})


if __name__ == '__main__':
    unittest.main()