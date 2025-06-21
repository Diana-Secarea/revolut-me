

@app.route('/run')
def run_code():
    # Your code goes here
    print("Someone clicked the link!")
    
    # Example: Save to a file
    with open("log.txt", "a") as f:
        f.write("Script was triggered!\n")

    return "✅ Your code ran successfully!"
