import json
from tabulate import tabulate #Imported so the print statement would show a readable table

def main():
    with open("data.json", "r") as input_file: #imports the json file
        s = input_file.read(2048) #convert to string
        s = s.replace("\'", "\"") #change single quotes to double quotes (It was throwing errors with single quotes)
                                  #found this line on stack overflow at:
                                  # https://stackoverflow.com/questions/39491420/python-jsonexpecting-property-name-enclosed-in-double-quotes
        j = json.loads(s) #converts to a python dictionary
        table = [] # This will be the 2D array
        teams = ['Tm'] # This array will be used for the top and bottom rows to match the example table
        table.append(teams)
        row = 0 # initializes row variable used during table creation
        for key in j: # this will iterate through the team arrays using the 3 letter codes as 'key'
            row += 1
            col = 1 # initializes column variable
            teams.append(key) # adds all the 3 letter codes to 'teams'
            newrow = [] # makes a new array that will be added as new row
            newrow.append(key) # each row begins with a teams 3 letter code

            if row == 1: # adds the dashes for the first teams wins against themselves
                newrow.append('--')
            # end if
            for subkey in j.get(key):
                record = j.get(key).get(subkey).get('W') # grabs the number of wins 'key' has against 'subkey'
                newrow.append(record) # adds the value to the current row
                col += 1
                if row == col:
                    newrow.append('--') # adds the dashes for teams 2 through n wins against themselves (keeps table aligned)
                    col += 1
                # end if
            # end for
            table.append(newrow) # adds the row we just put the wins into to the table
        # end for
        table.append(teams) # adds bottom row
        row += 1
        print(tabulate(table)) # prints table for viewing/debugging

main()