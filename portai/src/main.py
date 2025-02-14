import os
import sys
import logging
import asyncio
import traceback

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gui.interview_gui import InterviewGUI

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("interview_simulator.log"),  # Log to file
        logging.StreamHandler(sys.stdout),  # Log to console
    ],
)

logger = logging.getLogger(__name__)

# Configure asyncio policy for Windows
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def exception_handler(exc_type, exc_value, exc_traceback):
    """Handle uncaught exceptions and log them properly"""
    logger.error("Uncaught exception:", exc_info=(exc_type, exc_value, exc_traceback))
    # Print to stderr as well
    print("An error occurred:", file=sys.stderr)
    traceback.print_exception(exc_type, exc_value, exc_traceback)


def main():
    try:
        # Set up global exception handler
        sys.excepthook = exception_handler

        app = InterviewGUI()
        app.run()
    except Exception as e:
        logger.error(f"Application crashed: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
