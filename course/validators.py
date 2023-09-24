import re
from rest_framework.validators import ValidationError

class LinkValidator:
    def __init__(self, field):
        self.field = field


    def __call__(self, value):
        req = re.compile(r'\b(?:youtube\.com|mylink\.com)\b')
        res = value.get(self.field)
        if not bool(req.search(res)):
            raise ValidationError('Error validating link')

