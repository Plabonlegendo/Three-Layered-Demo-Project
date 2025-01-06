from datetime import datetime


def custom_encoder(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
