# to do look at how could do composition using address - has a relationship with x
# class created with the attributes of an address
# overriding the __str__ method to print the address
class Address:
    def __init__(self, street, city, county, postcode):
        self.street = street
        self.city = city
        self.county = county
        self.postcode = postcode

    def __str__(self):
        return f"Correspondence to be sent to: \n{self.street}, \n{self.city}, \n{self.county}, \n{self.postcode}"