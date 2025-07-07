# Halo-CME-WebApp
Halo CME Detection using SWIS-ASPEX Data (Aditya-L1)
This project is a real-time dashboard web application for detecting Halo Coronal Mass Ejection (CME) events using simulated Level-2 particle data from the SWIS instrument onboard the Aditya-L1 mission.

It includes a Flask-based Python backend that generates CME data, and an interactive frontend dashboard built with Plotly.js to visualize flux × density and highlight CME events.

Objective
To simulate and detect transient solar wind disturbances (Halo CME).

To analyze particle data parameters such as:

Flux

Density

Temperature

Speed

To derive thresholds and detect potential CME events in real-time.

Technologies Used
Python: Flask, NumPy, Pandas

Frontend: HTML, JavaScript, Plotly.js

Hosting: Deployable via Render, Railway, or any Flask-compatible platform

live Dashboard Features
Real-time CME detection API (/api/cme)

Interactive Plot: Flux × Density with red markers for CME flags

Data table: Shows timestamp-wise CME classification

Responsive dark-themed UI with Plotly graphs
