# Organisation Alpha

Alpha is a _fictional_ medical research organisation attempting to track the spread of diseases around the UK. They work with an international network of partner organisations to attempt to predict (and prevent) future pandemics. Alpha was set-up in a huge rush by the merger of several legacy organisations during the 2020 pandemic and their systems are a bit of a mess.

They've hired you to perform a security audit of their system. They want to know what they should be worried about; how worried they should be; and (hopefully) what they could do to fix it.

## Users

Alpha's systems have many different users.

### Supporters & Contributors

Members of the public who believe in Alpha's mission and want to help. **Supporters** donate their time and money to the organisation to help it succeed. This includes fund raising activities, promotional events and a host of other activities.

**Contributors** are a primary source of data for Alpha. They provide regular updates on their health and well-being, both by submitting a daily update but also sharing biometric readings from smart devices directly with Alpha.

### Collaborators

**Collaborators** are scientists and partner organisations who share data and insights with Alpha. Alpha provides regular updates to the international community.

## Key Systems

Alpha has lots of different systems, but they've prepared an outline of the most important ones for you to consider. They are Eleos, Athena, Apollo and Cassandra.

### Eleos: Event Organisation System

Used by **Supporters** and **Staff** to arrange events and collect donations. It's a stand-alone web-application that runs on a dedicated webserver. It supports multiple forms of authentication: AD Authentication for staff and Facebook, Twitter or Google for supporters.

Key activities it supports:

- Maintains a list of supporters contact details & volunteer history
- Processes one of donations to the organisation
- Maintains details of all events.

Reports on donations are kept on the server and a finance assistant downloads a report once a week for reconciliation.

### Athena: Knowledge Collection

Used by **Contributors** to provide information to Alpha.

Key activities it supports:

- Hosts the forms contributors use to update Alpha on their host and well-being. These can be accessed from both the web and Alpha's mobile app.
- Synchronises smart device data with third part AIs.
- Every six hours Athena sends all newly collected data to Apollo by compressing all its data and uploading it to Apollo's FTP site. Athena then wipes its own database.

### Apollo: Central Database

The central store of all Alpha data.

Key activities it supports:

- International nomenclature is updated every three months. It's published to a Github repo which is pulled onto the Apollo server manually.
- Servicing information requests from external collaborators are accepted by email through the Secure Email Communication Convention (SECC). Requests through SECC are made in a custom domain language, sent in specially encrypted emails. Apollo decrypts these emails, stores them in its database, processes them, and then generates a new, outgoing email with any results.

### Cassandra: Prediction Engine

Cassandra is Alpha's prediction engine. Once a day it connects to the Apollo database, takes a snapshot and produces a forecast of virus developments for the next 30 days. The forecast is uploaded to a storage bucket for future analysis.
