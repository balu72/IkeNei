from flask import Blueprint, request
from controllers.files_controller import FilesController
from middleware.auth_middleware import require_auth
from utils.response_helpers import validation_error_response, handle_exception

files_bp = Blueprint('files', __name__)

@files_bp.route('/api/upload', methods=['POST'])
@require_auth
def upload_file():
    """
    Upload files (avatars, documents)
    """
    try:
        if 'file' not in request.files:
            return validation_error_response({"file": "No file provided"})
        
        file = request.files['file']
        if file.filename == '':
            return validation_error_response({"file": "No file selected"})
        
        file_type = request.form.get('type', 'document')  # avatar, document, etc.
        
        return FilesController.upload_file(file, file_type)
    
    except Exception as e:
        return handle_exception(e)

@files_bp.route('/api/files/<int:file_id>', methods=['GET'])
@require_auth
def download_file(file_id):
    """
    Download/view files
    """
    try:
        return FilesController.download_file(file_id)
    
    except Exception as e:
        return handle_exception(e)

@files_bp.route('/api/files/<int:file_id>', methods=['DELETE'])
@require_auth
def delete_file(file_id):
    """
    Delete files
    """
    try:
        return FilesController.delete_file(file_id)
    
    except Exception as e:
        return handle_exception(e)
