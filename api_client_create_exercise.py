from clients.courses.courses_client import CreateCourseRequestDict, get_courses_client
from clients.exercises.exercises_client import CreateExerciseRequestDict, get_exercise_client
from clients.files.files_clients import CreateFileRequestDict, get_files_client
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import CreateUserRequestDict, get_public_users_client
from tools.fakers import get_random_email


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email= get_random_email(),
    password= 'string',
    lastName = 'string',
    firstName = 'string',
    middleName = 'string'
)


create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserDict(email=create_user_request['email'] , password= create_user_request['password'])

files_client = get_files_client(authentication_user)
course_client = get_courses_client(authentication_user)
exercise_client = get_exercise_client(authentication_user)

create_file_request = CreateFileRequestDict(

    filename= 'iamge.jpg',
    directory = 'exercises',
    url = './testdata/files/image.jpg'

)

create_file_response = files_client.create_file(create_file_request)
print('create file data:', create_file_response)

create_course_request = CreateCourseRequestDict(

    title = 'Python',
    maxScore = 10,
    minScore = 1,
    description = 'Python Course',
    estimatedTime = '2 weeks',
    previewFileId = create_file_response['file']['id'],
    createdByUserId = create_user_response['user']['id']
)

create_course_response = course_client.create_course(create_course_request)
print('Create course data:' , create_course_response)

create_exercise_request = CreateExerciseRequestDict(

    title = 'practice python',
    courseId= create_course_response['course']['id'],
    maxScore = 100,
    minScore = 1,
    orderIndex = 1,
    description = 'practive for improving',
    estimatedTime = '2 hours'

)

create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create exercise data: ', create_course_response)