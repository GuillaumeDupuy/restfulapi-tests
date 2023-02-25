import requests
import unittest

# assuming your FastAPI app is running on localhost:8000
url = 'http://localhost:8000/student'

# create a new student
data = {
    "fullname": "Test Student",
    "email": "test@student.com",
    "course_of_study": "Test Course",
    "year": 2
}

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.student_data = data

    def test_00_add_student(self):
        # test if student is successfully added to the database
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        student = response.json()
        self.assertIsInstance(student, dict)
        self.assertEqual(student["data"][0]["fullname"], self.student_data["fullname"])
        self.assertEqual(student["data"][0]["email"], self.student_data["email"])
        self.assertEqual(student["data"][0]["course_of_study"], self.student_data["course_of_study"])
        self.assertEqual(student["data"][0]["year"], self.student_data["year"])
        self.assertEqual(student["message"], "Student added successfully.")
    
    def test_01_update_student(self):
        # test if a student is successfully updated in the database
        self.student_data["year"] = 4
        response = requests.get(url)
        old_student = response.json()
        for i in range(0, len(old_student["data"][0])):
            if old_student["data"][0][i]["fullname"] == "Test Student":
                id_student = old_student["data"][0][i]["id"]
                break
        response = requests.put(f"{url}/{id_student}", json=data)
        self.assertEqual(response.status_code, 200)
        student = response.json()
        self.assertIsInstance(student, dict)
        self.assertEqual(student["data"][0], f"Student with ID: {id_student} update is successful")
        self.assertEqual(student["message"], "Student data updated successfully")

    def test_02_update_nonexistent_student(self):
        # test if an error response is returned when updating a nonexistent student
        id_student = "63fa0d6af9f464bdf1303b88"
        response = requests.put(f"{url}/{id_student}", json=data)
        self.assertEqual(response.status_code, 200)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertEqual(error["error"], "An error occurred")
        self.assertEqual(error["code"], 404)
        self.assertEqual(error["message"], "There was an error updating the student data.")

    def test_03_retrieve_students(self):
        # test if all students are successfully retrieved from the database
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        students = response.json()
        self.assertIsInstance(students, dict)
        self.assertGreater(len(students), 0)
        self.assertEqual(students["message"], "Students data retrieved successfully")
    
    def test_04_retrieve_student(self):
        # test if a student is successfully retrieved from the database
        response = requests.get(url)
        old_student = response.json()
        for i in range(0, len(old_student["data"][0])):
            if old_student["data"][0][i]["fullname"] == "Test Student":
                id_student = old_student["data"][0][i]["id"]
                break
        response = requests.get(f"{url}/{id_student}")
        self.assertEqual(response.status_code, 200)
        student = response.json()
        self.assertIsInstance(student, dict)
        self.assertEqual(student["message"], "Student data retrieved successfully")

    def test_05_get_nonexistent_student(self):
        # test if an error response is returned when getting a nonexistent student
        id_student = "63fa0d6af9f464bdf1303b88"
        response = requests.get(f"{url}/{id_student}")
        self.assertEqual(response.status_code, 200)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertEqual(error["error"], "An error occurred")
        self.assertEqual(error["code"], 404)
        self.assertEqual(error["message"], "Student doesn't exist.")

    def test_06_delete_student(self):
        # test if a student is successfully deleted from the database
        response = requests.get(url)
        old_student = response.json()
        for i in range(0, len(old_student["data"][0])):
            if old_student["data"][0][i]["fullname"] == "Test Student":
                id_student = old_student["data"][0][i]["id"]
                break
        response = requests.delete(f"{url}/{id_student}")
        self.assertEqual(response.status_code, 200)
        student = response.json()
        self.assertIsInstance(student, dict)
        self.assertEqual(student["message"], "Student deleted successfully")
    
    def test_07_delete_nonexistent_student(self):
        # test if an error response is returned when deleting a nonexistent student
        id_student = "63fa0d6af9f464bdf1303b88"
        response = requests.delete(f"{url}/{id_student}")
        self.assertEqual(response.status_code, 200)
        error = response.json()
        self.assertIsInstance(error, dict)
        self.assertEqual(error["error"], "An error occurred")
        self.assertEqual(error["code"], 404)
        self.assertEqual(error["message"], f"Student with id {id_student} doesn't exist")

if __name__ == '__main__':
    unittest.main()
