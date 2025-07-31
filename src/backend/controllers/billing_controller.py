from flask import jsonify
from datetime import datetime

class BillingController:
    """
    Controller for billing and usage tracking
    """
    
    @staticmethod
    def get_all_billing_records(page=1, limit=20, filters=None):
        """
        Get all billing records with pagination and filtering
        """
        try:
            # Mock billing records
            mock_records = [
                {
                    "id": "1",
                    "account_id": "1",
                    "account_name": "Demo Account 1",
                    "billing_period": "2024-01",
                    "subjects_count": 25,
                    "respondents_count": 150,
                    "surveys_count": 5,
                    "amount": 299.99,
                    "status": "paid",
                    "created_at": "2024-01-01T00:00:00Z",
                    "paid_at": "2024-01-05T00:00:00Z"
                },
                {
                    "id": "2",
                    "account_id": "2",
                    "account_name": "Demo Account 2",
                    "billing_period": "2024-01",
                    "subjects_count": 10,
                    "respondents_count": 60,
                    "surveys_count": 2,
                    "amount": 149.99,
                    "status": "pending",
                    "created_at": "2024-01-01T00:00:00Z",
                    "due_date": "2024-01-15T00:00:00Z"
                }
            ]
            
            # Apply filters if provided
            if filters:
                if filters.get('account_id'):
                    mock_records = [r for r in mock_records if r['account_id'] == filters['account_id']]
                if filters.get('status'):
                    mock_records = [r for r in mock_records if r['status'] == filters['status']]
                if filters.get('billing_period'):
                    mock_records = [r for r in mock_records if r['billing_period'] == filters['billing_period']]
            
            # Apply pagination
            start_idx = (page - 1) * limit
            end_idx = start_idx + limit
            paginated_records = mock_records[start_idx:end_idx]
            
            return jsonify({
                "success": True,
                "data": paginated_records,
                "pagination": {
                    "page": page,
                    "limit": limit,
                    "total": len(mock_records),
                    "pages": (len(mock_records) + limit - 1) // limit
                }
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve billing records: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_billing_record_by_id(billing_id):
        """
        Get specific billing record
        """
        try:
            mock_record = {
                "id": str(billing_id),
                "account_id": "1",
                "account_name": "Demo Account",
                "billing_period": "2024-01",
                "subjects_count": 25,
                "respondents_count": 150,
                "surveys_count": 5,
                "amount": 299.99,
                "status": "paid",
                "created_at": "2024-01-01T00:00:00Z",
                "paid_at": "2024-01-05T00:00:00Z",
                "details": {
                    "base_fee": 99.99,
                    "subject_fee": 100.00,
                    "respondent_fee": 75.00,
                    "survey_fee": 25.00
                }
            }
            
            return jsonify({
                "success": True,
                "data": mock_record
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve billing record: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_billing_by_account(account_id, page=1, limit=20, filters=None):
        """
        Get billing records for specific account
        """
        try:
            mock_records = [
                {
                    "id": "1",
                    "account_id": str(account_id),
                    "billing_period": "2024-01",
                    "subjects_count": 25,
                    "respondents_count": 150,
                    "surveys_count": 5,
                    "amount": 299.99,
                    "status": "paid",
                    "created_at": "2024-01-01T00:00:00Z"
                },
                {
                    "id": "2",
                    "account_id": str(account_id),
                    "billing_period": "2023-12",
                    "subjects_count": 20,
                    "respondents_count": 120,
                    "surveys_count": 4,
                    "amount": 249.99,
                    "status": "paid",
                    "created_at": "2023-12-01T00:00:00Z"
                }
            ]
            
            # Apply pagination
            start_idx = (page - 1) * limit
            end_idx = start_idx + limit
            paginated_records = mock_records[start_idx:end_idx]
            
            return jsonify({
                "success": True,
                "data": paginated_records,
                "pagination": {
                    "page": page,
                    "limit": limit,
                    "total": len(mock_records),
                    "pages": (len(mock_records) + limit - 1) // limit
                }
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve account billing: {str(e)}"}
            }), 500
    
    @staticmethod
    def get_billing_summary():
        """
        Get billing summary statistics
        """
        try:
            mock_summary = {
                "total_revenue": 15750.50,
                "monthly_revenue": 2499.99,
                "active_accounts": 25,
                "pending_payments": 3,
                "overdue_payments": 1,
                "current_period": "2024-01",
                "revenue_by_month": [
                    {"month": "2023-10", "revenue": 2100.00},
                    {"month": "2023-11", "revenue": 2300.50},
                    {"month": "2023-12", "revenue": 2450.75},
                    {"month": "2024-01", "revenue": 2499.99}
                ],
                "top_accounts": [
                    {"account_name": "Enterprise Corp", "revenue": 1200.00},
                    {"account_name": "Tech Solutions", "revenue": 899.99},
                    {"account_name": "Global Industries", "revenue": 750.50}
                ]
            }
            
            return jsonify({
                "success": True,
                "data": mock_summary
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to retrieve billing summary: {str(e)}"}
            }), 500
    
    @staticmethod
    def calculate_billing(subjects_count, respondents_count):
        """
        Calculate billing amount based on usage
        """
        try:
            # Mock pricing calculation
            base_fee = 99.99
            subject_fee_per_unit = 4.00
            respondent_fee_per_unit = 0.50
            
            subject_total = subjects_count * subject_fee_per_unit
            respondent_total = respondents_count * respondent_fee_per_unit
            total_amount = base_fee + subject_total + respondent_total
            
            calculation = {
                "base_fee": base_fee,
                "subjects_count": subjects_count,
                "subject_fee_per_unit": subject_fee_per_unit,
                "subject_total": subject_total,
                "respondents_count": respondents_count,
                "respondent_fee_per_unit": respondent_fee_per_unit,
                "respondent_total": respondent_total,
                "total_amount": round(total_amount, 2),
                "currency": "USD"
            }
            
            return jsonify({
                "success": True,
                "data": calculation
            })
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": {"message": f"Failed to calculate billing: {str(e)}"}
            }), 500
