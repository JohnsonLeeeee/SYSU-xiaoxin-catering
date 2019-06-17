

class CategoryViewModel:
    @classmethod
    def category(cls,category):
        return dict(
            name=category.name,
            weight=category.weight
        )

