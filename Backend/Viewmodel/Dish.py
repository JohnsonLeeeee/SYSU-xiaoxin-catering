from ..Model.FoodCategory import FoodCat
def buildimageurl(name):
    return "static/upload/"+name

class DishViewModel:

    @classmethod
    def dishlist(cls, dish):
        return dict(
            id = dish.id,
            name=dish.name,
            image=buildimageurl(dish.main_image),
            price=dish.price,
            category=FoodCat.query.filter_by(id=dish.cid).first().name
        )

    @classmethod
    def detail(cls,dish):
        return dict(
            id = dish.id,
            name=dish.name,
            image=buildimageurl(dish.main_image),
            price=dish.price,
            category=FoodCat.query.filter_by(id=dish.cid).first().name,
            summary = dish.summary
        )

