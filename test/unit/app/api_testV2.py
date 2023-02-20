import unittest
import asyncio
from bson.objectid import ObjectId
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd + '/app')
from server.app import app
from server.database import add_student, delete_student, retrieve_student, update_student


test_student = {
    "fullname": "Test Student",
    "email": "test@student.com",
    "course_of_study": "Test Course",
    "year": 2022,
}

class TestAPI(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        # Insert a test student in the database before each test
        self.test_student_id = str((await add_student(test_student))["id"])

    async def asyncTearDown(self):
        # Delete the test student from the database after each test
        await delete_student(self.test_student_id)

    async def test_retrieve_students(self):
        response = await app.test_client.get("/student/")
        self.assertEqual(response.status_code, 200)
        students = await response.json()
        self.assertIsInstance(students, list)

    async def test_add_student(self):
        new_student = {
            "fullname": "New Student",
            "email": "new@student.com",
            "course_of_study": "New Course",
            "year": 2023,
        }
        response = await app.test_client.post("/student/", json=new_student)
        self.assertEqual(response.status_code, 201)
        student = await response.json()
        self.assertIsInstance(student, dict)
        self.assertIn("id", student)
        self.assertEqual(student["fullname"], new_student["fullname"])
        await delete_student(student["id"])

    async def test_retrieve_student(self):
        response = await app.test_client.get(f"/student/{self.test_student_id}")
        self.assertEqual(response.status_code, 200)
        student = await response.json()
        self.assertIsInstance(student, dict)
        self.assertEqual(student["id"], self.test_student_id)

    async def test_update_student(self):
        new_data = {"year": 2024}
        response = await app.test_client.put(f"/student/{self.test_student_id}", json=new_data)
        self.assertEqual(response.status_code, 200)
        updated = await update_student(self.test_student_id, new_data)
        self.assertTrue(updated)

    async def test_delete_student(self):
        response = await app.test_client.delete(f"/student/{self.test_student_id}")
        self.assertEqual(response.status_code, 200)
        deleted = await delete_student(self.test_student_id)
        self.assertTrue(deleted)

if __name__ == '__main__':
    unittest.main()