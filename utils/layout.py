import os
import base64
import streamlit as st
import time
from pathlib import Path

def set_background(image_path):
    """
    Set background image for the Streamlit app with proper error handling
    """
    try:
        # Check if file exists
        if not os.path.exists(image_path):
            st.warning(f"Background image not found at: {image_path}")
            return
        
        # Read and encode the image
        with open(image_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        
        # Create CSS with proper background styling
        css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
        }}
        
        /* Ensure main content has good contrast */
        .stApp > div > div > div {{
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 10px;
            padding: 2rem;
            margin: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error loading background image: {str(e)}")

def load_css(file_path):
    """
    Load CSS file with proper error handling
    """
    try:
        if not os.path.exists(file_path):
            st.warning(f"CSS file not found at: {file_path}")
            return
            
        with open(file_path, 'r', encoding='utf-8') as f:
            css = f.read()
        
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Error loading CSS file: {str(e)}")

def typewriter(text_list, cursor_point="▌", speed=0.02, blink_speed=0.1, blinks=2, size="h5", color="MediumOrchid", center=True):
    """
    Improved typewriter effect with better performance
    """
    if not text_list:
        return
        
    placeholder = st.empty()
    align = "center" if center else "left"
    
    try:
        for text in text_list:
            typed = ""
            for char in text:
                typed += char
                placeholder.markdown(
                    f"<div style='text-align:{align};'><{size} style='color:{color};'>{typed}{cursor_point}</{size}></div>",
                    unsafe_allow_html=True
                )
                time.sleep(speed)
            
            # Blink effect
            for _ in range(blinks):
                placeholder.markdown(
                    f"<div style='text-align:{align};'><{size} style='color:{color};'>{typed}</{size}></div>",
                    unsafe_allow_html=True
                )
                time.sleep(blink_speed)
                placeholder.markdown(
                    f"<div style='text-align:{align};'><{size} style='color:{color};'>{typed}{cursor_point}</{size}></div>",
                    unsafe_allow_html=True
                )
                time.sleep(blink_speed)
            
            # Small pause between texts
            time.sleep(0.5)
            
    except Exception as e:
        st.error(f"Error in typewriter effect: {str(e)}")

def create_skill_tag(skill, color="#FFD700", text_color="#000000"):
    """
    Create a skill tag with customizable colors
    """
    return f'<span class="skill-tag" style="background-color: {color}; color: {text_color};">{skill}</span>'

def create_progress_bar(label, value, max_value=100):
    """
    Create a custom progress bar
    """
    percentage = (value / max_value) * 100
    return f"""
    <div style="margin: 10px 0;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
            <span>{label}</span>
            <span>{value}%</span>
        </div>
        <div style="background-color: #ddd; border-radius: 10px; height: 20px;">
            <div style="background-color: #4CAF50; width: {percentage}%; height: 100%; border-radius: 10px; transition: width 0.3s;"></div>
        </div>
    </div>
    """
