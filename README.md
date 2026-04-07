# 🧠 Sistema de Gestión de Usuarios

El Sistema de Gestión de Usuarios es una aplicación completa diseñada para administrar datos de usuarios de manera eficiente. Proporciona una interfaz basada en menú que permite interactuar con el sistema, creando nuevos usuarios, listando usuarios existentes, buscando, actualizando y eliminando usuarios. El sistema garantiza la validación y consistencia de los datos, convirtiéndolo en una solución confiable para la gestión de información.

## 🚀 Características

- **Gestión de Usuarios**: Crear, listar, buscar, actualizar y eliminar usuarios  
- **Validación de Datos**: Garantiza que la información sea válida y consistente  
- **Interfaz por Menú**: Interfaz fácil de usar para interactuar con el sistema  
- **Almacenamiento en JSON**: Guarda los datos en un archivo JSON para fácil acceso  
- **Manejo de Errores**: Control de excepciones y posibles fallos  

## 🛠️ Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal  
- **JSON**: Formato de almacenamiento de datos  
- **Interfaz por Menú**: Implementada con funciones de entrada/salida de Python  
- **Validación de Datos**: Funciones personalizadas para validar información  
- **Manejo de Errores**: Uso de bloques `try-except`  

## 📦 Instalación

Para instalar el Sistema de Gestión de Usuarios, sigue estos pasos:

1. Clona el repositorio usando `git clone`  
2. Instala las dependencias con `pip install -r requirements.txt`  
3. Ejecuta la aplicación con `python main.py`  

## 💻 Uso

Para usar el sistema, sigue estos pasos:

1. Ejecuta la aplicación con `python main.py`  
2. Interactúa con el menú para gestionar usuarios  
3. Usa la opción `create` para crear un usuario  
4. Usa la opción `list` para listar todos los usuarios  
5. Usa la opción `search` para buscar un usuario  
6. Usa la opción `update` para actualizar un usuario  
7. Usa la opción `delete` para eliminar un usuario  

## 📂 Estructura del Proyecto

```bash
gestion-info/
├─ README.md                         
├─ requirements.txt
├─ .gitignore
├─ data/
│  └─ records.json                # o registros.csv / registros.txt
└─ src/
   ├─ main.py                    # punto de entrada
   ├─ menu.py                    # interfaz de consola (UI)
   ├─ service.py                 # lógica (CRUD)
   ├─ file.py                    # persistencia (leer/guardar)
   ├─ validate.py                # validaciones y helpers
   └─ integration.py             # faker / pandas / requests
```

## 🤝 Contributing
Para contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio usando git fork
2. Realiza cambios y haz commit con git commit
3. Sube los cambios con git push
4. Crea un Pull Request para integrar los cambios

## 📝 License
Este proyecto está bajo la licencia MIT.

