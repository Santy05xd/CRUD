# Este archivo contiene la lógica CRUD para pruebas

# Lista que simulará una base de datos en memoria
database = []

# Función para crear un nuevo registro
def create(name, age):
    if name and age:
        database.append({"name": name, "age": age})
        return True
    return False

# Función para leer un registro
def read(index):
    if 0 <= index < len(database):
        return database[index]
    return None

# Función para actualizar un registro
def update(index, name, age):
    if 0 <= index < len(database) and name and age:
        database[index] = {"name": name, "age": age}
        return True
    return False

# Función para eliminar un registro
def delete(index):
    if 0 <= index < len(database):
        database.pop(index)
        return True
    return False
