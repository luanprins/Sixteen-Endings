class DimensionStruct():
    inventory = []
    mind = []
    world = []

    def get_inventory(self):
        return self.inventory

    def get_mind(self):
        return self.mind

    def get_world(self):
        return self.world

    def add_item(self, item, dimension):
        if dimension == "inventory":
            self.inventory.append(item)
        elif dimension == "mind":
            self.mind.append(item)
        elif dimension == "world":
            self.world.append(item)

    def remove_item(self, item, dimension):
        if dimension == "inventory":
            self.inventory.remove(item)
        elif dimension == "mind":
            self.mind.remove(item)
        elif dimension == "world":
            self.world.remove(item)