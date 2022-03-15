import turtle as tt
tt.title('sex')
tt.color('black','red')
tt.shape('turtle')

def move(length):
    tt.pu()
    tt.fd(length)
    tt.pd()

move(-200)

for _ in range(4):
    tt.fd(50)
    tt.left(90)
move(150)
colors=['red','green','blue','yellow']

for i in range(len(colors)):
    tt.color('black',colors[i])
    tt.fd(50)
    tt.stamp()
move(50)
for i in range(3):
    tt.left(120)
    tt.fd(30)
    tt.stamp()
tt.exitonclick()