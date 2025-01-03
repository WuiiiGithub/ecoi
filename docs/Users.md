# Users 
Let `userX`, `another_userY` be created users. Where `X`, `Y` are numbers respectively. Here, the operations that could be performed by users are grouped as follows:

```python
# related packages
from ecoi.core import users, groups, terminal
from ecoi.core.economy import *
from ecoi.core.social import *
```

## CURD+ Operations

```python
user = users.createUser(
    id: str,                  # Unique identifier for the user
    name: str,                # Full name of the user
    gmail: str,               # Gmail address for the user
    gender: Literal['Male', 'Female', 'Other'],  # Gender identity of the user
    birthday: datetime,       # Birthdate of the user (in datetime format)
    location: str,            # Geographical location (city, country)
    group_id: str,            # Group the user belongs to, e.g., 'group_01'
)
user_id = user.user_id     # Unique identifier for the created user

user = users.getUser(user_id: str)  # Get user by their ID

user.update(
    name: str,               # Update the user's name
    gmail: str,              # Update the user's email
    location: str,           # Update location
    birthday: datetime,      # Update birthday
    group_id: str,           # Update group membership
    **kwargs                 # Other optional fields like gender, profile picture
)

user.upgrade()             # Upgrade the user's status, role, or permissions

readable_user = user.read(
    format = Literal['dict', 'bson'],  # Format of the returned data (dict or bson)
    print_console = Literal[True, False],  # Print the result in the console or not
    ...
)

user.active()              # Activate the user, making them available for interactions
user.energize(amt: int)     # Increase the user's energy by a specified amount
user.exhaust(amt: int)      # Decrease the user's energy by a specified amount

user.report(
    user_id: int,            # ID of the user to be reported
    reason: str              # Reason for reporting the user (e.g., 'abusive behavior')
)

user.block(
    user_id: int,            # ID of the user to block
    reason: str              # Reason for blocking the user (e.g., 'spam')
)

user.unblock(
    user_id: int,            # ID of the user to unblock
    reason: str              # Reason for unblocking the user (e.g., 'misunderstanding')
)

user.delete()              # Delete the user's account permanently
```

## Profile

```python
user.profile.read(
    format = Literal['dict', 'bson'],  # Format of returned profile data
    print_console = Literal[True, False],  # Print profile data in console
    filter: dict,             # Filter conditions for reading specific profile data
)
user.profile.update(
    name: str,               # Update the name of the user
    pfp: str,                # URL or file path to the user's profile picture
    status: str,             # User's current status message
    bio: str,                # Short biography of the user
    gender: Literal['Male', 'Female', 'Other'],  # Gender identity of the user
    location: str,           # Geographical location of the user
    birthday: datetime,      # Updated birthdate
    relationship: str,       # Relationship status (e.g., 'Single', 'In a relationship')
    orientation: str,        # Sexual orientation (e.g., 'Heterosexual', 'Homosexual')
    **kwargs                 # Other optional attributes (e.g., personal interests)
)
```

### Personality Type

```python
user.profile.personality.read(ptype: str=None)  # Read specific personality type details
user.profile.personality.update(
    mbti: str = None,        # MBTI personality type (e.g., 'INFJ', 'ENTP')
    dom: str = None,         # Dominant personality trait (e.g., 'Analytical', 'Creative')
    moral: str = None,       # Moral alignment (e.g., 'Lawful', 'Chaotic')
    enneg: str = None,       # Enneagram type (e.g., 'Type 1', 'Type 5')
    tempr: str = None,       # Temperament (e.g., 'Choleric', 'Phlegmatic')
    analytical: str = None,  # Analytical approach (e.g., 'Logical', 'Emotional')
    zodiac: str = None,      # Zodiac sign (e.g., 'Pisces', 'Leo')
    mental_age: str = None,  # Mental age (e.g., 'Adult', 'Teen')
    **kwargs                 # Additional personality-related parameters
)
```

### Academics

```python
user.profile.academics.read(filter: dict)  # Read academic data with filter conditions
user.profile.academics.update(
    certifications: list,        # List of certifications (e.g., ['Python', 'Data Science'])
    projects: list,              # List of academic projects (e.g., ['AI Model', 'Robotics'])
    skills: list,                # List of skills (e.g., ['Python', 'Machine Learning'])
    education: list,             # List of education history (e.g., ['B.Tech in CS'])
    workExp: list,               # List of work experience details
    **kwargs                     # Other academic-related information
)
```

#### Projects

```python
user.profile.academics.projects.read(filter: dict)  # Read academic projects with filters
proj = user.profile.academics.projects.add(
    name: str,               # Project name (e.g., 'AI Research')
    link: str,               # Project link or URL
    description: str,        # Short project description
    since: datetime,         # Start date of the project
    till: datetime = None,   # End date of the project (optional)
    **kwargs                 # Any additional details like role, tools used, etc.
)
proj.update(
    name: str = None,        # Update project name
    link: str = None,        # Update project URL
    description: str = None, # Update project description
    since: datetime = None,  # Update start date
    till: datetime = None,   # Update end date
    **kwargs                 # Other updates
)
proj.delete()              # Delete the project from the list
```

#### Skills

```python
user.profile.skills.read()         # Read skills list
user.profile.skills.add(           # Add a new skill
    name: str,                     # Name of the skill (e.g., 'Python', 'Project Management')
    description: str,              # Description of the skill
    **kwargs                       # Additional details such as skill proficiency
)
user.profile.skills.update(        # Update existing skill
    name: str = None,               # Updated skill name
    description: str = None,        # Updated description
    **kwargs                        # Additional updated fields
)
user.profile.skills.delete()       # Delete a skill from the user's profile
```

#### Certifications

```python
user.profile.certifications.read(filter: dict)  # Read certifications based on filters
cert = user.profile.certifications.add(
    name: str,                      # Certification name (e.g., 'AWS Certified Solutions Architect')
    org: str,                       # Issuing organization (e.g., 'Amazon')
    link: str,                      # Link to certification or credential
    description: str,               # Short description of certification
    since: datetime,                # Date when the certification was issued
    till: datetime = None,          # Date when certification expires (optional)
    **kwargs                        # Additional details about certification
)
cert.update(
    name: str = None,               # Update certification name
    org: str = None,                # Update issuing organization
    link: str = None,               # Update certification link
    description: str = None,        # Update description
    since: datetime = None,         # Update start date
    till: datetime = None,          # Update expiration date
    **kwargs                        # Additional updates
)
cert.delete()                      # Delete the certification
```

#### Education

```python
user.profile.education.read(
    filter: dict,                  # Conditions to filter education details
    query_vars: list,              # Specific query variables to be included
    limit: int,                    # Limit number of education records
)
edu = user.profile.education.add(
    name: str,                     # Name of the institution
    degree: str,                   # Degree obtained (e.g., 'B.Tech', 'M.Sc')
    field: str,                    # Field of study (e.g., 'Computer Science')
    link: str,                     # Link to institution's website or relevant resource
    org: str,                      # Organization or university name
    since: datetime,               # Start date of education
    till: datetime = None,         # End date of education (optional)
)
edu.update(
    name: str = None,              # Update institution name
    degree: str = None,            # Update degree name
    field: str = None,             # Update field of study
    link: str = None,              # Update institution
    org: str = None,               # Update organization/university name
    since: datetime = None,        # Update start date
    till: datetime = None,         # Update end date
    **kwargs                       # Other optional parameters
)
edu.delete()                       # Delete education record
``` 
Here is the missing part of the code, formatted with proper parameters and descriptions:

---

## Work Experience

```python
user.profile.workExp.read()  # Retrieve work experience details

user.profile.workExp.add(
    position: str,  # Position held in the company
    company: str,  # Name of the company
    start_date: datetime,  # Start date of the work experience
    end_date: datetime = None,  # End date of the work experience (optional)
    description: str = '',  # Description of responsibilities or achievements
)

user.profile.workExp.update(
    work_id: str,  # ID of the work experience to update
    position: str = None,  # New position (optional)
    company: str = None,  # New company name (optional)
    start_date: datetime = None,  # New start date (optional)
    end_date: datetime = None,  # New end date (optional)
    description: str = None,  # New description (optional)
)

user.profile.workExp.delete(
    work_id: str  # ID of the work experience to delete
)
```

### Interests

```python
user.profile.interests.read(
    filter: dict = None,  # Filter to apply for interest retrieval
    query_vars: list = None,  # List of query variables for detailed filtering
    limit: int = 10,  # Maximum number of results to return
)

intr = user.profile.interests.add(
    name: str,  # Name of the interest
    description: str,  # Description of the interest
    since: datetime,  # Date when the interest started
    till: datetime = None,  # Optional: Date when the interest ended
)

intr.update(
    name: str = None,  # Update the name of the interest (optional)
    description: str = None,  # Update the description of the interest (optional)
    since: datetime = None,  # Update the start date (optional)
    till: datetime = None,  # Update the end date (optional)
)

intr.delete()  # Delete the interest
```

### Hobbies

```python
user.profile.hobbies.read(
    filter: dict = None,  # Filter to apply for hobbies retrieval
    query_vars: list = None,  # List of query variables for detailed filtering
    limit: int = 10,  # Maximum number of results to return
)

hob = user.profile.hobbies.add(
    name: str,  # Name of the hobby
    description: str,  # Description of the hobby
    since: datetime,  # Date when the hobby started
    till: datetime = None,  # Optional: Date when the hobby ended
)

hob.update(
    name: str = None,  # Update the name of the hobby (optional)
    description: str = None,  # Update the description of the hobby (optional)
    since: datetime = None,  # Update the start date (optional)
    till: datetime = None,  # Update the end date (optional)
)

hob.delete()  # Delete the hobby
```

### Ratings

```python
user.profile.ratings.read(
    filter: dict = None,  # Filter to apply for ratings retrieval
    query_vars: list = None,  # List of query variables for detailed filtering
    limit: int = 10,  # Maximum number of results to return
)

rating = user.profile.ratings.add(
    user_id: str,  # ID of the user being rated
    rating: int,  # Rating given (e.g., 1 to 5)
)

rating.delete()  # Delete the rating

rating.update(
    rating: int,  # New rating value
)

user.profile.ratings.clear()  # Clear all ratings
```

### Likes

```python
user.profile.likes.read(
    filter: dict = None,  # Filter to apply for likes retrieval
    query_vars: list = None,  # List of query variables for detailed filtering
    limit: int = 10,  # Maximum number of results to return
)

user.profile.likes.add(
    user_id: int,  # ID of the user to like
)

user.profile.likes.remove(
    user_id: int,  # ID of the user to remove from likes
)

user.profile.likes.update(
    user_id: int,  # ID of the user whose like to update
)

user.profile.likes.clear()  # Clear all likes
```

### Views

```python
user.profile.getViews()  # Get the number of views on the user's profile

user.profile.view()  # Mark the profile as viewed
```

## Terminal

```python
user.terminal.read(
    filter: dict = None,  # Optional filter for terminal history or settings
    query_vars: list = None,  # Optional query variables for detailed filtering
    limit: int = None,  # Limit the number of results
)

user.terminal.query(
    query: str,  # Query to be executed in the terminal
    **kwargs  # Additional parameters for the query
)

user.terminal.setSelf(
    mode: str,  # Set the self mode (e.g., 'user', 'admin')
    **kwargs  # Additional settings for self mode
)

user.terminal.setGlobal(
    mode: str,  # Set the global mode (e.g., 'read', 'write')
    **kwargs  # Additional settings for global mode
)

user.terminal.setGroupMode(
    group_id: str,  # Group ID to set the mode for
    role: str,  # Role within the group (e.g., 'member', 'admin')
    **kwargs  # Additional settings for the group mode
)

user.terminal.setCompanyMode(
    company_id: str,  # Company ID to set the mode for
    role: str,  # Role within the company (e.g., 'employee', 'manager')
    **kwargs  # Additional settings for the company mode
)
```

## Jobs

```python
user.jobs.getJobs()  # Get a list of available jobs

job = user.jobs.getJob(
    job_id: str  # ID of the specific job to retrieve
)

job.read()  # Read the job details

job.update(
    job_id: str,  # Job ID to update
    position: str = None,  # New job position (optional)
    description: str = None,  # New job description (optional)
    requirements: str = None,  # New job requirements (optional)
)

job.delete(
    job_id: str  # Job ID to delete
)

job.getInfo()  # Get additional information about the job

user.jobs.getJobHistory()  # Get the history of jobs
```
#### Work Experience
```python
user.profile.workExp.read()  # Read work experience details

user.profile.workExp.add(
    position: str,  # Position held
    company: str,  # Company name
    start_date: datetime,  # Start date of employment
    end_date: datetime = None,  # End date (optional)
    description: str = '',  # Description of role
)

user.profile.workExp.update(
    work_id: str,  # ID of the work experience to update
    position: str = None,  # Updated position (optional)
    company: str = None,  # Updated company name (optional)
    start_date: datetime = None,  # Updated start date (optional)
    end_date: datetime = None,  # Updated end date (optional)
    description: str = None,  # Updated description (optional)
)

user.profile.workExp.delete(
    work_id: str  # ID of the work experience to delete
)
```

### Interests 
```python
user.profile.interests.read(
    filter: dict = None,  # Filter criteria for reading interests
    query_vars: list = None,  # List of query variables for detailed filtering
    limit: int = 10,  # Limit the number of results
)

intr = user.profile.interests.add(
    name: str,  # Name of the interest
    description: str,  # Description of the interest
    since: datetime,  # Start date of interest
    till: datetime = None,  # End date (optional)
)

intr.update(
    name: str = None,  # Update the name of the interest (optional)
    description: str = None,  # Update the description (optional)
    since: datetime = None,  # Update the start date (optional)
    till: datetime = None,  # Update the end date (optional)
)

intr.delete()  # Delete the interest
```

### Hobbies
```python
user.profile.hobbies.read(
    filter: dict = None,  # Filter criteria for reading hobbies
    query_vars: list = None,  # List of query variables for filtering
    limit: int = 10,  # Limit the number of results
)

hob = user.profile.hobbies.add(
    name: str,  # Name of the hobby
    description: str,  # Description of the hobby
    since: datetime,  # Start date of hobby
    till: datetime = None,  # End date (optional)
)

hob.update(
    name: str = None,  # Update the hobby name (optional)
    description: str = None,  # Update the description (optional)
    since: datetime = None,  # Update the start date (optional)
    till: datetime = None,  # Update the end date (optional)
)

hob.delete()  # Delete the hobby
```

### Ratings
```python
user.profile.ratings.read(
    filter: dict = None,  # Filter criteria for reading ratings
    query_vars: list = None,  # List of query variables for filtering
    limit: int = 10,  # Limit the number of results
)

rating = user.profile.ratings.add(
    user_id: str,  # User being rated
    rating: int,  # Rating value
)

rating.delete()  # Delete the rating

rating.update(
    rating: int,  # Update the rating value
)

user.profile.ratings.clear()  # Clear all ratings
```

### Likes
```python
user.profile.likes.read(
    filter: dict = None,  # Filter criteria for reading likes
    query_vars: list = None,  # List of query variables for filtering
    limit: int = 10,  # Limit the number of results
)

user.profile.likes.add(
    user_id: int,  # User ID to like
)

user.profile.likes.remove(
    user_id: int,  # User ID to remove from likes
)

user.profile.likes.update(
    user_id: int,  # User ID to update the like
)

user.profile.likes.clear()  # Clear all likes
```

### Views
```python
user.profile.getViews()  # Get the number of views on the profile

user.profile.view()  # Mark the profile as viewed
```

## Terminal
```python
user.terminal.read(
    filter: dict = None,  # Filter criteria for terminal history or settings
    query_vars: list = None,  # List of query variables for filtering
    limit: int = None,  # Limit the number of results
)

user.terminal.query(
    query: str,  # Query to execute in the terminal
    **kwargs  # Additional query parameters
)

user.terminal.setSelf(
    mode: str,  # Self mode (e.g., 'user', 'admin')
    **kwargs  # Additional settings for self mode
)

user.terminal.setGlobal(
    mode: str,  # Global mode (e.g., 'read', 'write')
    **kwargs  # Additional settings for global mode
)

user.terminal.setGroupMode(
    group_id: str,  # Group ID to set mode for
    role: str,  # Role within the group (e.g., 'member', 'admin')
    **kwargs  # Additional settings for group mode
)

user.terminal.setCompanyMode(
    company_id: str,  # Company ID to set mode for
    role: str,  # Role within the company (e.g., 'employee', 'manager')
    **kwargs  # Additional settings for company mode
)
```

## Jobs
```python
user.jobs.getJobs()  # Get a list of available jobs

job = user.jobs.getJob(
    job_id: str  # ID of the job to retrieve
)

job.read()  # Read job details

job.update(
    job_id: str,  # Job ID to update
    position: str = None,  # New job position (optional)
    description: str = None,  # New job description (optional)
    requirements: str = None,  # New job requirements (optional)
)

job.delete(
    job_id: str  # Job ID to delete
)

job.getInfo()  # Get job-specific information

user.jobs.getJobHistory()  # Get the job history
```
---
## Requests

### **Send Requests**
When sending requests, multiple types, statuses, and categories of requests can be handled. Below are expanded functions with detailed parameters and potential additional settings for flexibility.

```python
# Sending a request
req = user1.requests.createRequest(
    request_type: str,  # Type of request ('friend', 'connection', 'project', 'collaboration', etc.)
    recipient_id: str,  # User ID of the recipient
    subject: str,  # Short subject line for the request (e.g., 'Job Opportunity', 'Collaboration Proposal')
    details: str,  # Full description or message for the request
    status: str = 'pending',  # Default status can be 'pending', 'urgent', 'waiting_for_approval', etc.
    priority: str = 'normal',  # Request priority level ('low', 'medium', 'high')
    urgency: str = 'standard',  # Urgency level ('low', 'normal', 'high')
    category: str = 'general',  # Categorize the request ('social', 'work', 'study', 'business', etc.)
    tags: list = None,  # Optional list of tags for better organization (e.g., ['urgent', 'important'])
    attachments: list = None,  # Optional list of files to attach (can be links or file objects)
    created_at: datetime = None,  # Timestamp for when the request was created (optional)
    expires_at: datetime = None,  # Expiration date for the request, after which it is no longer valid (optional)
    metadata: dict = None,  # Additional metadata (e.g., source of the request, origin IP, etc.)
    read_receipt: bool = False,  # Whether to request a read receipt (optional)
    confirmation_required: bool = False,  # Whether recipient confirmation is needed (optional)
    priority_level: str = 'low',  # Priority of the request (e.g., 'high', 'medium', 'low')
)

# Retrieving sent requests
user1.requests.readSent(
    filter: dict = None,  # Filter criteria for sent requests (e.g., 'status': 'pending')
    query_vars: list = None,  # Query variables to customize the request (e.g., ['status', 'category'])
    limit: int = 10,  # Limit the number of sent requests to retrieve
    include_attachments: bool = False,  # Whether to include attachments in the response
    sort_by: str = 'date',  # Sort requests by date, status, or other relevant fields
    order: str = 'desc',  # Sorting order ('asc', 'desc')
    sent_by: str = None,  # Filter by the user who sent the request (optional)
)

# Updating an existing request
req.update(
    request_id: str,  # ID of the request to update
    status: str = None,  # New status ('pending', 'accepted', 'rejected', etc.)
    priority: str = None,  # Update priority level ('low', 'medium', 'high')
    category: str = None,  # Update category ('work', 'social', etc.)
    details: str = None,  # Update request message or details
    recipient_id: str = None,  # Change recipient if necessary
    attachments: list = None,  # Attach new files to the request
    expiration_date: datetime = None,  # Change expiration date
    read_receipt: bool = None,  # Toggle read receipt (True/False)
)

# Deleting a request
req.delete(
    request_id: str,  # Request ID to delete
    soft_delete: bool = False,  # Whether to perform a soft delete (keep record for history)
    permanently: bool = False,  # Permanent deletion (irreversible)
)

# Drafting a request (save as draft without sending)
req.draft(
    recipient_id: str,  # Recipient of the request
    request_type: str,  # Type of request (social, work, etc.)
    details: str,  # Full message or details for the request
    status: str = 'draft',  # Status when saved as a draft
    expiration_date: datetime = None,  # Optional expiration date
)

# Sending a drafted request
req.send(
    draft_id: str,  # Draft ID to be sent
)

# Confirming or acknowledging a request
req.confirm(
    request_id: str,  # Confirm the request's acceptance
    confirmation_message: str = "Confirmed",  # Optional message for confirmation
)

req.acknowledge(
    request_id: str,  # Acknowledge the request without confirming
    ack_message: str = "Acknowledged",  # Optional message for acknowledgment
)

# Sending an urgent request (with higher priority)
req.sendUrgent(
    recipient_id: str,  # Urgent recipient
    request_type: str,  # Urgent request type
    details: str,  # Details of the urgent request
    urgency_level: str = 'high',  # Urgency level ('normal', 'urgent', 'critical')
    priority_level: str = 'high',  # Priority level
)
```

---

### **Receive Requests**

When receiving requests, you need to handle various scenarios and edge cases, like filtering requests based on their status, sender, priority, etc. Here’s an expanded view of receiving and managing requests.

```python
# Reading inbox requests
user1.requests.readInbox(
    filter: dict = None,  # Filter requests by status, sender, category, etc.
    query_vars: list = None,  # List of query variables to filter (e.g., ['status', 'priority'])
    limit: int = 10,  # Limit number of requests in the inbox
    include_attachments: bool = False,  # Whether to include attachments
    sort_by: str = 'date',  # Sort requests by 'date', 'priority', etc.
    order: str = 'desc',  # Sorting order ('asc', 'desc')
)

# Reading a specific request from inbox
req = user1.requests.getInbox(
    req_id: str,  # Request ID to read
    include_attachments: bool = False,  # Whether to include attachments
    check_status: bool = True,  # Check the status before retrieving
)

# Accepting a request
req.accept(
    request_id: str,  # Request ID to accept
    confirm_message: str = "Accepted",  # Confirmation message (optional)
    accept_time: datetime = None,  # Time of acceptance (optional)
)

# Denying a request
req.deny(
    request_id: str,  # Request ID to deny
    deny_reason: str = "Not interested",  # Optional reason for denial
)

# Responding to a request (can include a detailed response)
req.respond(
    request_id: str,  # Request ID to respond to
    response_message: str,  # Detailed response message
    response_time: datetime = None,  # Timestamp of the response
)

# Ignoring a request (mark as ignored, no further action needed)
req.ignore(
    request_id: str,  # Request ID to ignore
)

# Blocking a sender (no future requests from this sender)
req.block(
    sender_id: str,  # Block sender by user ID
)

# Unblocking a sender
req.unblock(
    sender_id: str,  # Unblock sender by user ID
)

# Deleting a request from inbox
req.delete(
    request_id: str,  # Request ID to delete
    soft_delete: bool = False,  # Whether to perform soft delete
    permanently: bool = False,  # Permanent deletion
)

# Clearing all requests (bulk delete or clear inbox)
user1.requests.clearAll(
    status: str = 'unread',  # Clear all requests with a certain status (e.g., 'read', 'unread', etc.)
    category: str = None,  # Clear requests from a specific category (optional)
    priority: str = None,  # Clear requests of a specific priority level (optional)
)

# Approving or rejecting multiple requests at once
user1.requests.batchProcess(
    request_ids: list,  # List of request IDs to approve/reject
    action: str = 'approve',  # Action to perform ('approve', 'reject')
    custom_message: str = None,  # Custom message for batch processing (optional)
)

# Read request receipt confirmation (if enabled)
req.readReceipt(
    request_id: str,  # Request ID to read receipt for
    status: str = 'read',  # Status of the request ('read', 'unread')
)
```
---

## Social

### Connection

Managing connections can involve various actions, including making new connections, checking connection statuses, and even managing blocked or unblocked connections. Here's a more detailed approach:

```python
# Connecting with another user
user1.connect(
    user2_id: str,  # User ID of the person to connect with
    connection_type: str = 'general',  # Type of connection (e.g., 'friend', 'professional', 'collaborator')
    message: str = None,  # Optional message to send with the connection request
    status: str = 'pending',  # Initial status of the connection ('pending', 'accepted', 'blocked')
    connection_strength: int = 0,  # Strength of the connection (0 = neutral, 10 = strong)
    connection_date: datetime = None,  # Date when the connection was made
    tags: list = None,  # Optional list of tags (e.g., ['important', 'business'])
    shared_interests: list = None,  # List of shared interests (optional)
    source: str = None,  # Where the connection request originated from (e.g., 'networking event', 'social media')
)

# Viewing all connections
user1.connections.viewAll(
    filter: dict = None,  # Filter criteria (e.g., 'status': 'accepted', 'type': 'friend')
    query_vars: list = None,  # Query variables for detailed filtering (e.g., ['connection_type', 'status'])
    limit: int = 10,  # Limit the number of connections displayed
    include_muted: bool = False,  # Whether to include muted connections in the view
    sort_by: str = 'connection_date',  # Sorting by connection date, name, or strength
    order: str = 'asc',  # Sorting order ('asc', 'desc')
)

# Checking the connection status
connection_status = user1.connections.checkStatus(
    user2_id: str,  # The ID of the user to check the connection status with
    include_muted: bool = False,  # Include muted connections
)

# Accepting a connection
user1.connections.accept(
    user2_id: str,  # User ID of the person to accept
    message: str = 'Accepted your connection request',  # Optional acceptance message
    accepted_at: datetime = None,  # Date and time when the connection was accepted
)

# Rejecting a connection
user1.connections.reject(
    user2_id: str,  # User ID of the person to reject
    message: str = 'Rejected your connection request',  # Optional rejection message
    rejected_at: datetime = None,  # Date and time when the connection was rejected
)

# Disconnecting a connection
user1.connections.disconnect(
    user2_id: str,  # User ID of the person to disconnect from
    disconnect_reason: str = 'No longer in contact',  # Optional reason for disconnecting
    disconnected_at: datetime = None,  # Date and time when the disconnection occurred
)

# Blocking a connection
user1.connections.block(
    user2_id: str,  # User ID of the person to block
    block_reason: str = 'Spam or inappropriate behavior',  # Reason for blocking (optional)
    block_time: datetime = None,  # Date and time when the block occurred
)

# Unblocking a connection
user1.connections.unblock(
    user2_id: str,  # User ID of the person to unblock
    unblock_reason: str = 'Mistake or changed circumstances',  # Optional reason for unblocking
    unblock_time: datetime = None,  # Date and time when the unblock occurred
)

# Muting a connection (temporarily ignore their activity)
user1.connections.mute(
    user2_id: str,  # User ID of the person to mute
    mute_duration: int = 7,  # Duration of mute in days (optional)
    mute_reason: str = 'Need a break from notifications',  # Optional mute reason
)

# Viewing muted connections
user1.connections.viewMuted(
    filter: dict = None,  # Filter muted connections (e.g., 'reason': 'personal space')
    query_vars: list = None,  # Query parameters for additional filtering (e.g., ['mute_duration'])
    limit: int = 10,  # Limit number of muted connections to show
    sort_by: str = 'mute_duration',  # Sorting by mute duration or other attributes
    order: str = 'desc',  # Sorting order ('asc', 'desc')
)

# Sending a message to a connection
user1.connections.sendMessage(
    user2_id: str,  # User ID of the connection to send a message to
    message: str,  # The message content
    message_type: str = 'text',  # Type of message ('text', 'image', 'video', etc.)
    attachment: str = None,  # Optional attachment (link or file path)
    sent_at: datetime = None,  # Timestamp for the message sent
)

# Reporting a connection for misconduct
user1.connections.report(
    user2_id: str,  # User ID of the connection being reported
    reason: str = 'Inappropriate content',  # Reason for the report
    report_time: datetime = None,  # Timestamp for when the report was made
    additional_notes: str = None,  # Optional notes for the report
)

# Searching for connections based on shared interests or attributes
user1.connections.search(
    interests: list = None,  # List of interests to search connections by (e.g., ['AI', 'Data Science'])
    tags: list = None,  # Tags for searching (e.g., ['business', 'technology'])
    location: str = None,  # Search by location (optional)
    mutual_friends: bool = False,  # Filter for mutual friends (optional)
    connection_type: str = 'general',  # Connection type filter (e.g., 'friend', 'work')
    limit: int = 10,  # Limit the number of search results
)
```

---

### Groups and Communities

This section deals with group interactions, which can involve both private and public groups. The operations here include creating, joining, and managing groups.

```python
# Creating a new group
group = user1.groups.create(
    group_name: str,  # Name of the group
    group_type: str = 'public',  # Group type ('public', 'private', 'restricted')
    description: str = '',  # Description of the group
    privacy_settings: dict = None,  # Optional privacy settings (e.g., 'only_admins', 'everyone')
    tags: list = None,  # Optional tags for the group (e.g., ['AI', 'Technology'])
    members: list = [],  # Initial list of members (optional)
    admin_id: str = user1.user_id,  # Initial admin ID (usually the creator)
    group_image: str = None,  # Optional group image (file path or URL)
)

# Joining a group
user1.groups.join(
    group_id: str,  # Group ID to join
    user_id: str = user1.user_id,  # User ID of the person joining
    join_time: datetime = None,  # Date and time of joining
)

# Leaving a group
user1.groups.leave(
    group_id: str,  # Group ID to leave
    leave_time: datetime = None,  # Timestamp for when the user left the group
)

# Posting to a group
user1.groups.postMessage(
    group_id: str,  # Group ID to post the message to
    message: str,  # Content of the message
    message_type: str = 'text',  # Type of message ('text', 'image', 'video')
    attachments: list = None,  # Optional list of attachments (images, documents, etc.)
    posted_at: datetime = None,  # Date and time of posting
)

# Managing group members (e.g., promoting, demoting)
user1.groups.manageMembers(
    group_id: str,  # Group ID to manage
    user_id: str,  # User ID of the member to manage
    action: str = 'promote',  # Action ('promote', 'demote', 'remove')
    role: str = 'admin',  # Role to assign if promoting (e.g., 'admin', 'member')
    reason: str = None,  # Reason for the action (optional)
)

# Searching for groups
user1.groups.search(
    group_name: str = None,  # Name of the group to search for
    tags: list = None,  # Tags to filter by
    privacy: str = None,  # Privacy level ('public', 'private')
    limit: int = 10,  # Limit the number of results
)
```

---

### Event Invitations

Managing events involves sending, accepting, and tracking event invitations, and we can integrate event planning with social connections.

```python
# Sending an event invitation
user1.events.sendInvite(
    event_id: str,  # Event ID for the invitation
    recipient_id: str,  # User ID of the recipient
    invitation_message: str = 'You are invited to our upcoming event!',  # Invitation message
    status: str = 'pending', 

 # Initial status of the invitation ('pending', 'accepted', 'declined')
    sent_at: datetime = None,  # Timestamp for sending the invitation
)

# Accepting an event invitation
user1.events.acceptInvite(
    event_id: str,  # Event ID for the invitation
    user_id: str = user1.user_id,  # User ID accepting the invitation
    accepted_at: datetime = None,  # Date and time of acceptance
)

# Declining an event invitation
user1.events.declineInvite(
    event_id: str,  # Event ID for the invitation
    user_id: str = user1.user_id,  # User ID declining the invitation
    declined_at: datetime = None,  # Date and time of decline
)
```
---


## Alerts

### Send Alerts

Alerts can be sent to specific users or groups, with the option to customize the message and set particular parameters for different audiences.

```python
# Send alert to a specific user
user1.allert.user(
    recipient_user_id: str,  # User ID of the recipient
    message: str,  # The message to send
    priority: str = 'normal',  # Priority level of the alert ('normal', 'high', 'critical')
    timestamp: datetime = None,  # Timestamp for when the alert is sent
    alert_type: str = 'notification',  # Type of alert ('notification', 'warning', 'error', 'info')
    context: str = 'general',  # Context of the alert (e.g., 'account', 'system', 'event')
    action_required: bool = False,  # Whether the user needs to take action
    urgency_level: int = 5,  # Urgency level (1 = low, 10 = high)
    expiration_time: datetime = None,  # When the alert expires (optional)
    custom_data: dict = None,  # Optional custom data related to the alert (e.g., {'user_action': 'reset_password'})
)

# Send alert to a list of users
user1.allert.users(
    user_list: list,  # List of user IDs to send the alert to
    message: str,  # The message to send
    priority: str = 'normal',  # Priority level of the alert
    timestamp: datetime = None,  # Timestamp for when the alert is sent
    alert_type: str = 'notification',  # Type of alert
    context: str = 'general',  # Context of the alert
    action_required: bool = False,  # Whether the users need to take action
    urgency_level: int = 5,  # Urgency level
    custom_data: dict = None,  # Optional custom data
)

# Send alert to moderators
user1.allert.mods(
    mod_list: list,  # List of moderator IDs to send the alert to
    message: str,  # The message to send
    priority: str = 'normal',  # Priority level of the alert
    timestamp: datetime = None,  # Timestamp for when the alert is sent
    alert_type: str = 'notification',  # Type of alert
    context: str = 'moderation',  # Context for moderators (e.g., 'content violation', 'user report')
    action_required: bool = True,  # Whether moderators need to take action
    urgency_level: int = 7,  # Urgency level (higher for moderation)
    escalation_level: str = 'low',  # Escalation level ('low', 'medium', 'high')
    custom_data: dict = None,  # Optional custom data related to the alert
)

# Send alert to managers
user1.allert.managers(
    manager_list: list,  # List of manager IDs to send the alert to
    message: str,  # The message to send
    priority: str = 'normal',  # Priority level of the alert
    timestamp: datetime = None,  # Timestamp for when the alert is sent
    alert_type: str = 'notification',  # Type of alert
    context: str = 'management',  # Context for managers (e.g., 'team update', 'project status')
    action_required: bool = False,  # Whether managers need to take action
    urgency_level: int = 6,  # Urgency level
    escalation_level: str = 'medium',  # Escalation level
    custom_data: dict = None,  # Optional custom data
)

# Send alert to admins
user1.allert.admins(
    admin_list: list,  # List of admin IDs to send the alert to
    message: str,  # The message to send
    priority: str = 'critical',  # Priority level of the alert
    timestamp: datetime = None,  # Timestamp for when the alert is sent
    alert_type: str = 'error',  # Type of alert (e.g., system failure, account issue)
    context: str = 'administration',  # Context for admins (e.g., 'security breach', 'critical system issue')
    action_required: bool = True,  # Whether admins need to take action
    urgency_level: int = 9,  # Urgency level (high priority for admins)
    escalation_level: str = 'high',  # Escalation level ('high', 'critical')
    custom_data: dict = None,  # Optional custom data
)

# Send a custom alert to a group of users
user1.allert.custom(
    custom_list: list,  # List of user IDs to send the custom alert to
    message: str,  # The message to send
    priority: str = 'normal',  # Priority level of the alert
    timestamp: datetime = None,  # Timestamp for when the alert is sent
    alert_type: str = 'notification',  # Type of alert
    context: str = 'custom',  # Context for the alert (user-defined)
    action_required: bool = False,  # Whether the users need to take action
    urgency_level: int = 5,  # Urgency level
    custom_data: dict = None,  # Optional custom data (e.g., {'event_type': 'webinar'})
    expiration_time: datetime = None,  # Expiration time for the alert
)
```

---

### Check Alerts

Managing and handling incoming alerts efficiently is essential. This section includes operations to read, clear, and manage alerts.

```python
# Read the latest alerts (limit the number of alerts)
user1.allerts.read(
    count: int = 5,  # Number of alerts to read
    filter: dict = None,  # Optional filter (e.g., 'priority': 'high', 'type': 'notification')
    query_vars: list = None,  # Optional query parameters for filtering (e.g., ['alert_type'])
    sort_by: str = 'timestamp',  # Sorting by timestamp (can also sort by priority or urgency level)
    order: str = 'desc',  # Sorting order ('asc', 'desc')
)

# Clear a specific alert by alert_id
user1.allerts.clear(
    alert_id: str,  # The ID of the alert to clear
    reason: str = 'Alert resolved',  # Optional reason for clearing the alert
    cleared_at: datetime = None,  # Timestamp for when the alert is cleared
)

# Clear all alerts
user1.allerts.clearAll(
    reason: str = 'Bulk clearance',  # Reason for clearing all alerts
    cleared_at: datetime = None,  # Timestamp for when the alerts are cleared
)

# Deny an alert sender (prevent further alerts from this sender)
user1.allerts.deny(
    sender_id: str,  # User ID or system ID of the sender
    deny_reason: str = 'Spam or irrelevant alerts',  # Reason for denial
    denied_at: datetime = None,  # Timestamp for when the denial occurs
)

# Deny all alert senders (bulk action)
user1.allerts.denyAll(
    deny_reason: str = 'System-wide spam filtering',  # Reason for denial
    denied_at: datetime = None,  # Timestamp for when the denial occurs
)

# Allow an alert sender (re-enable alerts from a specific sender)
user1.allerts.allow(
    sender_id: str,  # User ID or system ID of the sender
    allow_reason: str = 'Trusted user or system',  # Reason for allowing
    allowed_at: datetime = None,  # Timestamp for when the sender is allowed again
)

# Allow all alert senders (bulk action)
user1.allerts.allowAll(
    allow_reason: str = 'System settings reset',  # Reason for allowing
    allowed_at: datetime = None,  # Timestamp for when the action takes place
)

# Get a list of allowed alert senders' IDs
user1.allerts.allowedIds(
    filter: dict = None,  # Optional filter (e.g., 'type': 'trusted')
    query_vars: list = None,  # Optional query parameters (e.g., 'user_type')
    limit: int = 10,  # Limit number of results
)

# Get a list of denied alert senders' IDs
user1.allerts.deniedIds(
    filter: dict = None,  # Optional filter (e.g., 'reason': 'spam')
    query_vars: list = None,  # Optional query parameters (e.g., 'user_status')
    limit: int = 10,  # Limit number of results
)
```

---


## Economic Operations

### Wallet

```python
user1.wallet.read()  # Get current wallet information

user1.wallet.addMoney(
    amount: float,  # Amount to add to the wallet
    transaction_id: str,  # Unique identifier for the transaction
    source: str = 'deposit',  # Source of the money, e.g., 'deposit', 'transfer'
    notes: str = ''  # Optional: Additional notes about the transaction
)

user1.wallet.getMoney()  # Retrieve the current wallet balance

user1.wallet.removeMoney(
    amount: float,  # Amount to remove from the wallet
    transaction_id: str,  # Unique identifier for the transaction
    reason: str  # Reason for the withdrawal, e.g., 'payment', 'fee'
)

user1.wallet.clear()  # Clear the entire wallet

user1.wallet.upgrade(
    level: str  # New level to upgrade to, e.g., 'premium', 'vip'
)
```

### Safe

```python
user1.safe.read()  # Get current safe balance and details

user1.safe.addMoney(
    amount: float,  # Amount to add to the safe
    transaction_id: str,  # Unique identifier for the transaction
    source: str = 'deposit',  # Source of the money, e.g., 'deposit', 'transfer'
    notes: str = ''  # Optional: Additional notes about the transaction
)

user1.safe.getMoney()  # Retrieve the current balance in the safe

user1.safe.removeMoney(
    amount: float,  # Amount to remove from the safe
    transaction_id: str,  # Unique identifier for the transaction
    reason: str  # Reason for the withdrawal, e.g., 'emergency', 'purchase'
)

user1.safe.clear()  # Clear the entire safe

user1.safe.upgrade(
    level: str  # New level to upgrade to, e.g., 'secure', 'vault'
)
```
---

## Economic Operations

### Wallet

Managing the wallet's monetary operations effectively is crucial in a virtual economy, and it should support various parameters, features, and methods for users to interact with their virtual finances.

```python
# Read the wallet's current balance and transaction history
user1.wallet.read(
    filter: dict = None,  # Filter options (e.g., 'status': 'active')
    query_vars: list = None,  # Query parameters (e.g., ['currency', 'transaction_type'])
    limit: int = 10,  # Number of records to fetch (limit transaction history)
    sort_by: str = 'date',  # Sort transactions by date, amount, etc.
    order: str = 'desc',  # Order of results ('asc', 'desc')
)

# Add money to the wallet with optional metadata (e.g., source, transaction ID)
user1.wallet.addMoney(
    amount: float,  # Amount of money to add
    transaction_id: str = None,  # Optional transaction ID for tracking
    source: str = 'transfer',  # Source of money (e.g., 'transfer', 'earnings', 'deposit')
    reason: str = None,  # Reason for adding money (e.g., 'job payment')
    currency: str = 'USD',  # Currency type (e.g., 'USD', 'EUR', 'BTC')
    timestamp: datetime = None,  # Optional timestamp for when the money is added
)

# Get the current balance and available funds
user1.wallet.getMoney(
    currency: str = 'USD',  # Optional currency type to retrieve balance in specific currency
    include_locked: bool = False,  # Include locked (pending or frozen) funds in the balance
)

# Remove money from the wallet with optional reason and conditions
user1.wallet.removeMoney(
    amount: float,  # Amount of money to remove
    reason: str = 'payment',  # Reason for removing money (e.g., 'payment', 'purchase', 'withdrawal')
    currency: str = 'USD',  # Currency type to use for removal
    fee: float = 0.0,  # Optional transaction fee if applicable
    lock: bool = False,  # Lock the money for the operation (for secure transactions)
    timeout: int = 30,  # Timeout for the operation in seconds (e.g., for time-sensitive operations)
)

# Clear the wallet (use with caution; may be a full reset)
user1.wallet.clear(
    confirmation: bool = False,  # Confirm before clearing
    reason: str = 'user request',  # Reason for clearing the wallet (e.g., 'user request', 'error fix')
    cleared_at: datetime = None,  # Timestamp for when the wallet is cleared
)

# Upgrade wallet capabilities (e.g., increase limit, add premium features)
user1.wallet.upgrade(
    upgrade_type: str = 'premium',  # Type of upgrade (e.g., 'premium', 'business')
    duration: int = 30,  # Duration of the upgrade in days
    new_limits: dict = {'transaction_limit': 5000},  # New transaction or withdrawal limits
    additional_features: list = ['instant_transfer', 'high_security'],  # Additional features
    timestamp: datetime = None,  # Timestamp of the upgrade
)
```

### Safe

A virtual safe is used for securing funds and assets, and its operations can be more restrictive, with additional features such as withdrawal limits and security settings.

```python
# Read the safe's current balance and transaction history
user1.safe.read(
    filter: dict = None,  # Filter options (e.g., 'status': 'active')
    query_vars: list = None,  # Query parameters (e.g., ['currency', 'transaction_type'])
    limit: int = 10,  # Number of records to fetch
    sort_by: str = 'date',  # Sort by date, amount, etc.
    order: str = 'desc',  # Order of results ('asc', 'desc')
)

# Add money to the safe
user1.safe.addMoney(
    amount: float,  # Amount to add to the safe
    source: str = 'transfer',  # Source of the money (e.g., 'earnings', 'gift', 'loan repayment')
    reason: str = None,  # Reason for adding money (e.g., 'savings', 'payment')
    currency: str = 'USD',  # Currency type
    timestamp: datetime = None,  # Timestamp for the deposit
    transaction_id: str = None,  # Transaction ID (optional for tracking)
)

# Get the current balance in the safe
user1.safe.getMoney(
    currency: str = 'USD',  # Currency type to check balance in
    include_locked: bool = False,  # Include locked funds (for pending transactions)
)

# Remove money from the safe
user1.safe.removeMoney(
    amount: float,  # Amount to remove
    reason: str = 'withdrawal',  # Reason for removing money (e.g., 'emergency fund', 'purchase')
    fee: float = 0.0,  # Optional fee for the transaction
    currency: str = 'USD',  # Currency to use
    lock: bool = False,  # Lock funds for this transaction (for security)
    timeout: int = 30,  # Timeout for the operation (e.g., '30' seconds for urgency)
)

# Clear the safe (use with caution)
user1.safe.clear(
    confirmation: bool = False,  # Confirmation flag before clearing
    reason: str = 'user request',  # Reason for clearing the safe (e.g., 'error fix')
    cleared_at: datetime = None,  # Timestamp for clearing the safe
)

# Upgrade the safe's capacity or security level
user1.safe.upgrade(
    upgrade_type: str = 'high_security',  # Type of upgrade (e.g., 'premium', 'high_security')
    duration: int = 30,  # Duration of upgrade (in days)
    security_features: list = ['biometric_lock', 'two_factor_auth'],  # Additional security features
    new_limits: dict = {'withdrawal_limit': 5000},  # New withdrawal limits
    timestamp: datetime = None,  # Timestamp for the upgrade
)
```

### Banks

Bank accounts allow for more sophisticated operations, such as borrowing, lending, and loan closures. Banks can be customized with various parameters to simulate a realistic banking experience.

```python
# Read all banks associated with the user
user1.banks.read(
    filter: dict = None,  # Filter by attributes (e.g., 'status': 'active')
    query_vars: list = None,  # Query variables (e.g., ['bank_name', 'location'])
    limit: int = 5,  # Limit the number of banks returned
)

# Get a specific bank and create a new account in that bank
user1Bank = user1.banks.getBank(bank_id)
acc_id = user1Bank.createAccount(
    bank_id: str,  # Bank ID where the account is being created
    name: str,  # Account holder's name
    initial_amount: float = 1000,  # Initial deposit amount
    account_type: str = 'checking',  # Account type ('savings', 'checking')
    currency: str = 'USD',  # Currency for the account (e.g., 'USD', 'BTC')
    interest_rate: float = 0.03,  # Optional interest rate for savings accounts
    overdraft_protection: bool = False,  # Whether overdraft protection is enabled
)

# Get a list of accounts in the bank
user1Bank.getAccounts(bank_id).read(
    filter: dict = None,  # Filter for accounts (e.g., 'active': True)
    query_vars: list = None,  # Query parameters (e.g., 'account_type', 'status')
    limit: int = 5,  # Limit results (optional)
)

# Get a specific account and perform operations
user1Bank.getAccount(acc_id).read()  # Get account details
user1Bank.getAccount(acc_id).addMoney(1000)  # Deposit money into account
user1Bank.getAccount(acc_id).getMoney()  # Get current balance
user1Bank.getAccount(acc_id).removeMoney(1000)  # Withdraw money

# Borrow money from the bank with conditions
user1Bank.getAccount(acc_id).borrowReq(
    amount: float,  # Amount to borrow
    collateral: dict = None,  # Collateral (e.g., {'property': 'house', 'value': 50000})
    loan_type: str = 'personal',  # Type of loan ('personal', 'mortgage', 'auto')
    interest_rate: float = 0.05,  # Interest rate
    repayment_period: int = 12,  # Loan repayment period in months
    approval_status: str = 'pending',  # Loan approval status ('pending', 'approved', 'denied')
)

# Process a loan borrowing request
lend_id = user1.requests.read(
    filter: {
        "status": "pending",
        "fromType": "bank",
        "details": {"bank_id": bank_id, "account_id

": acc_id, "type": "borrow"},
    },
    query_vars: ["lend_id"],
)["lend_id"]

# Approve the loan and finalize borrowing
user1Bank.getAccount(acc_id).borrow(
    amount: float,  # Amount of loan
    lend_id: str,  # Lending ID
)

# Close the loan and pay it off
user1Bank.getAccount(acc_id).borrowClosure(
    lend_id: str,  # Lending ID to close
    amount_paid: float,  # Amount paid to close loan
)

# Clear the account (e.g., delete or reset account)
user1Bank.getAccount(acc_id).clear()

# Upgrade account features (e.g., interest rates, fees)
user1Bank.getAccount(acc_id).upgrade(
    upgrade_type: str = 'premium',  # Type of upgrade (e.g., 'premium', 'business')
    features: list = ['higher_interest', 'no_fee'],  # Additional features
    duration: int = 30,  # Duration of the upgrade
)

# Delete the account
user1Bank.delAccounts(acc_id)

# Delete the bank
user1.banks.delBank(bank_id)
```

### **Status**
Users can maintain their statuses for various reasons, such as updates, alerts, or even tracking.

```python
# Read status updates
user1.status.read(
    filter: dict = None,  # Filters for status (e.g., 'active': True)
    query_vars: list = None,  # Query parameters for specific statuses
    limit: int = 5,  # Limit number of statuses returned
)

# Add a new status update
user1.status.addStatus(
    link: str,  # URL or reference link
    description: str = None,  # Additional details or description for the status
    visibility: str = 'public',  # Visibility options ('public', 'private', 'friends')
    timestamp: datetime = None,  # Timestamp of the status update
)

# Remove a status update
user1.status.removeStatus(
    status_id: str,  # ID of the status to remove
)
```

