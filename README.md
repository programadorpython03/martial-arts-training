# martial-arts-training-api

API for managing martial arts students, tracking their progress, and recording completed classes.

## Repository

- GitHub: [github.com/your-username/martial-arts-training-api](https://github.com/programadorpython03/martial-arts-training-api)

## Features

- Student Management (CRUD operations)
- Progress Tracking
- Class Completion Recording
- Belt Progression System

## Endpoints

### Students

#### Create Student
- **POST** `/`
- Creates a new student
- Request Body: `AlunosSchema`
- Response: Student details

#### List Students
- **GET** `/alunos/`
- Returns a list of all students
- Response: Array of `AlunosSchema`

#### Update Student
- **PUT** `/atualizar_aluno/{aluno_id}`
- Updates student information
- Request Body: `AlunosSchema`
- Response: Updated student details
- Note: Students under 18 cannot receive certain belt ranks (A, R, M, P)

### Progress Tracking

#### Student Progress
- **GET** `/progresso_aluno/`
- Query Parameters: `email_aluno`
- Returns student's progress information including:
  - Current belt
  - Total completed classes
  - Classes needed for next belt promotion

### Class Management

#### Record Completed Class
- **POST** `/aula_realizada/`
- Records completed classes for a student
- Request Body: `AulaRealizadaSchema` (includes quantity and student email)
- Response: Success message

## Data Models

### Alunos (Students)
- email
- nome (name)
- data_nascimento (birth date)
- faixa (belt rank)

### AulasConcluidas (Completed Classes)
- aluno (student reference)
- faixa_atual (current belt)

## Requirements

- Django
- Django Ninja
- Python 3.x

## Installation

1. Clone the repository
2. Install dependencies
3. Run migrations
4. Start the server

## Usage

Make HTTP requests to the API endpoints using your preferred HTTP client or tool.