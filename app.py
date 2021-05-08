# Import the required modules
from flask import Flask, render_template, request
import meilisearch
import MySQLdb
import flask_excel as excel
import json

# Connecting to Meilisearch API as a client with the help of pypi package
client = meilisearch.Client('http://127.0.0.1:7700', 'masterKey')


# Function to generate the meilisearch index by passing the index name
# and query to add all the documents (records that are needed to be
# included in search)
def generate_index(index_name, sql_query):

    # Takes the input index name and creates the new index on meilisearch
    codes_index = client.index(index_name)

    # Connect to the MySQL database
    conn = MySQLdb.connect(db="clinical_codes")

    # Creates a cursor on the connection instance
    cursor = conn.cursor()

    # Executes the passed input query
    cursor.execute(sql_query)

    # columns names are loaded into row_headers
    row_headers = [x[0] for x in cursor.description]

    # Fetches all the results of the query
    rows = cursor.fetchall()

    # Initializes the document_array(list) for storing all the results
    document_array = []

    # For each row, a dictionary document is created and appended to
    # document_array
    for result in rows:
        document_array.append(dict(zip(row_headers, result)))

    # Closing the cursor
    cursor.close()

    # Closing the connection
    conn.close()

    # All the documents are added to the meilisearch index
    codes_index.add_documents(document_array)

    # Returns the meilisearch index
    return codes_index


# Declare the index name for diagnosis
diagnosis_index_name = 'diagnosis_codes'

# Declare the SQL query for diagnosis records
diagnosis_codes_query = 'select * from diagnosis_codes;'

# Call the generate_index function to create the diagnosis index
diagnosis_codes_index = generate_index(diagnosis_index_name,
                                       diagnosis_codes_query)

# Declare the index name for lab results
lab_index_name = 'lab_codes'

# Declare the SQL query for lab records
lab_codes_query = 'select * from lab_codes;'

# Call the generate_index function to create the lab index
lab_codes_index = generate_index(lab_index_name, lab_codes_query)

# Declare the index name for medication results
medication_index_name = 'medication_codes'

# Declare the SQL query for medication records
medication_codes_query = 'select * from medication_codes;'

# Call the generate_index function to create the medication index
medication_codes_index = generate_index(medication_index_name,
                                        medication_codes_query)

# Declare the index name for procedure results
procedure_index_name = 'procedure_codes'

# Declare the SQL query for procedure records
procedure_codes_query = 'select * from procedure_codes;'

# Call the generate_index function to create the procedure index
procedure_codes_index = generate_index(procedure_index_name,
                                       procedure_codes_query)

# Declare the index name for surgery results
surgery_index_name = 'surgery_codes'

# Declare the SQL query for surgery records
surgery_codes_query = 'select * from surgery_codes;'

# Call the generate_index function to create the surgery index
surgery_codes_index = generate_index(surgery_index_name,
                                     surgery_codes_query)

# Declare the index name for loinc results
loinc_index_name = 'loinc_codes'

# Declare the SQL query for loinc records
loinc_codes_query = 'select * from loinc_codes;'

# Call the generate_index function to create the loinc index
loinc_codes_index = generate_index(loinc_index_name,
                                   loinc_codes_query)

# Declare the index name for snomedct results
snomedct_index_name = 'snomedct_codes'

# Declare the SQL query for snomedct records
snomedct_codes_query = 'select * from snomedct_codes;'

# Call the generate_index function to create the snomedct index
snomedct_codes_index = generate_index(snomedct_index_name,
                                      snomedct_codes_query)


# Function performs search on the input index based on the search_string
# and returns the query results, number of hits and time in milliseconds for
# running the query
def search_index(index):
    # Get the value of search_string from the form post
    search_string = request.form.get('search_string')
    # Perform a search on diagnosis index by limiting the results to 200
    search_results = index.search(search_string,
                                  {'limit': 200})
    # Extract all the result documents from the search_results dictionary
    codes = search_results.get('hits')
    # Extract the number of results information from the search_results
    # dictionary
    hits = search_results.get('nbHits')
    # Extract the time in milliseconds for the query run time
    query_time = search_results.get('processingTimeMs')

    return codes, hits, query_time


# Create an instance of flask application
app = Flask(__name__)


# Define the method to render content based on the URL path in
# the route() decorator
@app.route("/", methods=['GET', 'POST'])
def index():
    # Initialize the values for headers, codes, hits and query_time variables
    headers = []
    codes = []
    hits = None
    query_time = None

    # If request method is of type POST, then enter the conditional block
    if request.method == 'POST':
        codes, hits, query_time = search_index(diagnosis_codes_index)

        # If there is atleast one result, enter the conditional block
        if(len(codes) > 0):
            # Get the first result (zero index) keys of the dictionary and
            # assign it to headers
            headers = codes[0].keys()

    # Render the template based on the passed html view and the data elements
    return render_template('index.html', headers=headers, codes=codes,
                           hits=hits, query_time=query_time)


# Define the method to render content based on the URL path in
# the route() decorator
@app.route("/labs", methods=['GET', 'POST'])
def labs():
    # Initialize the values for headers, codes, search_string,
    # hits and query_time variables
    headers = []
    codes = []
    hits = None
    query_time = None

    # If request method is of type POST, then enter the conditional block
    if request.method == 'POST':
        # Call search_index by passing the index name
        codes, hits, query_time = search_index(lab_codes_index)

        # If there is atleast one result, enter the conditional block
        if(len(codes) > 0):
            # Get the first result (zero index) keys of the dictionary and
            # assign it to headers
            headers = codes[0].keys()

    # Render the template based on the passed html view and the data elements
    return render_template('labs.html', headers=headers, codes=codes,
                           hits=hits, query_time=query_time)


# Define the method to render content based on the URL path in
# the route() decorator
@app.route("/procedures", methods=['GET', 'POST'])
def procedures():
    # Initialize the values for headers, codes, search_string,
    # hits and query_time variables
    headers = []
    codes = []
    hits = None
    query_time = None

    # If request method is of type POST, then enter the conditional block
    if request.method == 'POST':
        # Call search_index by passing the index name
        codes, hits, query_time = search_index(procedure_codes_index)

        # If there is atleast one result, enter the conditional block
        if(len(codes) > 0):
            # Get the first result (zero index) keys of the dictionary and
            # assign it to headers
            headers = codes[0].keys()

    # Render the template based on the passed html view and the data elements
    return render_template('procedures.html', headers=headers, codes=codes,
                           hits=hits, query_time=query_time)


# Define the method to render content based on the URL path in
# the route() decorator
@app.route("/medications", methods=['GET', 'POST'])
def medications():
    # Initialize the values for headers, codes, search_string,
    # hits and query_time variables
    headers = []
    codes = []
    hits = None
    query_time = None

    # If request method is of type POST, then enter the conditional block
    if request.method == 'POST':
        # Call search_index by passing the index name
        codes, hits, query_time = search_index(medication_codes_index)

        # If there is atleast one result, enter the conditional block
        if(len(codes) > 0):
            # Get the first result (zero index) keys of the dictionary and
            # assign it to headers
            headers = codes[0].keys()

    # Render the template based on the passed html view and the data elements
    return render_template('medications.html', headers=headers, codes=codes,
                           hits=hits, query_time=query_time)


# Define the method to render content based on the URL path in
# the route() decorator
@app.route("/surgeries", methods=['GET', 'POST'])
def surgeries():
    # Initialize the values for headers, codes, search_string,
    # hits and query_time variables
    headers = []
    codes = []
    hits = None
    query_time = None

    # If request method is of type POST, then enter the conditional block
    if request.method == 'POST':
        # Call search_index by passing the index name
        codes, hits, query_time = search_index(surgery_codes_index)

        # If there is atleast one result, enter the conditional block
        if(len(codes) > 0):
            # Get the first result (zero index) keys of the dictionary and
            # assign it to headers
            headers = codes[0].keys()

    # Render the template based on the passed html view and the data elements
    return render_template('surgeries.html', headers=headers, codes=codes,
                           hits=hits, query_time=query_time)


# Define the method to render content based on the URL path in
# the route() decorator
@app.route("/loinc", methods=['GET', 'POST'])
def loinc():
    # Initialize the values for headers, codes, search_string,
    # hits and query_time variables
    headers = []
    codes = []
    hits = None
    query_time = None

    # If request method is of type POST, then enter the conditional block
    if request.method == 'POST':
        # Call search_index by passing the index name
        codes, hits, query_time = search_index(loinc_codes_index)

        # If there is atleast one result, enter the conditional block
        if(len(codes) > 0):
            # Get the first result (zero index) keys of the dictionary and
            # assign it to headers
            headers = codes[0].keys()

    # Render the template based on the passed html view and the data elements
    return render_template('loinc.html', headers=headers, codes=codes,
                           hits=hits, query_time=query_time)


# Define the method to render content based on the URL path in
# the route() decorator
@app.route("/snomedct", methods=['GET', 'POST'])
def snomedct():
    # Initialize the values for headers, codes, search_string,
    # hits and query_time variables
    headers = []
    codes = []
    hits = None
    query_time = None

    # If request method is of type POST, then enter the conditional block
    if request.method == 'POST':
        # Call search_index by passing the index name
        codes, hits, query_time = search_index(snomedct_codes_index)

        # If there is atleast one result, enter the conditional block
        if(len(codes) > 0):
            # Get the first result (zero index) keys of the dictionary and
            # assign it to headers
            headers = codes[0].keys()

    # Render the template based on the passed html view and the data elements
    return render_template('snomedct.html', headers=headers, codes=codes,
                           hits=hits, query_time=query_time)


# Define the method to render content based on the URL path in
# the route() decorator
@app.route("/export", methods=['POST'])
def export_records():
    # Initialize the values for query_results and results_array
    query_results = None
    results_array = []

    # Get the query_results from previously rendered view
    query_results = request.form.get('query_results')

    # The query_results are obtained in the form of plain string and it should
    # be converted into JSON string and then to a list of python dictionaries
    query_results = query_results.replace("{\'", "{\"")
    query_results = query_results.replace("\':", "\":")
    query_results = query_results.replace(": \'", ": \"")
    query_results = query_results.replace("\',", "\",")
    query_results = query_results.replace(", \'", ", \"")
    query_results = query_results.replace("\'}", "\"}")
    query_results = query_results.replace("None", "\"\"")

    # Parse the JSON string into a list of dictionaries
    results_array = json.loads(query_results)

    # Return the CSV file from resultant list of dictionaries
    return excel.make_response_from_records(results_array, "csv",
                                            file_name="export_data")

# Initialize the flask_excel and run the flask application
if __name__ == "__main__":
    excel.init_excel(app)
    app.run(debug=True)
