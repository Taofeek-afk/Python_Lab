# @app.get("")
# async def get_menus(
#     user: User = Depends(get_current_user),
#     session: AsyncSession = Depends(get_session),
#     page: int = Query(1, ge=1, le=100),
#     limit: int = Query(20, ge=1, le=100)
# ):
#     offset = (page - 1) * limit

#     stmt = (
#         select(MenuItem)
#         .order_by(MenuItem.id)
#         .offset(offset)
#         .limit(limit)
#     )
    
#     count = select(func.count(MenuItem.id))
#     total = await session.scalar(count)
    
#     total_pages = math.ceil(total/limit)
    
#     result = await session.scalars(stmt)

#     objects = result.all()

#     return {
#     "objects": objects,
#     "page": page,
#     "limit": limit,
#     "total":  total,
#     "total_pages": total_pages,
# }


# A restaurant owner asks:

# "Show me the cheapest and most expensive menu item price for every restaurant."

# Write the SQLAlchemy statement that gives you:

# restaurant_id
# minimum_price
# maximum_price


# select(
#     MenuItem.restaurant_id,
#     func.min(MenuItem.price),
#     func.max(MenuItem.price)
# ).group_by(
#     MenuItem.restaurant_id
# ) 


# stmt = (
#     select(MenuItem)
#     .where(MenuItem.id == 5)
#     .with_for_update()
# )

# menu_item = await session.scalar(stmt)

# if menu_item.stock < 2:
#     raise ValueError("Not enough stock")

# menu_item.stock -= 2

# await session.commit()

# GET /restaurants/{restaurant_id}/menu-items

# Required

# 1. Restaurant filtering

# Only return menu items belonging to the requested restaurant.

# 2. Searching

# Optional:

# ?search=pizza

# Search name using case-insensitive partial matching.

# 3. Price filtering

# Optional:

# ?min_price=1000
# ?max_price=5000

# Both should work independently.

# 4. Sorting

# Support:

# sort_order=asc
# sort_order=desc

# Sort by price.


# 5. Pagination

# Support:

# page=1
# limit=20

# Calculate:

# offset = (page - 1) * limit

# 6. Total count

# Return the total number of matching menu items before pagination.

# So if there are 73 matching items:

# total = 73
# limit = 20
# total_pages = 4
# 7. Efficient loading

# Because we're already filtering directly by restaurant_id, don't unnecessarily load the Restaurant relationship.

# 8. Ordering

# Always include a deterministic ordering.

# For example:

# price ASC, id ASC

# rather than sorting only by price, because two items can have the same price.

# Your task

# Write the complete FastAPI endpoint.

# You can use everything you've learned:

# FastAPI
# Query
# Depends
# AsyncSession
# select
# func.count
# ilike
# between / >= / <=
# order_by
# asc / desc
# offset
# limit

# Don't worry about the response Pydantic model yet—we haven't started that course.

# Return a dictionary such as:

# {


# stmt = select(MenuItem).where(
#     MenuItem.restaurant_id == restaurant_id
# )

# if search is not None:
#     stmt = stmt.where(
#         MenuItem.name.ilike(f"%{search}%")
#     )

# if min_price is not None:
#     stmt = stmt.where(MenuItem.price >= min_price)

# if max_price is not None:
#     stmt = stmt.where(MenuItem.price <= max_price)

# if sort_order == Sort.desc:
#     stmt = stmt.order_by(
#         MenuItem.price.desc(),
#         MenuItem.id
#     )
# else:
#     stmt = stmt.order_by(
#         MenuItem.price.asc(),
#         MenuItem.id
#     )

# offset = (page - 1) * limit

# count_stmt = select(func.count()).select_from(
#     stmt.subquery()
# )

# total = await session.scalar(count_stmt)

# stmt = stmt.offset(offset).limit(limit)

# result = await session.scalars(stmt)
# items = result.all()

# pages = math.ceil(total / limit)

# return {
#     "total": total,
#     "pages": pages,
#     "limit": limit,
#     "items": items,
# }

