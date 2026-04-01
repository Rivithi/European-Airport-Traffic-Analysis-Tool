Project overview
One short paragraph saying the tool loads airport CSV data, validates input, analyses departures, saves results to results.txt, and shows a histogram.
Features
Mention:
CSV loading
airport/year validation
flight statistics
weather and delay analysis
histogram visualization
saving results to file
Requirements
State:
Python installed
graphics.py must be in the same folder
CSV files must be in the same folder as the script

How to run
Example:

python w2153584.py
Expected file format
Explain that files are named like:
LHR2025.csv
CDG2021.csv
Input rules
Add:
airport code must be 3 letters
year must be from 2000 to 2025
airline code must be valid
Outputs
Explain the 3 outputs:
terminal summary
saved results.txt
histogram window
Example results
Add a small sample from your actual output, such as Heathrow 2025 or CDG 2021. That makes the README look much stronger.

Project structure
Example:

w2153584.py
graphics.py
results.txt
LHR2025.csv
CDG2021.csv
README.md
Limitations
For example:
only works with expected CSV structure
uses predefined airport and airline codes
histogram uses simple graphics library
Future improvements
Good ideas:
use pandas/matplotlib
support more airports
add more charts
export results to CSV/PDF
build GUI version

The most important additions are:

how to run it
what inputs it expects
what outputs it gives
sample results
future improvements


<img width="1114" height="825" alt="Screenshot 2026-04-01 110133" src="https://github.com/user-attachments/assets/32efdf19-233b-4744-987f-74f67c2693c3" />
