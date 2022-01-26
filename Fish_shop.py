import datetime


class Fish:
    def __init__(self, name: str, price_in_uah_per_kilo: float, datetime, origin: str, weight: float) -> None:
        self.name = name
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_data = datetime
        self.origin = origin
        # self.body_only = True
        self.weight = weight


class FishShop:
    list_of_fishes = []

    def add_fish(self, fish: Fish) -> None:
        self.list_of_fishes.append(fish)

    def get_fish_names_sorted_by_price(self) -> None:
        self.list_of_fishes.sort(key=lambda fish: fish.price_in_uah_per_kilo, reverse=True)

    def print_sorted_list_with_fishes(self) -> None:
        self.get_fish_names_sorted_by_price()
        self.cast_out_old_fish()
        print("\nOur list of available and fresh fishes, which you can buy: ")

        for some_fish in self.list_of_fishes:
            print(str(self.list_of_fishes.index(some_fish) + 1) + ")" + some_fish.name + " " + str(
                some_fish.price_in_uah_per_kilo) + " kg ")

    def sell_fish(self, fish: Fish, weight: float) -> None:
        self.price = fish.price_in_uah_per_kilo * weight
        print("The price for " + str(weight) + " kg " + fish.name + " is " + str(self.price) + " UAH")

    def cast_out_old_fish(self) -> None:
        self.present_time = datetime.datetime(2022, 1, 25)
        self.get_fish_names_sorted_by_price()
        for some_fish in self.list_of_fishes:
            self.time_of_serving_fish = self.present_time - some_fish.catch_data

            if self.time_of_serving_fish.days > 30:
                print(str(some_fish.weight) + " kg " + some_fish.name + " was obsolete, so it was thrown away")
                self.list_of_fishes.remove(some_fish)


class Seller:
    def calculate_all_prise_of_purchase(self, fish: Fish):
        pass

    def remove_solded_fish_from_list(self):
        pass


class Buyer:
    def view_list_of_fishes(self, fishshop: FishShop):
        fishshop.print_sorted_list_with_fishes()

    def choose_fish_and_its_weight(self, fishshop: FishShop):
        if len(fishshop.list_of_fishes) > 0:
            if len(fishshop.list_of_fishes) == 1:
                print("Do you want to buy this fish( 1 - yes, 2 - no )")
                self.desire_to_buy_a_single_fish = int(input("Do you want to buy this fish( 1 - yes, 2 - no )"))
                if self.desire_to_buy_a_single_fish == 1:
                    self.weight_of_fish_want_to_buy = float(input("How many kg? "))
                    if self.weight_of_fish_want_to_buy > fishshop.list_of_fishes[0].weight():
                        print("Sorry we don't have so many fish")
                    else:
                        fishshop.sell_fish(fishshop.list_of_fishes[0], self.weight_of_fish_want_to_buy)
            else:
                self.selected_fish_number = int(
                    input("Which number of fish you want to buy (1 -" + str(len(fishshop.list_of_fishes)) + ")? "))
                self.weight_of_fish_want_to_buy = float(input("How many kg? "))

                # don't work properly
                if self.weight_of_fish_want_to_buy > fishshop.list_of_fishes[self.selected_fish_number - 1].weight:
                    print("Sorry we don't have so many fish")
                else:
                    fishshop.sell_fish(fishshop.list_of_fishes[self.selected_fish_number - 1],
                                       self.weight_of_fish_want_to_buy)

        else:
            print("Sorry, now we don't have any frash fish")


fish1 = Fish("Forel", 30, datetime.datetime(2018, 8, 13), "Ukraine", 46)
fish2 = Fish("Seliodka", 68, datetime.datetime(2022, 1, 22), "USA", 100)
fish3 = Fish("Okun", 90, datetime.datetime(2021, 8, 20), "Kanada", 36)
fish4 = Fish("Red Fish", 150, datetime.datetime(2022, 1, 20), "Kanada", 200)

shop = FishShop()
shop.add_fish(fish1)
shop.add_fish(fish2)
shop.add_fish(fish3)
shop.add_fish(fish4)
shop.get_fish_names_sorted_by_price()
# shop.cast_out_old_fish()
# shop.sell_fish(fish1, 47.9)
shop.print_sorted_list_with_fishes()

buyer = Buyer()
buyer.choose_fish_and_its_weight(shop)
