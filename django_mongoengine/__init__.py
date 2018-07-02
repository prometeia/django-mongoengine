from .document import Document, DynamicDocument, EmbeddedDocument, DynamicEmbeddedDocument
from .queryset import QuerySet, QuerySetNoCache


from . import monkeypatch

__all__ = ["QuerySet", "QuerySetNoCache", "Document", "DynamicDocument", "EmbeddedDocument", "DynamicEmbeddedDocument"]

default_app_config = 'django_mongoengine.apps.DjangoMongoEngineConfig'
