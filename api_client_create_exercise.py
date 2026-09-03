from clients.courses.courses_client import get_courses_client, \
    CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, \
    CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, \
    CreateUserRequestDict
from tools.fakers import get_random_email

# Создаем пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

public_users_client = get_public_users_client()
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиенты
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

# Загружаем файл
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)

files_client = get_files_client(authentication_user)
create_file_response = files_client.create_file(create_file_request)
print(f"Create file data: {create_file_response}")

# Создаем курс
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)

courses_client = get_courses_client(authentication_user)
create_course_response = courses_client.create_course(create_course_request)
print(f"Create course data: {create_course_response}")

create_exercise_request = CreateExerciseRequestDict(
    title="Java",
    courseId=create_course_response['course']['id'],
    maxScore=0,
    minScore=0,
    orderIndex=0,
    description="No description",
    estimatedTime="To long"
)

exercises_client = get_exercises_client(authentication_user)
create_exercise_response = exercises_client.create_exercise(
    create_exercise_request)
print(f"Create exercise data: {create_exercise_response}")
