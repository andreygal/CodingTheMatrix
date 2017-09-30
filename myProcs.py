def centerPts(compSet):
 pts = [compSet]
 center = pts[0] 
 for i in (1, len(compSet))
  pt1 = center
  pt2 = pts[i]
  center = (pt1 - pt2) / 2
 centSet = set()
 while (compSet)
  transPt = compSet.pop()
  transPt.real = transPt.real - center.real
  transPt.imag = transPt.imag - center.imag
  centSet.add(newPt)
return centSet


