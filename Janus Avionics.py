#Reading CSV FILE
import csv
f=open("Raw_data.csv",'r')
time=[]
pressure=[]
r=csv.reader(f)
c=-1
for i in r:
    for o in i:
        try:
            x=float(o)
            pressure.append(x)
            c+=1
            time.append(c)
        except ValueError:
            pass
f.close()

#Calculating Altitude and storing data
altitude=[]
PO=pressure[0]
for j in pressure:
    P=j
    T0 = 288.15      
    L = 0.0065       
    R = 8.314       
    M = 0.0289644    
    g = 9.80665
    exponent = (R * L) / (M * g)
    h = (T0 / L) * (1 - (P / PO) ** exponent)
    altitude.append(h)


#Calculating Velocity and storing data
velocity=[]
for k in range(len(altitude)):
    try:
        v=altitude[k+1]-altitude[k]
        velocity.append(v)
    except IndexError:
        velocity.append(k)
        pass

#Smoothing Graph
time.pop()
time.pop()
alt=[]
vel=[]
for a in range(len(altitude)):
    try:
        l=(altitude[a]+altitude[a+1]+altitude[a+2])/3
        alt.append(l)
    except:
        pass
for b in range(len(velocity)):
    try:
        u=(velocity[b]+velocity[b+1]+velocity[b+2])/3
        vel.append(u)
    except:
        pass

#Plotting values on graph
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use("seaborn-v0_8-darkgrid") 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13,7))

# initialize empty plots
line1, = ax1.plot([], [], 'o-', color="royalblue", lw=2, markersize=4, label="Altitude")
line2, = ax2.plot([], [], 'o-', color="crimson", lw=2, markersize=4, label="Velocity")

# Altitude subplot
ax1.set_xlim(0, max(time))
ax1.set_ylim(min(alt)-10, max(alt)+10)
ax1.set_xlabel("Time (s)", fontsize=12)
ax1.set_ylabel("Altitude (m)(reference from starting positon)", fontsize=12)
ax1.set_title("Altitude vs Time", fontsize=14, fontweight="bold")
ax1.legend()

# Velocity subplot
ax2.set_xlim(0, max(time))
ax2.set_ylim(min(vel)-1, max(vel)+1)
ax2.set_xlabel("Time (s)", fontsize=12)
ax2.set_ylabel("Velocity (m/s)", fontsize=12)
ax2.set_title("Velocity vs Time", fontsize=14, fontweight="bold")
ax2.legend()

# Initialization
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Update each frame
def update(frame):
    line1.set_data(time[:frame], alt[:frame])
    line2.set_data(time[:frame], vel[:frame])
    return line1, line2

ani = FuncAnimation(fig, update, frames=len(time), init_func=init,
                    blit=True, interval=25, repeat=False)
ani.save("altitude_velocity.gif",writer="pillow",fps=80)
plt.tight_layout()
plt.show()







    
