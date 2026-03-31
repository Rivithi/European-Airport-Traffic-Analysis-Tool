"""
****************************************************************************
Additional info
 1. I declare that my work contains no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID: w1234567
 4. Date: 25/08/2025
****************************************************************************
"""
import csv
import math
from graphics import *

# Global variables
data_list = []   #store data loaded from CSV

#Airport codes and names 
airports = {
    'LHR': 'London Heathrow',
    'MAD': 'Madrid Adolfo Suárez-Barajas', 
    'CDG': 'Charles De Gaulle International',
    'IST': 'Istanbul Airport International',
    'AMS': 'Amsterdam Schiphol',
    'LIS': 'Lisbon Portela',
    'FRA': 'Frankfurt Main',
    'FCO': 'Rome Fiumicino',
    'MUC': 'Munich International',
    'BCN': 'Barcelona International'
}

#Airline codes and names
airlines = {
    'BA': 'British Airways',
    'AF': 'Air France',
    'AY': 'Finnair',
    'KL': 'KLM',
    'SK': 'Scandinavian Airlines',
    'TP': 'TAP Air Portugal',
    'TK': 'Turkish Airlines',
    'W6': 'Wizz Air',
    'U2': 'easyJet',
    'FR': 'Ryanair',
    'A3': 'Aegean Airlines',
    'SN': 'Brussels Airlines',
    'EK': 'Emirates',
    'QR': 'Qatar Airways',
    'IB': 'Iberia',
    'LH': 'Lufthansa'
}

def load_csv(csv_filename):
    """
    This function loads any csv file by name into the list "data_list"
    Parameters: csv_filename - name of the CSV file to load
    Returns: None (modifies global data_list)
    """
    global data_list
    data_list = []  # Clear the list before loading new data
    
    try:
        with open(csv_filename, 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)  # Skip the header row
            for row in csvreader:
                data_list.append(row)  # Add each row to data_list
        print(f"Successfully loaded {len(data_list)} records from {csv_filename}")
    except FileNotFoundError:
        print(f"Error: File {csv_filename} not found!")
        raise
    except Exception as e:
        print(f"Error loading file: {e}")
        raise

def get_airport_code():
 #Ask user for valid 3-letter airport code
    while True:
        code = input("Please enter the three-letter code for the departure city required:")
        code = code.upper().strip()  # Convert to uppercase and remove spaces
        
        # Check the code has 3 words
        if len(code) != 3:
            print("Wrong code length - please enter a three-letter city code")
            continue
        
        # Check if code exists in the airport
        if code not in airports:
            print("Unavailable city code - please enter a valid city code")
            continue
            
        return code

def get_year():
   #Ask user for valid year (2000–2025)
    while True:
        year_input = input("Please enter the year required in the format YYYY:")
        
        #  convert input to integer
        try:
            year = int(year_input)
        except ValueError:
            print("Wrong data type - please enter a four-digit year value")
            continue
        
        # Check if year is in valid range    
        if year < 2000 or year > 2025:
            print("Out of range - please enter a value from 2000 to 2025")
            continue
            
        return year

def analyze_data():
   
    #Total number of flights
    total_flights = len(data_list)
    
    #Count flights from runway 1
    runway1_flights = 0
    for row in data_list:
        if row[8] == '1':  # Runway number is at index 8
            runway1_flights += 1
    
    #Count flights over 500 miles
    over_500_miles = 0
    for row in data_list:
        try:
            distance = int(row[5])  # Distance is at index 5
            if distance > 500:
                over_500_miles += 1
        except ValueError:
            continue  # Skip if distance is not a valid number
    
    # Count British Airways flights
    ba_flights = 0
    for row in data_list:
        flight_num = row[1]  # Flight number is at index 1
        airline_code = flight_num[:2]  # First two characters are airline code
        if airline_code == 'BA':
            ba_flights += 1
    
    # Count flights departing in rain
    rain_flights = 0
    for row in data_list:
        weather = row[9].lower()  # Weather is at index 9, convert to lowercase
        if 'rain' in weather:
            rain_flights += 1
    
    # Calculate average flights per hour
    average_per_hour = round(total_flights / 12, 2)
    
    # Calculate Air France percentage
    af_flights = 0
    for row in data_list:
        flight_num = row[1]
        airline_code = flight_num[:2]
        if airline_code == 'AF':
            af_flights += 1
    af_percentage = round((af_flights / total_flights) * 100, 2) if total_flights > 0 else 0
    
    #Calculate delayed flights percentage
    delayed_flights = 0
    for row in data_list:
        scheduled_dep = row[2]  # Scheduled departure at index 2
        actual_dep = row[3]     # Actual departure at index 3
        if scheduled_dep != actual_dep:
            delayed_flights += 1
    delayed_percentage = round((delayed_flights / total_flights) * 100, 2) if total_flights > 0 else 0
    
    #Count unique hours with rain
    rain_hours_set = set()
    for row in data_list:
        weather = row[9].lower()
        if 'rain' in weather:
            # Extract hour from scheduled departure time
            time_str = row[2]
            hour = time_str.split(':')[0]
            rain_hours_set.add(hour)
    total_rain_hours = len(rain_hours_set)
    
    # Find most common destination(s)
    destinations = {}
    for row in data_list:
        dest_code = row[4]  # Destination at index 4
        if dest_code in destinations:
            destinations[dest_code] += 1
        else:
            destinations[dest_code] = 1
    
    # Find the maximum count
    if destinations:
        max_count = max(destinations.values())
        # Get all destinations with max count and convert to full names
        most_common_dests = []
        for dest_code, count in destinations.items():
            if count == max_count:
                if dest_code in airports:
                    most_common_dests.append(airports[dest_code])
                else:
                    most_common_dests.append(dest_code)  # Use code if name not found
    else:
        most_common_dests = []
    
    # Return all results 
    return {
        'total_flights': total_flights,
        'runway1_flights': runway1_flights,
        'over_500_miles': over_500_miles,
        'ba_flights': ba_flights,
        'rain_flights': rain_flights,
        'average_per_hour': average_per_hour,
        'af_percentage': af_percentage,
        'delayed_percentage': delayed_percentage,
        'rain_hours': total_rain_hours,
        'most_common_dests': most_common_dests
    }

def display_results(airport_code, year, results):
 #Print results to screen
    airport_name = airports[airport_code]

    print(f"File {airport_code}{year}.csv selected - Planes departing {airport_name} {year}")
    
    
    # Print all outcomes in the required format
    print(f"The total number of flights from this airport was {results['total_flights']}")
    print(f"The total number of flights departing Runway one was {results['runway1_flights']}")
    print(f"The total number of departures of flights over 500 miles was {results['over_500_miles']}")
    print(f"There were {results['ba_flights']} British Airways flights from this airport")
    print(f"There were {results['rain_flights']} flights from this airport departing in rain")
    print(f"There was an average of {results['average_per_hour']} flights per hour from this airport")
    print(f"Air France planes made up {results['af_percentage']}% of all departures")
    print(f"{results['delayed_percentage']}% of all departures were delayed")
    print(f"There were {results['rain_hours']} hours in which rain fell")
    print(f"The most common destinations are {results['most_common_dests']}")

def save_results_to_file(airport_code, year, results):
    """
    Save analysis results to results.txt file (append mode)
    Parameters: airport_code, year, results dictionary
    """
    airport_name = airports[airport_code]
    
    try:
        # Open file in append mode - creates file if it doesn't exist
        with open('results.txt', 'a', encoding='utf-8') as file:
            file.write(f"\n{airport_name} {year}\n")
            file.write(f"Total flights: {results['total_flights']}\n")
            file.write(f"Runway 1 flights: {results['runway1_flights']}\n")
            file.write(f"Flights over 500 miles: {results['over_500_miles']}\n")
            file.write(f"British Airways flights: {results['ba_flights']}\n")
            file.write(f"Flights in rain: {results['rain_flights']}\n")
            file.write(f"Average per hour: {results['average_per_hour']}\n")
            file.write(f"Air France percentage: {results['af_percentage']}%\n")
            file.write(f"Delayed percentage: {results['delayed_percentage']}%\n")
            file.write(f"Rain hours: {results['rain_hours']}\n")
            file.write(f"Most common destinations: {results['most_common_dests']}\n")
            file.write("-" * 50 + "\n")
        print("Results saved to results.txt")
    except Exception as e:
        print(f"Error saving to file: {e}")

def get_airline_code():
    
   #Ask user for valid airline code
    while True:
        code = input("Enter a two-character Airline code to plot a histogram:")
        code = code.upper().strip()
        
        if code not in airlines:
            print("Unavailable Airline code please try again")
            continue
            
        return code

def create_histogram(airport_code, year, airline_code):

    #Draw histogram for chosen airline
    airport_name = airports[airport_code]
    airline_name = airlines[airline_code]
    
    # Count flights by hour
    hourly_counts = {}
    for i in range(12):
        hour_str = str(i).zfill(2)
        hourly_counts[hour_str] = 0
    
    for row in data_list:
        flight_num = row[1]
        flight_airline = flight_num[:2]
        
        if flight_airline == airline_code:
            time_str = row[2]
            hour = time_str.split(':')[0]
            if hour in hourly_counts:
                hourly_counts[hour] += 1
    
    # Create window
    win = GraphWin(f"{airline_name} Histogram", 900, 700)
    win.setCoords(0, 0, 900, 700)
    win.setBackground("white")
    
    # Title
    title_text = f"{airline_name} departures from {airport_name} {year}"
    title = Text(Point(450, 650), title_text)
    title.setSize(16)
    title.draw(win)
    
    # Max count for scaling
    max_count = max(hourly_counts.values()) if any(hourly_counts.values()) else 1
    
    # Draw bars
    bar_width = 60
    bar_spacing = 70
    start_x = 50
    
    for i in range(12):
        hour_str = str(i).zfill(2)
        count = hourly_counts[hour_str]
        
        # Calculate bar height
        bar_height = (count / max_count) * 400 if max_count > 0 else 0
        
        # Bar position
        x1 = start_x + (i * bar_spacing)
        y1 = 150
        x2 = x1 + bar_width
        y2 = y1 + bar_height
        
        # Draw bar
        bar = Rectangle(Point(x1, y1), Point(x2, y2))
        bar.setFill("lightblue")
        bar.setOutline("blue")
        bar.draw(win)
        
        # Hour label
        hour_label = Text(Point(x1 + bar_width/2, 120), f"{hour_str}:00")
        hour_label.draw(win)
        
        # Count on bar
        if count > 0:
            count_label = Text(Point(x1 + bar_width/2, y2 + 15), str(count))
            count_label.draw(win)
    
    # Axis labels
    x_label = Text(Point(450, 80), "Hour of Day")
    x_label.draw(win)
    
    y_label = Text(Point(25, 350), "Flights")
    y_label.draw(win)
    
    # Wait for click
    win.getMouse()
    win.close()

def ask_continue():
    #Ask user if they want to continue
    while True:
        answer = input("Do you want to select a new data file? Y/N:")
        answer = answer.upper().strip()
        
        if answer == 'Y':
            return True
        elif answer == 'N':
            return False
        else:
            continue

def main():
   
    # Main program loop - continues until user chooses to quit
    while True:
        try:
            # Task A - Get user input and validate
            airport_code = get_airport_code()
            year = get_year()
            
            # Create filename and load data
            selected_data_file = f"{airport_code}{year}.csv"
            load_csv(selected_data_file)
            
            # Task B - Analyze data and display results
            results = analyze_data()
            display_results(airport_code, year, results)
            
            # Task C - Save results to file
            save_results_to_file(airport_code, year, results)
            
            # Task D - Create histogram
            airline_code = get_airline_code()
            create_histogram(airport_code, year, airline_code)
            
            # Task E - Ask if user wants to continue
            if not ask_continue():
                print("Thank you. End of run")
                break
                
        except FileNotFoundError:
            print(f"Error: Could not find file {selected_data_file}")
            print("Please make sure the CSV file exists in the same directory as this program.")
            if not ask_continue():
                print("Thank you. End of run")
                break
        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            print("Thank you. End of run")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            if not ask_continue():
                print("Thank you. End of run")
                break

# Run the main program
if __name__ == "__main__":
    main()
