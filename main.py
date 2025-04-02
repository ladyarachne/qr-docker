#!/usr/bin/env python3
import argparse
import os
import qrcode
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join('logs', 'qr_generator.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('qr_generator')

def generate_qr_code(url, output_path=None):
    """
    Generate a QR code for the given URL and save it to the specified path.
    
    Args:
        url (str): The URL to encode in the QR code
        output_path (str, optional): Path to save the QR code image. 
                                    If None, a default path will be used.
    
    Returns:
        str: The path where the QR code image was saved
    """
    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # Add data to the QR code
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Generate filename based on URL if output_path is not provided
        if output_path is None:
            # Extract domain from URL for filename
            from urllib.parse import urlparse
            domain = urlparse(url).netloc
            if not domain:
                domain = "custom_url"
            
            # Create timestamp for unique filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{domain}_{timestamp}.png"
            
            # Ensure qr_codes directory exists
            os.makedirs('qr_codes', exist_ok=True)
            
            output_path = os.path.join('qr_codes', filename)
        
        # Save the image
        img.save(output_path)
        logger.info(f"QR code for {url} generated successfully and saved to {output_path}")
        
        return output_path
    
    except Exception as e:
        logger.error(f"Error generating QR code: {str(e)}")
        raise

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate QR code for a URL')
    parser.add_argument('--url', type=str, default='http://github.com/ladyarachne',
                        help='URL to encode in QR code')
    parser.add_argument('--output', type=str, default=None,
                        help='Output path for QR code image')
    
    args = parser.parse_args()
    
    # Ensure logs directory exists
    os.makedirs('logs', exist_ok=True)
    
    # Generate QR code
    try:
        output_path = generate_qr_code(args.url, args.output)
        print(f"QR code generated successfully and saved to: {output_path}")
    except Exception as e:
        print(f"Failed to generate QR code: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
