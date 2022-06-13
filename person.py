import re


class Person:
    def allowed_to_enter(self, age):
        if age > 20:
            return True

    def allowed_to_deny(self, age):
        if age < 20:
            return False
