from rest_framework.exceptions import AuthenticationFailed, APIException

from django.contrib.auth.hashers import check_password, make_password

from accounts.models import User

from companies.models import Enterprise, Employee


class Authentication:
    def signin(self, email=None, password=None) -> None:
        exception_auth = AuthenticationFailed('Email e/ou senha incorreto(s) !')

        user_exists = User.objects.filter(email=email).exists()
        
        if not user_exists:
            raise exception_auth
        
        user = User.objects.filter(email=email).first()

        if not check_password(password, user.password):
            raise exception_auth

        return user
    

    def signup(self, name, email, password, type_account='owner', company_id=False):
        if not name or name == '':
            raise APIException('Nome é obrigatório !')
        
        if not email or email == '':
            raise APIException('Email é obrigatório !')
        
        if not password or password == '':
            raise APIException('A senha é obrigatória !')
        
        if type_account =='employee' and not company_id:
            raise APIException('Empresa é obrigatória !')
        

        user = User
        if user.objects.filter(email=email).exists():
            raise APIException('Email já cadastrado !')
        
        password_hashed = make_password(password)

        created_user = user.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=0 if type_account == 'owner' else 1
        )

        if type_account == 'owner':
            Enterprise.objects.create(
                name='Nome da Empresa',
                user_id=created_user.id
            )

        if type_account == 'employee':
            Employee.objects.create(
                enterprise_id=company_id or created_enterprise.id,
                user_id=created_user.id  
            )
        return created_user