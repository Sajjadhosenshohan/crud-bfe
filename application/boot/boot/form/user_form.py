from boot.model.user import User
from pweb_form_rest import fields, PWebForm


class UserDetailsForm(PWebForm):

    class Meta:
        model = User
        load_instance = True

    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    email = fields.Email(required=True, error_messages={"required": "Please enter email"})
    address = fields.String(allow_none=True, type="textarea")


class UserCreateForm(UserDetailsForm):
    class Meta:
        model = User
        load_instance = True

    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")


class UserUpdateForm(UserDetailsForm):
    class Meta:
        model = User
        load_instance = True

    id = fields.Integer(required=True, error_messages={"required": "Please enter id"}, type="hidden", isLabel=False)