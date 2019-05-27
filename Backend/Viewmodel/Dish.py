from ..Model.restaurant import restaurant

class DishViewModel:
    @classmethod
    def dish(cls, dish):
        return dict(
            name=dish.name,
            image=dish.main_image,
            price=dish.price,
            restaurant=restaurant.query.filter_by(id=dish.rid).first().name
        )