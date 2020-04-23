import copy

# GENERICS -------------------------------

class Age:
    def __init__(self):
        self._ages = {}
    
    def create_unit(self, key):
        self._ages[key] = 0

    def set_unit(self, key, amt):
        self._ages[key] = amt

    def increment_unit(self, key, amt):
        self._ages[key] += amt 
    
    def get_ages(self):
        return copy.deepcopy(self._ages)

class Part:
    def __init__(self):
        self.age = Age()
        self.meta = {}

    def get_next_event(self):
        pass

    def resolve_event(self):
        pass


class Asset:
    def __init__(self):
        self.parts = []
        self.age = Age()

    # for now, no reliabilty on asset
    def get_next_event(self, schedule):
        events = []
        for p in self.parts:
            events.append(p.get_next_event())
        return events



# TEMPLATE ----------------------------------

class Wheel(Part):
    def __init__(self):
        super().__init__()
        self.meta['last_maint'] = 0
        self.age.create_unit('miles')
    
    def get_next_event(self):
        # placeholder
        return {
            "age": {"miles": self.meta['last_maint'] + 10},
            "tag": "scheduled maintenance"
        }
        

# MODEL ---------------------------------------

bicycle = Asset()
bicycle.age.create_unit('miles')
bicycle.parts.append(Wheel())

print(bicycle.age.get_ages())
print(bicycle.parts[0].age.get_ages())

fleet = [bicycle]

# RUN -----------------------------------------

schedule = [
    {"label": "1", "ages": [
        {"miles": 5}
    ]},
    {"label": "2", "ages": [
        {"miles": 5}
    ]},
    {"label": "3", "ages": [
        {"miles": 5}
    ]},    
    {"label": "4", "ages": [
        {"miles": 5}
    ]},
    {"label": "5", "ages": [
        {"miles": 5}
    ]}
]

print(bicycle.get_next_event(schedule))

# print(bicycle.parts[0].get_next_event())

