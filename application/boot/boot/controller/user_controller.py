from boot.service.user_service import UserService
from pweb import Blueprint

user_url_prefix = "/user"

user_controller = Blueprint(
    "user_controller",
    __name__,
    url_prefix=user_url_prefix
)
user_service = UserService()


@user_controller.route("/create", methods=['POST', 'GET'])
def create():
    return user_service.create()


@user_controller.route("/details/<int:id>", methods=['GET'])
def details(id: int):
    return user_service.details(id)


@user_controller.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id: int = None):
    return user_service.update(id)


@user_controller.route("/delete/<int:id>", methods=['GET'])
def delete(id: int):
    return user_service.delete(id)


@user_controller.route("/", methods=['GET'])

@user_controller.route("/list", methods=['GET'])
def list():
    return user_service.list()