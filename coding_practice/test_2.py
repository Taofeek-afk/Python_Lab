# stmt = "Remember Red Hope is a good thing and no good thing ever dies"

# # dic = {}.fromkeys(stmt.lower().split())

# # | = union, & = intersection

# print(dir(set))
# print("vertical tab in work \v bah-ha")

# print("this line will return this line \
# with whatever is written in the next line")

# print(rf"escape characters are lost here \ well, {"apple bread"} not so true")


a = dict(name="taofeek", nationality="taofeek", age=23)  # noqa: C408

# print(a)

from types import SimpleNamespace

id_1 = SimpleNamespace(name="Taofeek", age=23, nationality="Nigeria")

# print(id_1)
# print(id_1.age)
# print(id_1.nationality)


class AttrDict(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"{self.__class__} object has no attr '{key}'")
    
    def __setattr__(self, key, value):
        # try:
        self[key] = value
        # except AttributeError("")

class AttrDict2(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'AttrDict' object has no attribute '{key}'")

    def __setattr__(self, key, value):
        self[key] = value


# Usage:
a = AttrDict(name="taofeek", nationality="Nigeria", age=23)


class RecursiveAttrDict(dict):
    def __getattr__(self, key):
        try:
            val = self[key]
            # If the retrieved value is a standard dict, convert it on the fly
            if isinstance(val, dict) and not isinstance(val, RecursiveAttrDict):
                val = RecursiveAttrDict(val)
                self[key] = val
            return val
        except KeyError:
            raise AttributeError(f"'RecursiveAttrDict' object has no attribute '{key}'")

    def __setattr__(self, key, value):
        self[key] = value

    def __getitem__(self, key):
        val = super().__getitem__(key)
        # Handle recursive conversion for standard bracket access as well
        if isinstance(val, dict) and not isinstance(val, RecursiveAttrDict):
            val = RecursiveAttrDict(val)
            self[key] = val
        return val


# Example usage:
data = {
    "user": {
        "name": "Taofeek",
        "location": {
            "city": "Lagos",
            "country": "Nigeria"
        }
    }
}

a = RecursiveAttrDict(data)

# Infinite nesting supported:
print(a.user.name)              # Output: Taofeek
print(a.user.location.city)     # Output: Lagos

# Still acts like a dict:
print(a["user"]["location"]["country"])  # Output: Nigeria
