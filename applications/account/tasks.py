from django.core.mail import send_mail
from main_app.celery import app


@app.task
def send_activation_code(email, code):
    activate_url = f'http://localhost:8000/api/v1/account/activate/{code}'

    send_mail(
        'Активация пользователя',
        activate_url,
        'musabekova.amina13@gmail.com',
        [email],
    )


@app.task
def send_confirmation_code(email, code):
    send_mail(
        'Изменить пароль',
        code,
        'musabekova.amina13@gmail.com',
        [email]
    )
