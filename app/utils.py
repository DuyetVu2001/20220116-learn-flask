def as_dict(obj):
    """
        Convert SQLAlchemy class to dict
    """
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
