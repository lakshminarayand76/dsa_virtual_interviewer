"""
Streamlit entrypoint for AI Virtual DSA Technical Interviewer.
Run with: streamlit run app.py
"""

import os
import sys

# Ensure src directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from ai_interviewer.app import *
