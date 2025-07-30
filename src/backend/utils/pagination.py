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

def paginate_query(query, page, limit):
    """
    Apply pagination to a SQLAlchemy query
    """
    total = query.count()
    items = query.offset((page - 1) * limit).limit(limit).all()
    
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
