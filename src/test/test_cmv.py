from math import pi
from src.cmv import *

def test_cmv():
    """""
    Tests that the 'cmv' function returns the same vector
    as calling every 'lic' function individually would
    """""
    points = list()
    for i in range(0, 100):
        points.append((i, i))

    parameters = {
        "length1": 0.5,
        "radius1": 10.0,
        "epsilon": pi/2,
        "area1": 10.0,
        "q_pts": 10,
        "quads": 5,
        "dist": 5.0,
        "n_pts": 5,
        "k_pts": 5,
        "a_pts": 5,
        "b_pts": 5,
        "c_pts": 5,
        "d_pts": 5,
        "e_pts": 5,
        "f_pts": 5,
        "g_pts": 5,
        "length2": 10.0,
        "radius2": 5.0,
        "area2": 10.0
    }

    cmv_res = cmv(parameters, points)
    lics = [lic_0, lic_1, lic_2, lic_3, lic_4, lic_5, lic_6, lic_7, lic_8, lic_9, lic_10, lic_11, lic_12, lic_13, lic_14]
    for i in range(15):
        assert cmv_res[i] == lics[i](parameters, points)

def test_lic_0_true():
    """""
    Test that lic_0 returns true when two consecutive points have a distance larger than or equal to length1
    """""
    parameters = {
        "length1": 0.5
    }
    points = [(0.0, 0.0), (0.0, 0.0), (1.0, 1.0)]
    result = lic_0(parameters, points)
    assert(result)

def test_lic_0_false():
    """""
    Test that lic_0 returns false when no consecutive points have a distance larger than or equal to length1
    """""
    parameters = {
        "length1": 5.0
    }
    points = [(0.0, 0.0), (1.0, 1.0), (1.0, 3.0)]
    result = lic_0(parameters, points)
    assert(not result)

def test_lic_1_true():
    """
    Test that lic_1 returns true if any three consecutive points cannot all be contained in a circle with
    the specified radius
    """
    parameters = {
        "radius1": 1.0
    }
    points = [(2.0, 0.0), (0.0, 2.0), (3.0, 0.0)]
    result = lic_1(parameters, points)
    assert(result)

def test_lic_1_false():
    """
    Test that lic_1 returns false if all sequences of three consecutive points can be contained in a circle
    with the specified radius
    """
    parameters = {
        "radius1": 1.0
    }
    points = [(1.0, 2.0), (2.0, 1.0), (1.5, 1.0)]
    result = lic_1(parameters, points)
    assert(not result)

def test_lic_degenerate_triangle_true():
    """
    Test that lic_1 returns true if three consecutive points that form a degenerate triangle
    (i.e. a+b=c for a≤b≤c) cannot all be contained in a circle with the specified radius
    """
    parameters = {
        "radius1": 1.0
    }
    points = [(2.0, 0.0), (0.0, 2.0), (1.0, 0.0)]
    result = lic_1(parameters, points)
    assert(result)

def test_lic_degenerate_triangle_false():
    """
    Test that lic_1 returns false if three consecutive points that form a degenerate triangle and
    all sequences of three consecutive points can be contained in a circle with the specified radius
    """
    parameters = {
        "radius1": 1.0
    }
    points = [(1.0, 0.0), (0.0, 0.0), (-1.0, 0.0)]
    result = lic_1(parameters, points)
    assert(not result)

def test_lic_2_true():
    """
    Test that lic_2 returns true when angle < (PI-EPSILON) (or equivalently outer angle > (PI+EPSILON))
    """
    parameters = {
        "epsilon": pi/2
    }
    points = [(0.0, 0.0), (1.0, 0.0), (0, 1.0)] # pi/4 angle
    result = lic_2(parameters, points)
    assert(result)


def test_lic_2_false():
    """
    Test that lic_2 returns false when angle > (PI-EPSILON) (or equivalently outer angle < (PI+EPSILON))
    """
    parameters = {
        "epsilon": 3*pi/4
    }
    points = [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0)] # pi/2 angle
    result = lic_2(parameters, points)
    assert(not result)

def test_lic_2_coinciding_vertex_1():
    """
    Test that lic_2 returns false when the first point in one sequence
    coincides with the vertex and no other sequence of consecutive points
    satisfies angle < (PI-EPSILON)
    """
    parameters = {
        "epsilon": 3*pi/4
    }
    points = [(0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (1.0, 1.0)]
    result = lic_2(parameters, points)
    assert(not result)

def test_lic_2_coinciding_vertex_2():
    """
    Test that lic_2 returns true when the first point in one sequence
    coincides with the vertex and another sequence of consecutive points
    satisfies angle < (PI-EPSILON)
    """
    parameters = {
        "epsilon": pi/2
    }
    points = [(0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (0, 1.0)]
    result = lic_2(parameters, points)
    assert(result)

def test_lic_2_coinciding_vertex_3():
    """
    Test that lic_2 returns false when the last point in one sequence
    coincides with the vertex and no other sequence of consecutive points
    satisfies angle < (PI-EPSILON)
    """
    parameters = {
        "epsilon": 3*pi/4
    }
    points = [(-1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (1.0, 1.0)]
    result = lic_2(parameters, points)
    assert(not result)

def test_lic_2_coinciding_vertex_4():
    """
    Test that lic_2 returns true when the last point in one sequence
    coincides with the vertex and another sequence of consecutive points
    satisfies angle < (PI-EPSILON)
    """
    parameters = {
        "epsilon": pi/2
    }
    points = [(-1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (0, 1.0)]
    result = lic_2(parameters, points)
    assert(result)

def test_lic_3_true():
    """
    Tests that lic_3 returns true when there are three consecutive points that form a triangle
    with area > [area1]
    """
    parameters = {
        "area1": 0.5
    }
    points = [(0.0, 0.0), (2.0, 0.0), (2.0, 2.0)]
    result = lic_3(parameters, points)
    assert result

def test_lic_3_false_area_too_small():
    """
    Tests that lic_3 returns false when the area of the triangle is smaller than [area1]
    """
    parameters = {
        "area1": 2.0
    }
    points = [(0.0, 0.0), (1.0, 0.0), (0.0, 0.5)]
    result = lic_3(parameters, points)
    assert not result

def test_lic_3_false_too_few_points():
    """
    Tests that lic_3 returns false when there are only two data points
    """
    parameters = {
        "area1": 0.5
    }
    points = [(0.0, 0.0), (2.0, 0.0)]
    result = lic_3(parameters, points)
    assert not result

def test_lic_3_false_not_a_triangle():
    """
    Tests that lic_3 returns false when the points don't form a triangle
    """
    parameters = {
        "area1": 0.5
    }
    points = [(0.0, 0.0), (0.0, 0.0), (5.0, 5.0)]
    result = lic_3(parameters, points)
    assert not result

def test_lic_4_true():
    """
    Tests that lic_4 returns true when there is a set of [q_pts] consecutive points in the middle of the list
    that lie in more than [quads] different quadrants
    """
    parameters = {
        "quads": 1,
        "q_pts": 2
    }
    points = [(1.0, 1.0), (1.0, 1.0), (-1.0, -1.0), (-1.0, -1.0)]
    result = lic_4(parameters, points)
    assert result

def test_lic_4_true_entire_list_all_quads():
    """
    Tests that lic_4 returns true when there is a set of [q_pts] consecutive points that lie in 
    more than [quads] different quadrants
    """
    parameters = {
        "quads": 3,
        "q_pts": 4
    }
    points = [(1.0, 1.0), (-1.0, 1.0), (-1.0, -1.0), (1.0, -1.0)]
    result = lic_4(parameters, points)
    assert result

def test_lic_4_true_points_on_axes():
    """
    Tests that lic_4 returns true for edge cases where points lie on the x and y axes but belong to 
    three different quadrants
    """
    parameters = {
        "quads": 2,
        "q_pts": 4
    }
    points = [(0.0, 0.0), (-1.0, 0.0), (0.0, -1.0), (0.0, 1.0)] # points belong to q1, q2, q3 and q1
    result = lic_4(parameters, points)
    assert result

def test_lic_4_false_too_few_points():
    """
    Tests that lic_4 returns false when there are less than [q_pts] in the list
    """
    parameters = {
        "quads": 3,
        "q_pts": 4
    }
    points = [(1.0, 1.0), (-1.0, 1.0), (-1.0, -1.0)]
    result = lic_4(parameters, points)
    assert not result

def test_lic_4_false_all_same_quadrant():
    """
    Tests that lic_4 returns false when all points lie in the same quadrant
    """
    parameters = {
        "quads": 1,
        "q_pts": 2
    }
    points = [(1.0, 1.0), (0.0, 0.0), (0.0, 1.0)]
    result = lic_4(parameters, points)
    assert not result

def test_lic_4_false_edge_cases():
    """
    Tests that lic_4 returns false for edge cases where points lie on the x and y axes
    """
    parameters = {
        "quads": 3,
        "q_pts": 4
    }
    points = [(0.0, 0.0), (-1.0, 0.0), (0.0, -1.0), (0.0, 1.0)] # points belong to q1, q2, q3 and q1
    result = lic_4(parameters, points)
    assert not result

def test_lic_4_false_not_consecutive():
    """
    Tests that lic_4 returns false when there are not enough consecutive points that lie
    in the correct number of quadrants
    """
    parameters = {
        "quads": 2,
        "q_pts": 2
    }
    points = [(0.0, 0.0), (-1.0, -1.0), (0.0, 0.0), (-1.0, -1.0)]
    result = lic_4(parameters, points)
    assert not result

def test_lic_5_true():
    """
    Tests that lic_5 returns true when two consecutive points (x1, y1) (x2, y2) exist such that x2 - x1 < 0
    """
    parameters = {}
    points = [(1.0, 0.0), (0.0, 0.0)]
    result = lic_5(parameters, points)
    assert(result)

def test_lic_5_false():
    """
    Tests that lic_5 returns false when no consecutive points (x1, y1) (x2, y2) exist such that x2 - x1 < 0
    """
    parameters = {}
    points = [(0.0, 0.0), (1.0, 0.0)]
    result = lic_5(parameters, points)
    assert(not result)

def test_lic_6_true():
    """
    Tests that lic_6 returns true when there is one set of three consecutive points with one point that lies
    at a distance greater than [dist] from the line joining the other two
    """
    parameters = {
        "n_pts": 3,
        "dist": 1
    }
    points = [(-2.0, -2.0), (-1.0, 0.0), (0.0, 5.0), (1.0, 0.0)]
    result = lic_6(parameters, points)
    assert result

def test_lic_6_true_coinciding_point():
    """
    Tests that lic_6 returns true when the first and last points coincide and each other consecutive point
    lies at a distance greater than [dist] to the coinciding point
    """
    parameters = {
        "n_pts": 4,
        "dist": 1
    }
    points = [(0.0, 0.0), (-2.0, 1.0), (1.0, 5.0), (0.0, 0.0)]
    result = lic_6(parameters, points)
    assert result

def test_lic_6_false():
    """
    Tests that lic_6 returns false when there is no point that lies at a distance greater than [dist]
    to the line joining the first and last points
    """
    parameters = {
        "n_pts": 4,
        "dist": 5
    }
    points = [(-2.0, 0.0), (-1.0, 1.0), (0.0, 3.0), (2.0, 0.0)]
    result = lic_6(parameters, points)
    assert not result

def test_lic_6_false_too_few_points():
    """
    Tests that lic_6 returns false when there are less than three points
    """
    parameters = {
        "n_pts": 4,
        "dist": 5
    }
    points = [(-2.0, 0.0), (-1.0, 1.0)]
    result = lic_6(parameters, points)
    assert not result

def test_lic_6_false_coinciding_point():
    """
    Tests that lic_6 returns false when the first and last points coincide and not all points lie at a 
    distance greater than [dist] to the coinciding point
    """
    parameters = {
        "n_pts": 4,
        "dist": 5
    }
    points = [(0.0, 0.0), (-1.0, 1.0), (15.0, 15.0), (0.0, 0.0)]
    result = lic_6(parameters, points)
    assert not result

def test_lic_7_true():
    """
    Tests that lic_7 returns true when there are two points separated by [k_pts] consecutive points
    that lie at a distance greater than [length1] units apart
    """
    parameters = {
        "length1": 1,
        "k_pts": 1
    }
    points = [(0.0, 0.0), (-1.0, -1.0), (2.0, 0.0)]
    result = lic_7(parameters, points)
    assert result

def test_lic_7_false():
    """
    Tests that lic_7 returns false when there are no two points separated by [k_pts] consecutive points
    that lie at a distance greater than [length1] units apart
    """
    parameters = {
        "length1": 1,
        "k_pts": 2
    }
    points = [(0.0, 0.0), (-1.0, -1.0), (2.0, 0.0)]
    result = lic_7(parameters, points)
    assert not result

def test_lic_7_false_distance_too_small():
    """
    Tests that lic_7 returns false when the points lie at a distance smaller than [length1]
    """
    parameters = {
        "length1": 10,
        "k_pts": 1
    }
    points = [(0.0, 0.0), (-1.0, -1.0), (2.0, 0.0)]
    result = lic_7(parameters, points)
    assert not result

def test_lic_7_too_few_points():
    """
    Tests that lic_7 returns false when there are less than 3 points
    """
    parameters = {
        "length1": 1,
        "k_pts": 1
    }
    points = [(0.0, 0.0), (-1.0, -1.0)]
    result = lic_7(parameters, points)
    assert not result
    
def test_lic_8_true():
    """
    Tests that lic_8 returns true when three points with A_PTS and B_PTS consecutive intervening points
    cannot all be contained in a circle with radius RADIUS1
    """
    parameters = {
        "radius1": 1.0,
        "a_pts": 1,
        "b_pts": 1
    }
    points = [(0.0, 0.0), (-1.0, -2.0), (5.0, 0.0), (1.0, 2.0), (0.0, 5.0)]
    result = lic_8(parameters, points)
    assert(result)

def test_lic_8_false():
    """
    Tests that lic_8 returns false when three points with A_PTS and B_PTS consecutive intervening points
    can all be contained in a circle with radius RADIUS1
    """
    parameters = {
        "radius1": 10.0,
        "a_pts": 2,
        "b_pts": 1
    }
    points = [(1.0, 1.0), (-1.0, -2.0), (0.0, 0.0), (3.0, 1.0), (1.0, 2.0), (3.0, 1.0)]
    result = lic_8(parameters, points)
    assert(not result)

def test_lic_8_degenerate_triangle_true():
    """
    Tests that lic_8 returns true if three points with A_PTS and B_PTS consecutive intervening points that
    form a degenerate triangle (i.e. a+b=c for a≤b≤c) cannot all be contained in a circle with radius RADIUS1
    """
    parameters = {
        "radius1": 2.9,
        "a_pts": 1,
        "b_pts": 2
    }
    points = [(0.0, 0.0), (-2.0, -7.0), (3.0, 0.0), (0.0, 3.0), (1.0, 4.0), (-3.0, 0.0)]
    result = lic_8(parameters, points)
    assert(result)

def test_lic_8_degenerate_triangle_false():
    """
    Tests that lic_8 returns false if three points with A_PTS and B_PTS consecutive intervening points that
    form a degenerate triangle (i.e. a+b=c for a≤b≤c) can be contained in a circle with radius RADIUS1
    """
    parameters = {
        "radius1": 3.0,
        "a_pts": 1,
        "b_pts": 2
    }
    points = [(0.0, 0.0), (-2.0, -7.0), (3.0, 0.0), (0.0, 3.0), (1.0, 4.0), (-3.0, 0.0)]
    result = lic_8(parameters, points)
    assert(not result)

def test_lic_8_too_few_points():
    """
    Tests that lic_8 returns false when there are less than 5 points
    """
    parameters = {
        "radius1": 0.0,
        "a_pts": 0,
        "b_pts": 1
    }
    points = [(0.0, 0.0), (-1.0, -2.0), (3.0, 0.0), (1.0, 2.0)]
    result = lic_8(parameters, points)
    assert(not result)

def test_lic_9_true():
    """
    Tests that lic_9 returns true when there is a set of three points separated by [c_pts] and [d_pts] consecutive points
    that form an angle that is smaller than pi - [epsilon]
    """
    parameters = {
        "c_pts": 1,
        "d_pts": 1,
        "epsilon": pi/4
    }
    points = [(0.0, 1.0), (-1.0, -1.0), (0.0, 0.0), (-1.0, -1.0), (1.0, 0.0)] # pi/2 angle
    result = lic_9(parameters, points)
    assert result

def test_lic_9_false():
    """
    Tests that lic_9 returns false when there is no set of points that form an angle smaller than pi - [epsilon]
    """
    parameters = {
        "c_pts": 1,
        "d_pts": 1,
        "epsilon": 3*pi/4
    }
    points = [(0.0, 1.0), (-1.0, -1.0), (0.0, 0.0), (-1.0, -1.0), (1.0, 0.0)] # pi/2 angle
    result = lic_9(parameters, points)
    assert not result

def test_lic_9_false_coinciding_point1():
    """
    Tests that lic_9 returns false when the first point coincides with the vertex
    """
    parameters = {
            "c_pts": 2,
            "d_pts": 1,
            "epsilon": pi/2
        }
    points = [(0.0, 0.0), (-1.0, -1.0), (-1.0, -1.0), (0.0, 0.0), (-1.0, -1.0), (2.0, 2.0)]
    result = lic_9(parameters, points)
    assert not result

def test_lic_9_false_coinciding_point2():
    """
    Tests that lic_9 returns false when the second point coincides with the vertex
    """
    parameters = {
            "c_pts": 2,
            "d_pts": 1,
            "epsilon": pi/2
        }
    points = [(0.0, 1.0), (-1.0, -1.0), (-1.0, -1.0), (0.0, 0.0), (-1.0, -1.0), (0.0, 0.0)]
    result = lic_9(parameters, points)
    assert not result

def test_lic_9_false_too_few_points():
    """
    Tests that lic_9 returns false when there are less than 5 points
    """
    parameters = {
            "c_pts": 1,
            "d_pts": 1,
            "epsilon": pi/4
        }
    points = [(0.0, 1.0), (-1.0, -1.0), (0.0, 0.0)] 
    result = lic_9(parameters, points)
    assert not result

def test_lic_10_true():
    """
    Tests that lic_10 returns true when there exists a set of three points separated by [e_pts] and [f_pts]
    consecutive points that form a triangle with area greater than area1
    """
    parameters = {
        "area1": 1,
        "e_pts": 2,
        "f_pts": 1
    }
    points = [(1.0, 1.0), (0.0, 0.0), (1.0, 1.0), (1.0, 1.0), (2.0, 0.0), (1.0, 1.0), (0.0, 2.0)]
    result = lic_10(parameters, points)
    assert result

def test_lic_10_false():
    """
    Tests that lic_10 returns false when there is no set of three points separated by [e_pts] and [f_pts] consecutive points
    that form a triangle with area greater than area1
    """
    parameters = {
        "area1": 10,
        "e_pts": 2,
        "f_pts": 1
    }
    points = [(0.0, 0.0), (1.0, 1.0), (1.0, 1.0), (2.0, 0.0), (1.0, 1.0), (0.0, 2.0)]
    result = lic_10(parameters, points)
    assert not result

def test_lic_10_too_few_points():
    """
    Tests that lic_10 returns false when there are less than 5 points provided
    """
    parameters = {
        "area1": 10,
        "e_pts": 2,
        "f_pts": 1
    }
    points = [(0.0, 0.0), (1.0, 1.0)]
    result = lic_10(parameters, points)
    assert not result

def test_lic_11_true():
    """
    Tests that lic_11 returns true when there exists two points (x1, y1) (x2, y2)
    separated by exactly G_PTS consecutive points such that x2 - x1 < 0
    """
    parameters = {
        "g_pts": 2
    }
    points = [(1.0, 0.0), (5.0, 5.0), (-1.0, 0.0), (0.0, 0.0)]
    result = lic_11(parameters, points)
    assert(result)

def test_lic_11_false():
    """
    Tests that lic_11 returns false when there are no points (x1, y1) (x2, y2)
    separated by exactly G_PTS consecutive points such that x2 - x1 < 0
    """
    parameters = {
        "g_pts": 3
    }
    points = [(0.0, 1.0), (3.0, 5.0), (-1.0, 0.0), (-1.0, 0.0), (6.0, 0.0)]
    result = lic_11(parameters, points)
    assert(not result)

def test_lic_11_too_few_points():
    """
    Tests that lic_11 returns false if there are fewer than 3 points
    """
    parameters = {
        "g_pts": 1
    }
    points = [(0.0, 1.0), (1.0, 2.0)]
    result = lic_11(parameters, points)
    assert(not result)

def test_lic_12_true():
    """
    Tests that lic_12 returns true when there is a pair of points separated by [k_pts] that are more than [length1] units apart,
    and a set of points separated by [k_pts] that are less than [length2] apart
    """
    parameters = {
        "length1": 1,
        "length2": 2,
        "k_pts": 1
    }
    points = [(0.0, 0.0), (-1.0, -1.0), (2.0, 0.0), (0.0, 0.0)]
    result = lic_12(parameters, points)
    assert result

def test_lic_12_true_same_points():
    """
    Tests that lic_12 returns true when the same set of points are at a distance greater than [length1]
    and smaller than [length2] apart
    """
    parameters = {
        "length1": 1,
        "length2": 3,
        "k_pts": 2
    }
    points = [(0.0, 0.0), (-1.0, -1.0), (-1.0, -1.0), (2.0, 0.0)]
    result = lic_12(parameters, points)
    assert result

def test_lic_12_false_length1_not_met():
    """
    Tests that lic_12 returns false when there is a set of points that fulfill the condition on [length2] but not [length1]
    """
    parameters = {
        "length1": 10,
        "length2": 3,
        "k_pts": 1
    }
    points = [(0.0, 0.0), (-1.0, -1.0), (2.0, 0.0), (1.0, 1.0)]
    result = lic_12(parameters, points)
    assert not result

def test_lic_12_false_length2_not_met():
    """
    Tests that lic_12 returns false when there is a set of points that fulfill the condition on [length1] but not [length2]
    """
    parameters = {
        "length1": 0.5,
        "length2": 0.1,
        "k_pts": 1
    }
    points = [(0.0, 0.0), (-1.0, -1.0), (2.0, 0.0), (1.0, 1.0)]
    result = lic_12(parameters, points)
    assert not result

def test_lic_12_false_too_few_points():
    """
    Tests that lic_12 returns false when there are less than 3 points
    """
    parameters = {
        "length1": 1,
        "length2": 3,
        "k_pts": 1
    }
    points = [(0.0, 0.0), (-1.0, -1.0)]
    result = lic_12(parameters, points)
    assert not result

def test_lic_13_true():
    """
    Tests that lic_13 returns true if both the following conditions are true:
    - any three points with A_PTS and B_PTS consecutive intervening points cannot all be contained in a circle with radius RADIUS1
    - any three points with A_PTS and B_PTS consecutive intervening points cannot all be contained in a circle with radius RADIUS2
    """
    parameters = {
        "radius1": 0.5,
        "radius2": 1.0,
        "a_pts": 1,
        "b_pts": 1
    }
    points = [(2.0, 0.0), (0.0, 0.0), (0.0, 2.0), (0.0, 0.0), (3.0, 0.0)]
    result = lic_13(parameters, points)
    assert(result)

def test_lic_13_false_1():
    """
    Tests that lic_13 returns false if any three points with A_PTS and B_PTS intervening points can all be contained
    in a circle with the radius RADIUS1
    """
    parameters = {
        "radius1": 10.0,
        "radius2": 1.0,
        "a_pts": 2,
        "b_pts": 2
    }
    points = [(2.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 2.0), (0.0, 0.0), (0.0, 0.0), (3.0, 0.0)]
    result = lic_13(parameters, points)
    assert(not result)

def test_lic_13_false_2():
    """
    Tests that lic_13 returns false if both:
    - any three points with A_PTS and B_PTS consecutive intervening points can all be contained in a circle with radius RADIUS1
    - any three points with A_PTS and B_PTS consecutive intervening points can all be contained in a circle with radius RADIUS2
    """
    parameters = {
        "radius1": 10.0,
        "radius2": 10.0,
        "a_pts": 3,
        "b_pts": 1
    }
    points = [(2.0, 0.0), (0.0, 0.0), (0.0, 0.0), (25.0, 25.0), (0.0, 2.0), (0.0, 0.0), (3.0, 0.0)]
    result = lic_13(parameters, points)
    assert(not result)

def test_lic_14_true():
    """
    Tests that lic_14 returns true if both the following conditions are true:
    - any three points with E_PTS and F_PTS consecutive intervening points cannot all be contained in a triangle with area AREA1
    - any three points with E_PTS and F_PTS consecutive intervening points can be contained in a triangle with area AREA2
    """
    parameters = {
        "area1": 0.5,
        "area2": 2.0,
        "e_pts": 1,
        "f_pts": 1
    }
    points = [(3.0, 1.0), (0.0, 0.0), (1.0, 3.0), (0.0, 0.0), (1.0, 1.0)]
    result = lic_14(parameters, points)
    assert(result)

def test_lic_14_false_1():
    """
    Tests that lic_14 returns false if three points with E_PTS and F_PTS consecutive intervening points can be contained in a triangle with area AREA1
    """
    parameters = {
        "area1": 2.0,
        "area2": 3,
        "e_pts": 2,
        "f_pts": 2
    }
    points = [(2.0, 1.0), (0.0, 0.0), (1.0, 1.0), (1.0, 2.0), (5.0, 3.0), (0.0, 0.0), (1.0, 1.0)]
    result = lic_14(parameters, points)
    assert(not result)

def test_lic_14_false_2():
    """
    Tests that lic_14 returns false if both the following conditions are true:
    - any three points with E_PTS and F_PTS consecutive intervening points can be contained in a triangle with area AREA1
    - any three points with E_PTS and F_PTS consecutive intervening points cannot be contained in a triangle with area AREA2
    """
    parameters = {
        "area1": 2.0,
        "area2": 0.0,
        "e_pts": 0,
        "f_pts": 2
    }
    points = [(2.0, 1.0), (1.0, 2.0), (5.0, 3.0), (0.0, 0.0), (1.0, 1.0)]
    result = lic_14(parameters, points)
    assert(not result)

def test_lic_14_too_few_points():
    """
    Tests that lic_14 returns false if there are fewer than 5 points
    """
    parameters = {
        "area1": 0.0,
        "area2": 0.0,
        "e_pts": 0,
        "f_pts": 1
    }
    points = [(-3.0, -1.0), (-1.0, -3.0), (0.0, 0.0), (-1.0, -1.0)]
    result = lic_14(parameters, points)
    assert(not result)

def test_lic_14_true_helper_loop():
    """
    Tests that the helper loop for lic_14 is run more than once (i.e. can find solutions that are not at the beginning of the list of points)
    """
    parameters = {
        "area1": 0.5,
        "area2": 2.0,
        "e_pts": 1,
        "f_pts": 1
    }
    points = [(-1.0, -1.0), (3.0, 1.0), (0.0, 0.0), (1.0, 3.0), (0.0, 0.0), (1.0, 1.0)]
    result = lic_14(parameters, points)
    assert(result)

def test_triangle_lics_rounding_area_to_0():
    """
    Tests that LICs using Heron's formula (LICs 1, 3, 8, 10, 13, 14) don't raise domain errors due to float precision errors causing negative square root inputs
    """
    points = []
    num_points = 10
    for i in range(num_points):
        points.append((i, i)) 
    points.extend([(0.0, 0.0), (2.0, 0.0), (0.0, 2.0)]) 
    points.extend([(0.0, 0.0), (-1.0, -1.0), (2.0, 0.0), (-1.0, -1.0), (0.0, 2.0)])
    parameters = {
        "length1": 0.5,      # Length in LICs 0, 7, 12
        "radius1": 0.5,      # Radius in LICs 1, 8, 13
        "epsilon": 0.5,      # Deviation from PI in LIC 2,9
        "area1": 1,        # Area in LICs 3, 10, 14
        "q_pts": 2,          # Nr consecutive points in LIC 4
        "quads": 1,          # Nr quadrants in LIC 4
        "dist": 0,         # Distance in LIC 6
        "n_pts": 3,          # Nr consecutive points in LIC 6
        "k_pts": 1,          # Nr int points in LICS 7, 12
        "a_pts": 1,          # Nr int points in LICS 8, 13
        "b_pts": 1,          # Nr int points in LICS 8, 13
        "c_pts": 1,          # Nr int points in LICS 9
        "d_pts": 1,          # Nr int points in LICS 9
        "e_pts": 1,          # Nr int points in LICS 10, 14
        "f_pts": 1,          # Nr int points in LICS 10, 14
        "g_pts": 1,          # Nr int points in LICS 11
        "length2": 2,      # Nr int points in LICS 12
        "radius2": 3,      # Nr int points in LICS 13
        "area2": 40,        # Nr int points in LICS 14
    }

    try:
        lic_1(parameters, points)
        lic_3(parameters, points)
        lic_8(parameters, points)
        lic_10(parameters, points)
        lic_13(parameters, points)
        lic_14(parameters, points)
        assert True
    except ValueError:
        assert False
