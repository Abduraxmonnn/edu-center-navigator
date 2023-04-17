import json
import random

SUBJECT = {
    "EN": "Your account verification code",
    "RU": "Код подтверждения вашей учетной записи",
    "UZ": "Elektron pochta tasdiqlovchi kod"
}

OTP_CODE = random.randint(100000, 999999)

MESSAGE = {
    "EN": "Hellooooo!!!\n\n"
          "Wowwee! Thanks for registering an account with TCB (Training Centers Base)! You're the coolest person in all the land."
          "Before we get started, we'll need to verify your email.\n\n"
          "Your verify code is:\n\n\n"
          f"\t\t\t\t{OTP_CODE}\n\n\n\n"
          f"Thank you for your trust\n"
          f"Welcome to TCB!\n",
    "RU": "Приветоооо!!!\n\n"
          "Спасибо за регистрацию учетной записи в TCB (Training Centers Base)! Ты самый крутой человек на всей земле."
          "Прежде чем мы начнем, нам необходимо подтвердить вашу электронную почту.\n\n"
          "Ваш код подтверждения:\n\n\n"
          f"\t\t\t\t{OTP_CODE}\n\n\n\n"
          f"Спасибо за ваше доверие\n"
          f"Добро пожаловать в TCB!\n",
    "UZ": "Salommm!!!\n\n"
          "TCB (Training Centers Base) da akkauntni ro'yxatdan o'tkazganingiz uchun tashakkur! Siz butun mamlakatdagi eng zo'r odamsiz."
          "Ishni boshlashdan oldin elektron pochta manzilingizni tekshirishimiz kerak.\n\n"
          "Tasdiqlash kodingiz:\n\n\n"
          f"\t\t\t\t{OTP_CODE}\n\n\n\n"
          f"Ishonchingiz uchun rahmat\n"
          f"TCBga xush kelibsiz!\n",
}
