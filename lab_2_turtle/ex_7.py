import turtle

turtle.shape('turtle')

k=1
fi_rad=0.2
fi_degr=fi_rad*(180/3.14)

for i in range (0,1000):
    ro=k*fi_rad
    turtle.forward(ro)
    turtle.left(fi_degr)
    fi_rad+=0.1
    ro+=ro
    
