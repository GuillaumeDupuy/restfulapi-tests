import requests
import unittest
unittest.TestLoader.sortTestMethodsUsing = lambda *args: -1

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

    def test_add_student(self):
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
    
    def test_update_student(self):
        # test if a student is successfully updated in the database
        data["year"] = 4
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
        self.assertEqual(student["message"], "Student data updated successfully") 

    def test_retrieve_students(self):
        # test if all students are successfully retrieved from the database
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        students = response.json()
        self.assertIsInstance(students, dict)
        self.assertGreater(len(students), 0)
        self.assertEqual(students["message"], "Students data retrieved successfully")
    
    def test_retrieve_student(self):
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

    def test_delete_student(self):
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

if __name__ == '__main__':
    unittest.main()
