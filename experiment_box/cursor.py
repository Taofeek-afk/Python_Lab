# Design the first request and next request for:

# GET /menu-items

# where:

# the client requests 10 items
# the first request has no cursor
# the response gives the client a cursor
# the next request uses that cursor to retrieve the next 10


# Start with select(MenuItem)
# If search exists,
# If min_price exists,
# If max_price exists, 
# Sort by MenuItem.price descending
# Don't use if/else unnecessarily—the filters are independent.
