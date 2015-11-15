from temboo.Library.Wordnik.Word import GetEtymology
from temboo.core.session import TembooSession

# Create a session with your Temboo account details
session = TembooSession("accountName", "myFirstApp", "abc123xxxxxxxxxxxxxx")

# Instantiate the Choreo
getEtymologyChoreo = GetEtymology(session)

# Get an InputSet object for the Choreo
getEtymologyInputs = getEtymologyChoreo.new_input_set()

# Execute the Choreo
getEtymologyResults = getEtymologyChoreo.execute_with_results(getEtymologyInputs)

# Print the Choreo outputs
print("Response: " + getEtymologyResults.get_Response())
