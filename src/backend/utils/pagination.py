from flask import request
from config import Config

def get_pagination_params():
    """
    Extract pagination parameters from request
    """
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', Config.DEFAULT_PAGE_SIZE, type=int)
    
    # Ensure page is at least 1
    page = max(1, page)
    
    # Ensure limit is within bounds
    limit = min(max(1, limit), Config.MAX_PAGE_SIZE)
    
    return page, limit

def get_filter_params():
    """
    Extract common filter parameters from request
    """
    search = request.args.get('search', '', type=str).strip()
    sort = request.args.get('sort', 'created_at:desc', type=str)
    filter_param = request.args.get('filter', '', type=str)
    
    # Parse sort parameter
    sort_field = 'created_at'
    sort_direction = 'desc'
    
    if ':' in sort:
        sort_field, sort_direction = sort.split(':', 1)
        sort_direction = sort_direction.lower()
        if sort_direction not in ['asc', 'desc']:
            sort_direction = 'desc'
    
    # Parse filter parameter
    filters = {}
    if filter_param:
        for filter_item in filter_param.split(','):
            if ':' in filter_item:
                key, value = filter_item.split(':', 1)
                filters[key.strip()] = value.strip()
    
    return {
        'search': search,
        'sort_field': sort_field,
        'sort_direction': sort_direction,
        'filters': filters
    }

def paginate_mongo_query(collection, filter_dict, page, limit, sort_field='created_at', sort_direction='desc'):
    """
    Apply pagination to a MongoDB query
    """
    # Calculate skip value
    skip = (page - 1) * limit
    
    # Get total count
    total = collection.count_documents(filter_dict)
    
    # Build sort criteria
    sort_order = 1 if sort_direction == 'asc' else -1
    sort_criteria = [(sort_field, sort_order)]
    
    # Execute query with pagination
    cursor = collection.find(filter_dict).sort(sort_criteria).skip(skip).limit(limit)
    items = list(cursor)
    
    # Convert ObjectId to string for JSON serialization
    for item in items:
        if '_id' in item:
            item['id'] = str(item['_id'])
            del item['_id']
    
    has_prev = page > 1
    has_next = (page * limit) < total
    total_pages = (total + limit - 1) // limit  # Ceiling division
    
    return {
        'items': items,
        'pagination': {
            'page': page,
            'limit': limit,
            'total': total,
            'total_pages': total_pages,
            'has_prev': has_prev,
            'has_next': has_next,
            'prev_page': page - 1 if has_prev else None,
            'next_page': page + 1 if has_next else None
        }
    }

def build_mongo_filter(filters, search_term=None, search_fields=None):
    """
    Build MongoDB filter dictionary from request parameters
    """
    filter_dict = {}
    
    # Add search functionality
    if search_term and search_fields:
        search_conditions = []
        for field in search_fields:
            search_conditions.append({field: {'$regex': search_term, '$options': 'i'}})
        filter_dict['$or'] = search_conditions
    
    # Add other filters
    for key, value in filters.items():
        if value:
            # Handle boolean filters
            if value.lower() in ['true', 'false']:
                filter_dict[key] = value.lower() == 'true'
            # Handle date filters (you can extend this)
            elif key.endswith('_date') or key.endswith('_at'):
                # This would need more sophisticated date parsing
                pass
            else:
                filter_dict[key] = value
    
    return filter_dict

def create_paginated_response(data, pagination_info, message="Data retrieved successfully"):
    """
    Create a standardized paginated response
    """
    return {
        'success': True,
        'data': data,
        'pagination': pagination_info,
        'message': message
    }
