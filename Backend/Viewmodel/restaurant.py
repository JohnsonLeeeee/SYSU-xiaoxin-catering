
class RestaurantViewModel:
    def __init__(self, data):
        self.name = data['name']
        self.host = data['host']
        self.address = '、'.join(data['address'])
        self.image = data['image']
        self.summary = data['summary']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.name, self.address, self.host,self.summary])
        return ' / '.join(intros)


class RestaurantCollection:
    def __init__(self):
        self.total = 0
        self.restaurants = []
        self.keyword = None

    def fill(self, search_restaurant, keyword):
        self.total = search_restaurant.total
        self.restaurants = [RestaurantViewModel(Restaurant) for Restaurant in search_restaurant.restaurants]
        self.keyword = keyword

