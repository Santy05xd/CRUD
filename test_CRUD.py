import unittest
import logica_CRUD

class TestCRUD(unittest.TestCase):

    def setUp(self):
        # Vacía la base de datos antes de cada prueba para tener un estado limpio
        logica_CRUD.database.clear()

    def test_create(self):
        self.assertTrue(logica_CRUD.create("Alice", "25"))
        self.assertEqual(len(logica_CRUD.database), 1)
        self.assertEqual(logica_CRUD.database[0], {"name": "Alice", "age": "25"})
        # Prueba la creación con datos inválidos
        self.assertFalse(logica_CRUD.create("", "25"))
        self.assertFalse(logica_CRUD.create("Bob", ""))

    def test_read(self):
        logica_CRUD.create("Alice", "25")
        self.assertEqual(logica_CRUD.read(0), {"name": "Alice", "age": "25"})
        self.assertIsNone(logica_CRUD.read(1))

    def test_update(self):
        logica_CRUD.create("Alice", "25")
        self.assertTrue(logica_CRUD.update(0, "Alicia", "26"))
        self.assertEqual(logica_CRUD.database[0], {"name": "Alicia", "age": "26"})
        # Prueba actualización con datos inválidos
        self.assertFalse(logica_CRUD.update(0, "", "26"))
        self.assertFalse(logica_CRUD.update(0, "Alicia", ""))

    def test_delete(self):
        logica_CRUD.create("Alice", "25")
        self.assertTrue(logica_CRUD.delete(0))
        self.assertEqual(len(logica_CRUD.database), 0)
        # Prueba eliminar un índice no válido
        self.assertFalse(logica_CRUD.delete(0))

if __name__ == "__main__":
    unittest.main()
