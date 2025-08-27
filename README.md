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
  h = \frac{T_0}{L} \Big( 1 - \Big(\frac{P}{P_0}\Big)^{\frac{RL}{Mg}} \Big)
  \]  
- **Velocity Calculation:**  
  \[
  v = \Delta h / \Delta t
  \]  
- **Noise Filtering:** 3-point moving average for altitude & velocity.  
- **Graph Animation:** Altitude & velocity plotted and saved as `altitude_velocity.gif`.  

### How to Run  
```bash
pip install matplotlib
python analysis.py
