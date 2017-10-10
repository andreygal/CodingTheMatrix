def center_pts(comp_set):
    pts = list(comp_set)
    print(pts)
    #find the center
    maxX, maxY, minX, minY = pts[0].real, pts[0].imag, pts[0].real, pts[0].imag
    for i in pts:
        if i.real > maxX:
            maxX = i.real
        if i.imag > maxY:
            maxY = i.imag
        if i.real < minX:
            minX = i.real
        if i.imag < minY:
            minY = i.imag
    center = complex(minX+(maxX-minX)/2, minY+((maxY - minY)/2))
    print(center, maxX, maxY, minX, minY)
    cent_set = set()
    #transalte the points
    while comp_set:
        trans_pt = comp_set.pop()
        new_pt = trans_pt - center
        cent_set.add(new_pt)
    print(cent_set)
    return cent_set


