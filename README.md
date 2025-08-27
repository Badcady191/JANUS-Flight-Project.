# JANUS-Flight-Project.
# 🚀 JANUS Flight Analysis & Simulation  

## 📖 Overview  
This project simulates and visualizes the flight of a model rocket using two main components:  

1. **Task 1 – Data Analysis & Visualization (Python)**  
   - Reads raw pressure data from a CSV file.  
   - Calculates altitude using the **barometric formula**.  
   - Derives velocity from altitude changes.  
   - Applies smoothing with a moving average filter.  
   - Animates and saves graphs of **Altitude vs Time** and **Velocity vs Time**.  

2. **Task 2 – Hardware Simulation (Arduino in Tinkercad)**  
   - Simulates rocket flight states: **Ascending, Apogee, Descending**.  
   - Filters noisy sensor data with a moving average.  
   - Uses LEDs and a buzzer as indicators:  
     - 🟢 Green LED → Ascending  
     - 🟡 Yellow LED → Apogee  
     - 🔴 Red LED → Descending  
   - Buzzer gives a short beep at apogee.  

---

## 🗂 Project Structure  

---

## ⚙️ Task 1 – Python (Data Analysis & Visualization)  

### Features  
- **Input:** Raw pressure values from `Raw_data.csv`.  
- **Altitude Calculation (Barometric Formula):**  
  \[
  T0 = 288.15      
    L = 0.0065       
    R = 8.314       
    M = 0.0289644    
    g = 9.80665
    exponent = (R * L) / (M * g)
    h = (T0 / L) * (1 - (P / PO) ** exponent)
  \]  
- **Velocity Calculation:**  
  \[
  v = \Delta h / \Delta t(=1)
  \]  
- **Noise Filtering:** 3-point moving average for altitude & velocity.  
- **Graph Animation:** Altitude & velocity plotted and saved as `altitude_velocity.gif`.  

### How to Run  
```bash
pip install matplotlib
python analysis.py

# 1. Create project folder and go inside
mkdir JANUS-Flight-Project
cd JANUS-Flight-Project

# 2. Create empty files
echo "# JANUS Flight Project" > README.md
echo "print('Python Analysis Placeholder')" > analysis.py
echo "// Arduino Simulation Placeholder" > simulation.ino
echo "time,pressure" > Raw_data.csv
echo "" > altitude_velocity.gif   # placeholder gif

# 3. Create screenshots folder
mkdir screenshots
echo "Tinkercad screenshots go here" > screenshots/README.md

# 4. Initialize Git
git init
git add .
git commit -m "Initial project structure"

# 5. Connect to GitHub (replace with your repo link!)
git remote add origin https://github.com/YOUR-USERNAME/JANUS-Flight-Project.git
git branch -M main
git push -u origin main


