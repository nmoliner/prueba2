import math

class Star:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def galaxy(self):
        pass
    
    def distance(self, other_star):
        distance_x = (other_star.x - self.x) ** 2
        distance_y = (other_star.y - self.y) ** 2
        distance_z = (other_star.z - self.z) ** 2
        total_distance = math.sqrt(distance_x + distance_y + distance_z)
        return total_distance


class Galaxy:
    def __init__(self, name):
        self.name = name
        self.stars = []
    
    def add_star(self, star):
        self.stars.append(star)
    
    def star_count(self):
        return len(self.stars)


class MilkyWay(Galaxy):
    def star_count(self):
        return len(self.stars)


class AndromedaGalaxy(Galaxy):
    def star_count(self):
        return len(self.stars)


class TriangleGalaxy(Galaxy):
    def star_count(self):
        return len(self.stars)


class SombreroGalaxy(Galaxy):
    def star_count(self):
        return len(self.stars)


class WhirlpoolGalaxy(Galaxy):
    def star_count(self):
        return len(self.stars)


class SagittariusDwarfGalaxy(Galaxy):
    def star_count(self):
        return len(self.stars)


class TypeOStar(Star):
    def galaxy(self):
        return "Type O Star"


class TypeBStar(Star):
    def galaxy(self):
        return "Type B Star"


class TypeAStar(Star):
    def galaxy(self):
        return "Type A Star"


class TypeFStar(Star):
    def galaxy(self):
        return "Type F Star"


class TypeGStar(Star):
    def galaxy(self):
        return "Type G Star"


class TypeKStar(Star):
    def galaxy(self):
        return "Type K Star"


class TypeMStar(Star):
    def galaxy(self):
        return "Type M Star"


def main():
    # Example usage
    star1 = TypeGStar(1, 2, 3)
    star2 = TypeKStar(4, 5, 6)
    star3 = TypeBStar(-3, -1, 0)

    milky_way = MilkyWay("Milky Way")
    andromeda = AndromedaGalaxy("Andromeda Galaxy")
    triangle = TriangleGalaxy("Triangle Galaxy")

    milky_way.add_star(star1)
    andromeda.add_star(star2)
    triangle.add_star(star3)

    print("Star 1:", star1)
    print("Star 2:", star2)
    print("Star 3:", star3)

    print("Galaxy of Star 1:", star1.galaxy())
    print("Galaxy of Star 2:", star2.galaxy())
    print("Galaxy of Star 3:", star3.galaxy())

    print("Number of stars in Milky Way:", milky_way.star_count())
    print("Number of stars in Andromeda Galaxy:", andromeda.star_count())
    print("Number of stars in Triangle Galaxy:", triangle.star_count())

    distance_12 = star1.distance(star2)
    distance_23 = star2.distance(star3)

    print("Distance between Star 1 and Star 2:", distance_12)
    print("Distance between Star 2 and Star 3:", distance_23)


