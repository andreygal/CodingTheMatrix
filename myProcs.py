def center_pts(comp_set):
    pts = list(comp_set)
    print(pts)
    center = pts[0]
    for i in (1, len(pts) - 1):
        pt1 = center
        pt2 = pts[i]
        center = (pt1 - pt2) / 2
        cent_set = set()
        print(center)
    while comp_set:
        trans_pt = comp_set.pop()
        new_pt = trans_pt - center
        cent_set.add(new_pt)
    print(cent_set)
    return cent_set


