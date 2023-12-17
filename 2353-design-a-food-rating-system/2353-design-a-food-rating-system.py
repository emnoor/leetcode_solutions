import bisect


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating = {}
        self.food_cuisine = {}
        self.cuisine_foods = {}
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_rating[food] = rating
            self.food_cuisine[food] = cuisine
            self.cuisine_foods.setdefault(cuisine, [])
            self._insert_into_cuisine_foods(food)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine[food]
        index = bisect.bisect_left(
            self.cuisine_foods[cuisine],
            (-self.food_rating[food], food),
        )
        #print(f'changeRating {food=} {cuisine=} {index=} {self.food_rating=} {self.food_cuisine=} {self.cuisine_foods=}')
        self.cuisine_foods[cuisine].pop(index)
        self.food_rating[food] = newRating
        self._insert_into_cuisine_foods(food)

    def highestRated(self, cuisine: str) -> str:
        #print(f"highestRated {cuisine=} {self.food_rating=} {self.food_cuisine=} {self.cuisine_foods=}")
        return self.cuisine_foods[cuisine][0][1]
    
    def _insert_into_cuisine_foods(self, food: str) -> None:
        cuisine = self.food_cuisine[food]
        bisect.insort_left(
            self.cuisine_foods[cuisine],
            (-self.food_rating[food], food),
        )


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)