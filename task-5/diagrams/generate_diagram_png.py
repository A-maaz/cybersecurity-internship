"""
Generates diagrams/architecture.png using Pillow.
Renders the 3-tier architecture diagram requested in Section 5 of the Capstone project.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_architecture_diagram():
    width = 1000
    height = 700
    
    # Create image with deep navy background
    img = Image.new("RGBA", (width, height), (10, 14, 23, 255))
    draw = ImageDraw.Draw(img)
    
    # Load fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 24)
        subtitle_font = ImageFont.truetype("arial.ttf", 14)
        box_title_font = ImageFont.truetype("arialbd.ttf", 16)
        text_font = ImageFont.truetype("arial.ttf", 13)
        code_font = ImageFont.truetype("consola.ttf", 12)
    except IOError:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        box_title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        code_font = ImageFont.load_default()
        
    # Draw Grid lines
    for x in range(0, width, 50):
        draw.line([(x, 0), (x, height)], fill=(25, 33, 50, 255), width=1)
    for y in range(0, height, 50):
        draw.line([(0, y), (width, y)], fill=(25, 33, 50, 255), width=1)
        
    # Header Titles
    draw.text((width // 2, 40), "PHISHAWARE SYSTEM & NETWORK ARCHITECTURE", fill=(248, 250, 252), font=title_font, anchor="mm")
    draw.text((width // 2, 70), "Controlled Educational Phishing Awareness Simulation & Incident Response Platform", fill=(148, 163, 184), font=subtitle_font, anchor="mm")
    
    # Box 1: Test User Browser (Top)
    b1_x1, b1_y1, b1_x2, b1_y2 = 250, 110, 750, 200
    draw.rectangle([b1_x1, b1_y1, b1_x2, b1_y2], fill=(19, 28, 46, 255), outline=(0, 210, 255, 255), width=2)
    draw.text((500, 138), "1. PRESENTATION TIER: Test User Browser (Synthetic Client)", fill=(0, 210, 255), font=box_title_font, anchor="mm")
    draw.text((500, 168), "Simulated Corporate Webmail Client  *  Safe Landing Pages  *  Awareness Curriculum", fill=(203, 213, 225), font=text_font, anchor="mm")
    
    # Arrow 1: Browser -> Flask
    draw.line([(500, 200), (500, 260)], fill=(0, 210, 255), width=3)
    draw.polygon([(493, 250), (507, 250), (500, 262)], fill=(0, 210, 255))
    draw.rectangle([520, 218, 700, 244], fill=(15, 23, 42), outline=(30, 41, 59))
    draw.text((610, 231), "HTTP Requests / Telemetry", fill=(0, 210, 255), font=code_font, anchor="mm")
    
    # Box 2: Flask Web Application (Middle)
    b2_x1, b2_y1, b2_x2, b2_y2 = 140, 265, 860, 520
    draw.rectangle([b2_x1, b2_y1, b2_x2, b2_y2], fill=(15, 23, 42, 255), outline=(59, 130, 246, 255), width=2)
    draw.rectangle([b2_x1, b2_y1, b2_x2, b2_y1 + 40], fill=(30, 41, 59, 255))
    draw.text((b2_x1 + 20, b2_y1 + 20), "2. APPLICATION TIER: Flask Core Engine (Python 3.13 / REST / Jinja2)", fill=(255, 255, 255), font=box_title_font, anchor="lm")
    
    # Sub-modules inside Box 2
    # Module A: Simulation Engine
    draw.rectangle([170, 325, 480, 405], fill=(10, 14, 23), outline=(30, 41, 59), width=1)
    draw.text((185, 345), "[A] Simulation Engine", fill=(0, 210, 255), font=box_title_font)
    draw.text((185, 370), "Campaign Config * Synthetic Dispatch * Webmail", fill=(148, 163, 184), font=text_font)
    
    # Module B: Awareness Training
    draw.rectangle([515, 325, 830, 405], fill=(10, 14, 23), outline=(30, 41, 59), width=1)
    draw.text((530, 345), "[B] Awareness Training Gateway", fill=(16, 185, 129), font=box_title_font)
    draw.text((530, 370), "Indicator Breakdowns * Interactive Threat Quiz", fill=(148, 163, 184), font=text_font)
    
    # Module C: Telemetry Event Logger
    draw.rectangle([170, 420, 480, 500], fill=(10, 14, 23), outline=(30, 41, 59), width=1)
    draw.text((185, 440), "[C] Telemetry Event Logger", fill=(245, 158, 11), font=box_title_font)
    draw.text((185, 465), "SENT, OPEN, CLICK, REPORT * Zero Harvest", fill=(148, 163, 184), font=text_font)
    
    # Module D: Incident Response & SOC
    draw.rectangle([515, 420, 830, 500], fill=(10, 14, 23), outline=(30, 41, 59), width=1)
    draw.text((530, 440), "[D] SOC Incident Response & Charts", fill=(239, 68, 68), font=box_title_font)
    draw.text((530, 465), "Anomaly Detection * Containment * Reports", fill=(148, 163, 184), font=text_font)
    
    # Arrow 2: Flask -> SQLite
    draw.line([(500, 520), (500, 575)], fill=(16, 185, 129), width=3)
    draw.polygon([(493, 565), (507, 565), (500, 577)], fill=(16, 185, 129))
    draw.rectangle([520, 535, 715, 561], fill=(15, 23, 42), outline=(30, 41, 59))
    draw.text((617, 548), "SQLAlchemy ORM (Localhost)", fill=(16, 185, 129), font=code_font, anchor="mm")
    
    # Box 3: SQLite Database (Bottom)
    b3_x1, b3_y1, b3_x2, b3_y2 = 250, 580, 750, 670
    draw.rectangle([b3_x1, b3_y1, b3_x2, b3_y2], fill=(19, 28, 46, 255), outline=(16, 185, 129, 255), width=2)
    draw.text((500, 608), "3. DATA TIER: SQLite Event Store (database/app.db)", fill=(16, 185, 129), font=box_title_font, anchor="mm")
    draw.text((500, 638), "Tables: Campaign * TestUser * Event * Incident * IncidentAction (Zero Passwords)", fill=(203, 213, 225), font=text_font, anchor="mm")
    
    output_path = os.path.join(os.path.dirname(__file__), 'architecture.png')
    img.save(output_path, "PNG")
    print(f"Architecture diagram saved to {output_path}")

if __name__ == '__main__':
    create_architecture_diagram()
