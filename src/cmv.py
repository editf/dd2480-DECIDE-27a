from math import sqrt, acos, pi, dist, hypot

def cmv(parameters, points):
    cmv = [False] * 15
    cmv[0] = lic_0(parameters, points)
    cmv[1] = lic_1(parameters, points)
    cmv[2] = lic_2(parameters, points)
    cmv[3] = lic_3(parameters, points)
    cmv[4] = lic_4(parameters, points)
    cmv[5] = lic_5(parameters, points)
    cmv[6] = lic_6(parameters, points)
    cmv[7] = lic_7(parameters, points)
    cmv[8] = lic_8(parameters, points)
    cmv[9] = lic_9(parameters, points)
    cmv[10] = lic_10(parameters, points)
    cmv[11] = lic_11(parameters, points)
    cmv[12] = lic_12(parameters, points)
    cmv[13] = lic_13(parameters, points)
    cmv[14] = lic_14(parameters, points)
    return cmv

def lic_0(parameters, points):
    for i in range(0, len(points)-1):
        x_distance = abs(points[i][0] - points[i+1][0])
        y_distance = abs(points[i][1] - points[i+1][1])
        distance = abs(sqrt(x_distance**2 + y_distance**2))
        if distance > parameters["length1"]:
            return True
    return False

def lic_1(parameters, points):
    """
    Checks whether any three data points fits inside a circle
    with the radius specified in parameters["radius1"]
    """
    for i in range(len(points) - 2):
        p1 = points[i]
        p2 = points[i+1]
        p3 = points[i+2]

        a = dist(p1, p2)
        b = dist(p1, p3)
        c = dist(p2, p3)

        # Semi-perimeter
        s = (a+b+c)/2

        # Heron's formula
        area = sqrt(__round_to_0(s*(s-a)*(s-b)*(s-c)))
        
        # If the area is zero, then the triangle is degenerate, i.e. a+b=c for a≤b≤c
        if area == 0.0:
            if max(a, b, c) > 2*parameters["radius1"]:
                return True
            else:
                continue
        
        # All other triangles
        circumradius = a*b*c/(4*area)

        if circumradius > parameters["radius1"]:
            return True
    return False

def lic_2(parameters, points):
    for i in range(0, len(points)-2):
        a_x_distance = abs(points[i+1][0] - points[i+2][0])
        a_y_distance = abs(points[i+1][1] - points[i+2][1])
        a = abs(sqrt(a_x_distance**2 + a_y_distance**2))

        b_x_distance = abs(points[i][0] - points[i+1][0])
        b_y_distance = abs(points[i][1] - points[i+1][1])
        b = abs(sqrt(b_x_distance**2 + b_y_distance**2))

        c_x_distance = abs(points[i][0] - points[i+2][0])
        c_y_distance = abs(points[i][1] - points[i+2][1])
        c = abs(sqrt(c_x_distance**2 + c_y_distance**2))

        # Not satisfied if either the first point or
        # the last point (or both) coincides with the vertex
        if a == 0 or b == 0:
            continue
        
        # Use the law of cosines
        angle = acos((a**2 + b**2 - c**2) / (2*a*b))

        if angle < pi - parameters["epsilon"]:
            return True
    return False

def lic_3(parameters, points):
    """
    Checks whether or not there are three consecutive points that form a triangle with area greater than [area1].
    Uses Heron's formula to calculate the area of the triangle created by three consecutive points. 
    """
    if len(points) < 3:
        return False

    area1 = parameters["area1"]

    for i in range(len(points)-2):
        p1 = points[i]
        p2 = points[i+1]
        p3 = points[i+2]
        a = dist(p1, p2)
        b = dist(p1, p3)
        c = dist(p2, p3)
        s = (a+b+c)/2
        area = sqrt(__round_to_0(s*(s-a)*(s-b)*(s-c)))
        if area > area1:
            return True
    return False

def lic_4(parameters, points):
    """
    Checks whether or not there exists a set of [q_pts] consecutive points that lie in more than [quads] quadrants.
    """
    q_pts = parameters["q_pts"]
    quads = parameters["quads"]
    
    if len(points) < q_pts:
        return False

    for i in range(len(points)-q_pts+1):
        consecutive_points = []
        for j in range(q_pts):
            consecutive_points.append(points[i+j])
        
        counts = [0,0,0,0] # q1, q2, q3, q4
        for point in consecutive_points:
            if point[0] > 0 and point[1] > 0:
                counts[0] += 1
            elif point[0] < 0 and point[1] > 0:
                counts[1] += 1
            elif point[0] < 0 and point[1] < 0:
                counts[2] += 1
            elif point[0] > 0 and point[1] < 0:
                counts[3] += 1
            else: # cases where a point is on either of the axes
                if point[0] == 0: # point is on the y axis
                    if point[1] >= 0:
                        counts[0] += 1
                    else:
                        counts[2] += 1
                else: # point is on the x axis
                    if point[0] >= 0:
                        counts[0] += 1
                    else:
                        counts[1] += 1
        different_quads = 0
        for i in counts:
            if i > 0:
                different_quads += 1
        if different_quads > quads:
            return True
    return False

def lic_5(parameters, points):
    """
    Checks whether there exists two consecutive points (x1, y1) (x2, y2) such that x2 - x1 < 0
    """
    for i in range(0, len(points)-1):
        if points[i+1][0] - points[i][0] < 0:
            return True
    return False

def lic_6(parameters, points):
    """
    Checks whether or not there exists at least one set of [n_pts] consecutive data points such that at least one point 
    lies at a distance greater than [dist] to the line joining the first and the last point.
    If the first and last point are the same, then it will check whether or not *all* other points lie at a distance
    greater than [dist] to the first/last point. 
    """
    n_pts = parameters["n_pts"]
    dist_p = parameters["dist"]

    if len(points) < n_pts or len(points) < 3:
        return False

    for i in range(len(points)-n_pts+1):
        consecutive_points = []
        for j in range(n_pts):
            consecutive_points.append(points[i+j])
        p1 = consecutive_points[0]
        p2 = consecutive_points[-1]
        line = dist(p1, p2)
        all_points_greater_than_dist = True # used in case p1 and p2 are the same
        for p in consecutive_points[1:-1]:
            if line == 0:
                dist_to_point = dist(p, p1)
                if dist_to_point < dist_p:
                    all_points_greater_than_dist = False
                    break
            else:
                dist_to_line = abs((p2[0]-p1[0])*(p1[1]-p[1]) - (p1[0]-p[0])*(p2[1]-p1[1]))/line
                if dist_to_line > dist_p:
                    return True
        if line == 0 and all_points_greater_than_dist:
            return True
    return False

def lic_7(parameters, points):
    """
    Checks whether or not there exists two points separated by [k_pts] consecutive points
    that are more than [length1] units apart
    """
    k_pts = parameters["k_pts"]
    length1 = parameters["length1"]

    for i in range(len(points)-k_pts-1):
        if dist(points[i], points[i+k_pts+1]) > length1:
            return True
    return False

def lic_8(parameters, points):
    """
    Checks whether any three points with A_PTS and B_PTS consecutive intervening points cannot all be contained in a circle with radius RADIUS1
    """
    if len(points) < 5:
        return False
    a_pts = parameters["a_pts"]
    b_pts = parameters["b_pts"]
    radius1 = parameters["radius1"]
    for i in range(len(points) - 2 - a_pts - b_pts):
        p1 = points[i]
        p2 = points[i+1+a_pts]
        p3 = points[i+2+a_pts+b_pts]

        a = dist(p1, p2)
        b = dist(p1, p3)
        c = dist(p2, p3)

        # Semi-perimeter
        s = (a+b+c)/2

        # Heron's formula
        area = sqrt(__round_to_0(s*(s-a)*(s-b)*(s-c)))

        # If the area is zero, then the triangle is degenerate, i.e. a+b=c for a≤b≤c
        if area == 0.0:
            if max(a, b, c) > 2*radius1:
                return True
            else:
                continue

        # All other triangles
        circumradius = a*b*c/(4*area)

        if circumradius > radius1:
            return True
    return False

def lic_9(parameters, points):
    """
    Checks whether or not there exists at least one set of three points, separated by [c_pts] and [d_pts] consecutive points,
    that form an angle that is either < pi - epsilon or > pi + epsilon. The middle point is the vertex of the angle and the condition
    is not fulfilled if any of the other points of the angle coincide with the vertex. 
    """
    if len(points) < 5:
        return False
    
    epsilon = parameters["epsilon"]
    c_pts = parameters["c_pts"]
    d_pts = parameters["d_pts"]

    for i in range(len(points) - (c_pts + d_pts + 2)):
        p1 = points[i]
        p2 = points[i+c_pts+1] # vertex
        p3 = points[i+c_pts+d_pts+2]

        a = (p1[0] - p2[0], p1[1] - p2[1])
        b = (p3[0] - p2[0], p3[1] - p2[1])

        len_a = hypot(*a)
        len_b = hypot(*b)

        if len_a == 0 or len_b == 0: # point(s) coincide with vertex
            continue

        tmp = (a[0]*b[0] + a[1]*b[1]) / (len_a*len_b)

        # avoid acos domain errors due to float accuracy
        if abs(tmp - 1) < 1e-5:
            tmp = 1.0
        if abs(tmp + 1) < 1e-5:
            tmp = -1.0

        angle = acos(tmp) # if the points lie on a straight line, the angle will be considered to be 0
        if angle < pi - epsilon: # equivalent to alternative angle > pi + epsilon
            return True
    return False

def lic_10(parameters, points):
    """
    Checks whether or not there exists one set of three points separated by exactly [e_pts]
    and [f_pts] consecutive points that form a triangle with area greater than [area1]
    """
    e_pts = parameters["e_pts"]
    f_pts = parameters["f_pts"]
    area1 = parameters["area1"]

    if len(points) < 5:
        return False
    
    for i in range(len(points)-(e_pts+f_pts+2)):
        p1 = points[i]
        p2 = points[i+e_pts+1]
        p3 = points[i+e_pts+f_pts+2]
        a = dist(p1, p2)
        b = dist(p1, p3)
        c = dist(p2, p3)
        s = (a+b+c)/2
        area = sqrt(__round_to_0(s*(s-a)*(s-b)*(s-c))) # Heron's formula
        if area > area1:
            return True
    return False

def lic_11(parameters, points):
    """
    Checks whether there exists two points (x1, y1) (x2, y2) separated by exactly G_PTS consecutive points such that x2 - x1 < 0
    """
    if len(points) < 3:
        return False
    g_pts = parameters["g_pts"]
    for i in range(0, len(points) - 1 - g_pts):
        if points[i+1+g_pts][0] - points[i][0] < 0:
            return True
    return False

def lic_12(parameters, points):
    """
    Checks whether or not there exists at least one pair of points separated by [k_pts] consecutive points that are a distance 
    greater than [length1] apart AND at least one pair of points separated by [k_pts] consecutive points that are less than [length2]
    apart
    """
    if len(points) < 3:
        return False
    
    length1 = parameters["length1"]
    length2 = parameters["length2"]
    k_pts = parameters["k_pts"]

    length1_true = False
    length2_true = False

    for i in range(len(points)-(k_pts+1)):
        p1 = points[i]
        p2 = points[i+k_pts+1]
        
        if dist(p1, p2) > length1:
            length1_true = True

        if dist(p1, p2) < length2:
            length2_true = True

    return length1_true and length2_true

def lic_13(parameters, points):
    """
    Checks whether both the following conditions are true:
    - any three points with A_PTS and B_PTS consecutive intervening points cannot all be contained in a circle with radius RADIUS1
    - any three points with A_PTS and B_PTS consecutive intervening points cannot all be contained in a circle with radius RADIUS2
    If they are, return true. If they are not, return false.
    """
    if len(points) < 5:
        return False
    a_pts = parameters["a_pts"]
    b_pts = parameters["b_pts"]
    radius1 = parameters["radius1"]
    radius2 = parameters["radius2"]
    def helper(radius):
        """
        Checks whether any three points with A_PTS and B_PTS consecutive intervening points
        cannot all be contained in a circle with the specified radius
        """
        for i in range(len(points) - 2 - a_pts - b_pts):
            p1 = points[i]
            p2 = points[i+1+a_pts]
            p3 = points[i+2+a_pts+b_pts]

            a = dist(p1, p2)
            b = dist(p1, p3)
            c = dist(p2, p3)

            # Semi-perimeter
            s = (a+b+c)/2

            # Heron's formula
            area = sqrt(__round_to_0(s*(s-a)*(s-b)*(s-c)))
            
            # If the area is zero, then the triangle is degenerate, i.e. a+b=c for a≤b≤c
            if area == 0.0:
                if max(a, b, c) > 2*radius:
                    return True
                else:
                    continue
            
            # All other triangles
            circumradius = a*b*c/(4*area)

            if circumradius > radius:
                return True
        return False
    return helper(radius1) and helper(radius2)

def lic_14(parameters, points):
    """
    Checks whether both the following conditions are true:
    - any three points with E_PTS and F_PTS consecutive intervening points cannot all be contained in a triangle with area AREA1
    - any three points with E_PTS and F_PTS consecutive intervening points can be contained in a triangle with area AREA2
    If they are, return true. If they are not, return false.
    """
    if len(points) < 5:
        return False
    e_pts = parameters["e_pts"]
    f_pts = parameters["f_pts"]
    area1 = parameters["area1"]
    area2 = parameters["area2"]
    def helper(max_area):
        """
        Checks whether any three points with E_PTS and F_PTS consecutive intervening points
        cannot all be contained in a triangle with the specified area
        """
        for i in range(len(points) - 2 - e_pts - f_pts):
            p1 = points[i]
            p2 = points[i+1+e_pts]
            p3 = points[i+2+e_pts+f_pts]

            a = dist(p1, p2)
            b = dist(p1, p3)
            c = dist(p2, p3)

            # Semi-perimeter
            s = (a+b+c)/2

            # Heron's formula
            area = sqrt(__round_to_0(s*(s-a)*(s-b)*(s-c)))

            if area > max_area:
                return True
        return False
    return helper(area1) and not helper(area2)

def __round_to_0(x):
    """
    Helper function that makes sure that input to sqrt() is not negative due to floating point errors. Returns 0 if it should be rounded, else returns the same input that was given. 
    """
    if abs(x) < 1e-5:
        return 0.0
    else:
        return x