import shapefile

w=shapefile.Writer('./soal10',shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("crot","dua")
w.record("uluh","tiga")
w.record("sip","empat")
w.record("itugera","dua")



w.poly([[[-5,6],[-9,6], [-9,9],[-5,9], [-5,6]]])
w.poly([[[-5,-3],[-9,-3], [-9,-6],[-5,-6], [-5,-3]]])
w.poly([[[1,6],[5,6], [5,9],[1,9], [1,6]]])
w.poly([[[2,4],[4,4], [4,1],[2,1], [2,4]]])
w.poly([[[5,-1],[5,-10], [-1,-10],[-1,-1], [5,-1]]])