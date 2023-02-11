# Domain-check

By using a regular expression to search for a specific string in the HTML content of the domain,
which indicates the use of WordPress as the CMS and includes the version number. If the string is present,
the script extracts the version number using the group method of the match object and outputs "Yes, running WordPress version X.X.X". 
If the string is not present, the script outputs "No".


