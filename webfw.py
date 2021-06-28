from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/")
def index():
    change = request.args.get("change", "")
    hostname = request.args.get("hostname", "")
    button = request.args.get("button","")
    print("You pressed the button")
    print (hostname + change)
    if change:
        fahrenheit = fahrenheit_from(change)
    else:
        fahrenheit = ""
    return (
        """
        <form action="" method="get">
                Change Req: <input type="text" name="change">
                Hostname: <input type="text" name="hostname">
                <input type="submit" value="SetHostname">
                <button name="button">Press me</button>
            </form>
            
        + "Fahrenheit: "
        + fahrenheit
        
        """
    ) 
    
def fahrenheit_from(change):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(change) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)
    #print (device)