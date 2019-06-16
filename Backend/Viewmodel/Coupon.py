from ..Model.Coupon import Coupon

class CouponViewModel:
    @classmethod
    def coupon(cls,coupon):
        return dict(
            discount=coupon.discount,
            expiration_date=coupon.expiration_date
        )

