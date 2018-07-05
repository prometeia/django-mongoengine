from mongoengine import common
field = common._import_class("ObjectIdField")
setattr(field, "verbose_name", None)
setattr(field, "help_text", None)
