def center_pts(comp_set):
    pts = [comp_set]
    center = pts[0]
    for i in (1, len(comp_set)):
        pt1 = center
        pt2 = pts[i]
        center = (pt1 - pt2) / 2
        cent_set = set()
    while comp_set:
        trans_pt = comp_set.pop()
        trans_pt.real = trans_pt.real - center.real
        trans_pt.imag = trans_pt.imag - center.imag
        cent_set.add(trans_pt)
    return cent_set


