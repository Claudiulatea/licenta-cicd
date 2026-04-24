import os
import logging
from flask import Flask, jsonify

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

# API status endpoint
@app.route('/api/status', methods=['GET'])
def api_status():
    return jsonify({'status': 'running', 'timestamp': os.environ.get('CURRENT_TIMESTAMP')}), 200

# Error handling
@app.errorhandler(500)
def internal_error(error):
    logger.error(f'Internal Error: {error}')
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    # Load environment variables
    os.environ['CURRENT_TIMESTAMP'] = '2026-04-24 07:40:45'
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))