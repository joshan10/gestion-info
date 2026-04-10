# 🧠 Sistema de Gestión de Usuarios en Python

## 📌 Descripción

Este proyecto es un sistema de gestión de usuarios desarrollado en Python.
Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) con persistencia en archivos JSON, siguiendo buenas prácticas de desarrollo.

Además, incluye un menú dinámico para ejecutar ejercicios independientes desde la carpeta `assets`.

---

## 🚀 Funcionalidades

### 🔹 Gestión de usuarios

* Crear usuarios
* Listar usuarios
* Buscar usuarios por ID
* Actualizar usuarios
* Eliminar usuarios
* Persistencia en archivo JSON

### 🔹 Integraciones

* Importación de datos desde API usando `requests`

### 🔹 Ejercicios

* Menú dinámico que detecta automáticamente archivos `exerciseX.py`
* Ejecución independiente de cada ejercicio

### 🔹 Testing

* Pruebas automatizadas con `pytest`

---

## 🗂️ Estructura del proyecto

```
gestion-info/
├─ src/
│  ├─ main.py
│  ├─ menu.py
│  ├─ service.py
│  ├─ file.py
│  ├─ validate.py
│  ├─ integration.py
│  ├─ exercises_menu.py
│  └─ __init__.py
├─ assets/
│  ├─ exercise1.py
│  ├─ exercise2.py
│  ├─ exercise3.py
│  ├─ exercise4.py
│  ├─ exercise5.py
│  ├─ exercise6.py
│  └─ test_exercise6.py
├─ tests/
│  └─ test_service.py
├─ data/
│  └─ records.json
├─ requirements.txt
├─ pytest.ini
└─ README.md
```

---

## ⚙️ Instalación

1. Clonar el repositorio:

```
git clone <URL_DEL_REPO>
cd gestion-info
```

2. Crear entorno virtual:

```
python3 -m venv venv
source venv/bin/activate
```

3. Instalar dependencias:

```
pip install -r requirements.txt
```

---

## ▶️ Ejecución del programa

Ejecutar desde la raíz del proyecto:

```
python -m src.main
```

---

## 🧪 Ejecutar pruebas

```
pytest
```

---

## 🧠 Ejecución de ejercicios

Desde el menú principal, selecciona la opción de ejercicios para ejecutar los archivos dentro de la carpeta `assets`.

Cada ejercicio debe contener una función `main()`.

---

## 🛠 Tecnologías utilizadas

* Python 3
* JSON (persistencia de datos)
* colorama (interfaz en consola)
* requests (consumo de API)
* pytest (pruebas automatizadas)

---

## 📌 Buenas prácticas aplicadas

* Código modular (separación por responsabilidades)
* Uso de estructuras de datos (listas, diccionarios, sets)
* Manejo de errores con try-except
* Validaciones centralizadas
* Uso de `**kwargs` en funciones dinámicas
* Uso de imports absolutos
* Testing automatizado

---

## 👨‍💻 Autor

Proyecto desarrollado como parte de formación en programación y desarrollo backend en Python.
by joshan pereira
