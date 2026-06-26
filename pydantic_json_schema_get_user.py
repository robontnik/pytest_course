
from clients.courses.courses_client import  get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.files.files_clients import  get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import  AuthenticationUserSchema
from clients.users.private_users_client import get_private_user_client
from clients.users.public_users_client import  get_public_users_client
from clients.users.usersSchema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email = fake.email(),
    password = 'string',
    last_name = 'string',
    first_name = 'string',
    middle_name = 'string'
    )

create_user_response = public_users_client.create_user(create_user_request)

auth_user = AuthenticationUserSchema(email = create_user_request.email, password = create_user_request.password)

private_users_client = get_private_user_client(auth_user)

get_user_response = private_users_client.get_user_api(create_user_response.user.id)

get_user_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(),schema=get_user_response_schema)