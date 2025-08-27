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

