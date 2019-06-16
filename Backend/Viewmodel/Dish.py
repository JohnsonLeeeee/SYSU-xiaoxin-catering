from ..Model.FoodCategory import FoodCat

class DishViewModel:

    @classmethod
    def dishlist(cls, dish):
        return dict(
            name=dish.name,
            image=dish.main_image,
            price=dish.price,
            category=FoodCat.query.filter_by(id=dish.cid).first().name
        )

    @classmethod
    def detail(cls,dish):
        return dict(
            name=dish.name,
            image=dish.main_image,
            price=dish.price,
            category=FoodCat.query.filter_by(id=dish.cid).first().name,
            summary = dish.summary
        )

