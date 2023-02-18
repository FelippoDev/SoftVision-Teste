# SoftVision-Teste
Technical challenge for the vaccancy for a mid-level position.
The Code only contains the backend part.


## Requirements

Before you can run the project, you'll need to have Python3 installed on your system 💻.


## Installation

To install the project and its dependencies, follow these steps:

1. Clone the repository to your local machine 💾
2. Navigate to the project directory in your terminal 💻
3. Run the command ```pip install -r requirements.txt`` inside the working directory, to install the dependencies 🔍


## Running the Project
To run the project, you'll need to do the following:

1. Remove the .env.example file and create a .env file and put the environment variables needed to run the project.
2. Use the command ```flask run```


## Documentation

The API as 3 main functions basically, create an Aluno, Curso and Matricula fields. For the Aluno e Curso datas we have an API for creating, updating, selecting and deleting.

### Aluno Views
Starting with the Aluno data we have the following endpoints: 
```GET /api/aluno/<id>```  for retrieving an Aluno from the database.

```POST /api/create/aluno``` for creating an Aluno. Example of a expected json body: ```{
    "nome": "Jhon Doe",
    "email": "jdoe@gmail.com",
    "cpf": "33133141981341",
    "status": true,
    "data_nascimento": "1992-05-09"
}```

```PUT /api/aluno/<id>``` for updating an Aluno in the database. Example of a expected json body: ``` {
    "nome": "Bond James",
    "cpf": "11255833719",
    "data_nascimento": "1994-10-30"
} ```

```GET /api/aluno/list``` returns a list containing all the Aluno data from the database.

```DELETE /api/aluno/<id>``` deletes an Aluno from the database.

### Curso Views
```GET /api/curso/<id>``` retrieves a Curso from the database.

```POST /api/create/curso``` for creating a Curso data. Example of a expected json body: ```{
    "nome": "Curso Frontend Javascript",
    "preco_venda": 89.90,
    "sequencia": 10,
    "status": true
}```

```PUT /api/curso/<id>``` for updating a Curso in the database. Example of a expected json body: ``` {
    "nome": "Terapia Comportamental",
    "preco_venda": 49.90,
    "sequencia": 4
} ```

```GET /api/curso/list``` returns a list containing all the Curso data from the database.

```DELETE /api/curso/<id>``` deletes a Curso from the database.


### Matricula View
``` POST /api/<aluno_id>/matricular/<curso_id> ``` This endpoints establish a many to many relation with the Aluno and the Curso Tables.

```GET /api/matriculas``` returns all Matriculas made.
 
 ``` PUT /api/matriculas``` update the status of an Matricula in the database.
