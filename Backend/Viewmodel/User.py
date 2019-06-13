
from ..Model.Address import Address

class UserSummary:
    @classmethod
    def user(cls, user):
        return dict(
            name=user.username,
            phone=user.phone_number,
            email=user.email,
            address = Address.query.filter_by(id = user.aid).first().content
        )
