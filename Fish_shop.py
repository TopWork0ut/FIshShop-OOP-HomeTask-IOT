import datetime
from multimethod import multimethod


class FishInfo:
    def __init__(self, name: str, price_in_uah_per_kilo: float, origin: str, catch_date: datetime, due_time: datetime):
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = catch_date
        self.due_time = due_time
        self.origin = origin

        if self.due_time > datetime.datetime.now():
            self.age_in_months = (datetime.datetime.now().year - self.catch_date.year) * 12 + (
                    self.due_time.month - self.catch_date.month)
        else:
            self.age_in_months = (self.due_time.year - self.catch_date.year) * 12 + (
                    self.due_time.month - self.catch_date.month)


class Fish(FishInfo):
    def __init__(self, name: str, price_in_uah_per_kilo: float, origin: str, catch_date: datetime, due_time: datetime,
                 weight: float, number: int = 1) -> None:
        super().__init__(name, price_in_uah_per_kilo, origin, catch_date, due_time)
        self.weight = weight
        self.due_time = due_time
        self.catch_date = catch_date
        self.number = number


class FishBox:
    def __init__(self, fish_info: FishInfo, weight: float, package_date: datetime, height: float, width: float,
                 length: float, number: int = 1):
        self.fish_info = fish_info
        self.weight = weight
        self.package_date = package_date
        self.height = height
        self.width = width
        self.length = length
        self.number = number

datetime.datetime()
class FishShop:
    dict_of_boxes_with_fish = {}
    dict_of_boxes_with_frozen_fish = {}
    dict_of_boxes_with_fresh_fish = {}
    dict_of_fishes = {}
    dict_of_fresh_fishes = {}
    dict_of_frozen_fishes = {}

    @multimethod
    def add_fish(self, fish_box: FishBox, number_of_boxes: int = 1) -> None:
        if datetime.datetime.now().year - fish_box.fish_info.catch_date.year < 1:
            self.dict_of_boxes_with_fresh_fish[fish_box.fish_info.name] = fish_box.number
            fish_box.fish_info.price_in_uah_per_kilo *= 1.5

        elif 1 <= datetime.datetime.now().year - fish_box.fish_info.catch_date.year < 2:
            self.dict_of_boxes_with_fish[fish_box.fish_info.name] = fish_box.number
            fish_box.fish_info.price_in_uah_per_kilo *= 1.25

        else:
            self.dict_of_boxes_with_frozen_fish[fish_box.fish_info.name] = fish_box.number

        print("\nWe added " + str(number_of_boxes) + " boxes (" + str(
            (fish_box.weight * number_of_boxes)) +
              ") kg of " + fish_box.fish_info.name)

    @multimethod
    def add_fish(self, fish: Fish) -> None:
        if fish.age_in_months < 1:  # age of the fresh fish is not bigger than 1 month
            self.dict_of_fresh_fishes[fish.name] = fish.number
            fish.price_in_uah_per_kilo *= 1.5

        elif 1 <= fish.age_in_months <= 3:
            self.dict_of_fishes[fish.name] = fish.number
            fish.price_in_uah_per_kilo *= 1.25

        else:
            self.dict_of_frozen_fishes[fish.name] = fish.weight

        print("We added " + str(round((fish.weight * fish.number), 1)) + " kg of " + fish.name + " (" + str(
            fish.number) + " fishes)")

        # print("We added " + str(round((fish.weight * fish.number), 1)) + " kg of " + fish.name)

    def sell_fish(self, count: int, is_alive: bool, is_fresh: bool, fish: Fish) -> None:
        if count < fish.number:
            if is_fresh and is_alive:
                if len(self.dict_of_fresh_fishes) > 0:
                    self.dict_of_fresh_fishes[fish.name] -= count
                    print("You bought " + str(count) + " kg of " + fish.name)
                    # print(self.dict_of_fresh_fishes)

            elif not is_fresh and not is_alive:
                if len(self.dict_of_fishes) > 0:
                    self.dict_of_fishes[fish.name] -= count
                    print("You bought " + str(count) + " kg of " + fish.name)
                    # print(self.dict_of_fishes)

            elif is_fresh and not is_alive:
                if len(self.dict_of_frozen_fishes) > 0:
                    self.dict_of_frozen_fishes[fish.name] -= count
                    print("You bought " + str(count) + " kg of " + fish.name)
                    # print(self.dict_of_frozen_fishes)

            self.price = fish.price_in_uah_per_kilo * count * fish.weight
            print("The price for " + str(count * fish.weight) + " kg " + fish.name + " is " + str(self.price) + " UAH")

        else:
            print("We don't have " + str(count) + " kg of " + fish.name)

    def sell_fish_boxes(self, count: int, is_alive: bool, is_fresh: bool, fish_box: FishBox) -> None:
        if count < fish_box.number:
            if is_fresh and is_alive:
                if len(self.dict_of_boxes_with_fresh_fish) > 0:
                    self.dict_of_boxes_with_fresh_fish[fish_box.name] -= count
                    print("You bought " + str(count) + " boxes of " + fish_box.name)
                    # print(self.dict_of_fresh_fishes)

            elif not is_fresh and not is_alive:
                if len(self.dict_of_boxes_with_fish) > 0:
                    self.dict_of_boxes_with_fish[fish_box.name] -= count
                    print("You bought " + str(count) + " boxes of " + fish_box.name)
                    # print(self.dict_of_fishes)

            elif is_fresh and not is_alive:
                if len(self.dict_of_boxes_with_frozen_fish) > 0:
                    self.dict_of_boxes_with_frozen_fish[fish_box.name] -= count
                    print("You bought " + str(count) + " boxes of " + fish_box.name)
                    # print(self.dict_of_frozen_fishes)
            self.price = fish_box.fish_info.price_in_uah_per_kilo * count * fish_box.weight
            print(
                "The price for " + str(count) + " boxes " + fish_box.fish_info.name + " is " + str(self.price) + " UAH")
        else:
            print("We don't have " + str(count) + " boxes of " + fish_box.fish_info.name)

    def get_fish_sorted_by_price(self) -> None:
        # self.sort(key=lambda fish: fish.price_in_uah_per_kilo, reverse=True)
        self.dict_of_fishes = sorted(self.dict_of_fishes.items(), key=lambda x: x[1])
        print("Sorted normal age fishes: " + str(self.dict_of_fishes))

    def get_fresh_fish_sorted_by_price(self):
        self.dict_of_fresh_fishes = sorted(self.dict_of_fresh_fishes.items(), key=lambda x: x[1])
        print("Sorted fresh fishes: " + str(self.dict_of_fresh_fishes))

    def get_frozen_fish_sorted_by_price(self):
        self.dict_of_frozen_fishes = sorted(self.dict_of_frozen_fishes.items(), key=lambda x: x[1])
        print("Sorted frozen fishes: " + str(self.dict_of_frozen_fishes))


fish1 = Fish("Forel", 45, "Ukraine", datetime.datetime(2022, 1, 20), datetime.datetime(2022, 2, 25), 1.5, 6)
fish2 = Fish("Okun", 20, "Ukraine", datetime.datetime(2022, 1, 9), datetime.datetime(2022, 1, 10), 0.9, 9)
fish3 = Fish("Karp", 70, "Ukraine", datetime.datetime(2022, 1, 20), datetime.datetime(2022, 2, 25), 2.3, 3)
fish4 = Fish("Oseled", 36, "USA", datetime.datetime(2022, 1, 10), datetime.datetime(2022, 6, 20), 3.1, 5)

fish_info1 = FishInfo("Forel", 45, "Ukraine", datetime.datetime(2022, 1, 20), datetime.datetime(2022, 2, 25))
fish_info2 = FishInfo("Meduza", 400, "Australia", datetime.datetime(2018, 1, 20), datetime.datetime(2022, 5, 27))
fish_box1 = FishBox(fish_info1, 50, datetime.datetime(2021, 2, 25), 40, 40, 40, 3)
fish_box2 = FishBox(fish_info2, 100, datetime.datetime(2018, 1, 20), 40, 40, 40, 9)

fish_shop = FishShop()
fish_shop.add_fish(fish1)
fish_shop.add_fish(fish2)
fish_shop.add_fish(fish3)
fish_shop.add_fish(fish4)
fish_shop.add_fish(fish_box1, 4)
fish_shop.add_fish(fish_box2, 2)
fish_shop.sell_fish(3, True, True, fish2)
fish_shop.sell_fish_boxes(2, False, False, fish_box1)
fish_shop.get_fish_sorted_by_price()
fish_shop.get_fresh_fish_sorted_by_price()
fish_shop.get_frozen_fish_sorted_by_price()

