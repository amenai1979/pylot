# determine if a point is inside a given polygon or not
# Polygon is a list of (x,y) pairs.
# adapted from the following page (thank you) : http://www.ariel.com.au/a/python-point-int-poly.html
class Polygon:
    def __init__(self, *points):
        """
        delfines a polygon object as a set of float points. There is no intention to define coplex polygons here but feel free to contribute
        :type self: object
        :type points a list of (x,y) tuples defining points in a 2 dimensional plane
        """
        self.points= points

        
    def point_inside_polygon(self,x,y):
        """
        :param x: x coordinate of the point
        :param y: y coordinate of the point
        :param poly: a list of (x,y) pairs (tuples) that delimit the polygon
        :return: True if the point is in the polygon, False otherwise
        """
        n = len(self.points)
        inside = False
        p1x,p1y = self.points[0]
        for i in range(n+1):
            p2x,p2y = self.points[i % n]
            if y > min(p1y,p2y):
                if y <= max(p1y,p2y):
                    if x <= max(p1x,p2x):
                        if p1y != p2y:
                            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x,p1y = p2x,p2y
        return inside
