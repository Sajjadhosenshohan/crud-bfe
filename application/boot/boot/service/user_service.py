from pweb import url_for
from boot.form.user_form import UserCreateForm, UserUpdateForm, UserDetailsForm
from boot.model.user import User
from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD


class UserService:
    form_data_crud = FormDataCRUD(model=User)

    def create(self):
        params = {"button": "Create", "action": url_for("user_controller.create")}
        form = UserCreateForm()
        return self.form_data_crud.create(view_name="user/form", form=form, redirect_url=url_for("user_controller.list"), params=params)

    def update(self, model_id: int):
        params = {"button": "Update", "action": url_for("user_controller.update", id=model_id)}
        form = UserUpdateForm()
        return self.form_data_crud.update(view_name="user/form", model_id=model_id, update_form=form, redirect_url=url_for("user_controller.list"), params=params)

    def details(self, model_id: int):
        form = UserDetailsForm()
        return self.form_data_crud.details("user/details", model_id=model_id, redirect_url=url_for("user_controller.list"), display_from=form)

    def delete(self, model_id: int):
        return self.form_data_crud.delete(model_id=model_id, redirect_url=url_for("user_controller.list"))

    def list(self):
        search_fields = ["name", "email"]
        return self.form_data_crud.paginated_list(view_name="user/list", search_fields=search_fields)