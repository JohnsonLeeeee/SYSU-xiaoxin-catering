
class RestaurantViewModel:
    @classmethod
    def info(self,res):
        return dict(
            name=res.name,
            summary=res.summary
        )



