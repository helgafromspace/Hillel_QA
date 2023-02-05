class Resources:

    class LoginPage:
        INCORRECT_CREDS_ERROR_MESSAGE = 'Введен неверный логин или пароль.\nРекомендуем вместо логина вводить email.'

    class RegisterPage:
        EMAIL_VALIDITY_MESSAGE = 'Можно использовать данный email для регистрации'
        LOGIN_VALIDITY_MESSAGE = 'Можно использовать данный логин для регистрации'
        EMAIL_INVALIDITY_MESSAGE = 'Введен неверный email адрес'
        LOGIN_INVALIDITY_MESSAGE = 'Логин не может быть менее 3 символов и более 30 символов'
        PASSWORD_INVALIDITY_MESSAGE = 'Длина пароля должна быть не менее 6 символов'
        EMPTY_NAME_ERROR = 'Имя пользователя не может быть пустым'
        LOGIN_FIELD_ERROR = 'Логин не может быть менее 3 символов и более 30 символов'
        EMAIL_FIELD_NOTIFICATION_TEXT = 'Введи действующий email'
        LOGIN_FIELD_NOTIFICATION_TEXT = 'Логин должен должен содержать минимум 3 символа'
        EMAIL_LABEL_TEXT = 'Твой email *'
        LOGIN_LABEL_TEXT = 'Твой логин *'
        PASSWORD_LABEL_TEXT = 'Пароль *'
        SUBMIT_BUTTON_TEXT = 'Зарегистрироваться'