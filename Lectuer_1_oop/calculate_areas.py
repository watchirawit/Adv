class Calculate_area:
    def rectangle_area(self,w,h):
        return w*h
    @classmethod
    def triang_area(cls,b,h):
        return 0.5 * b * h
    @staticmethod
    def circle_area(r):
        return 3.14 * r * r

cal = Calculate_area()

cal_rec = cal.rectangle_area(4,5)
cal_tri = cal.triang_area(4,5)
cal_circle = cal.circle_area(5)

print('Rectangle Area =',cal_rec)
print('Triang Area =',cal_tri)
print('Circle Area =',cal_circle)

#print('Test Triang Area',Calculate_area.triang_area(5,6))
#print('Test Circle Area',Calculate_area.circle_area(5))
#print('Test Rectangle Area',Calculate_area.rectangle_area(5,6))