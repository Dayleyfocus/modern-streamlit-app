# Modern Streamlit Website

A modern, feature-rich web application built with Streamlit. This project follows a modular design pattern allowing for easy feature extension.

## Project Structure

```
app/
├── main.py                    # Main application entry point
├── config.py                  # Configuration settings
├── core/                      # Core application utilities
├── features/                  # Feature modules
│   ├── home/                  # Home page feature
│   ├── dashboard/             # Dashboard feature
│   └── about/                 # About page feature
└── static/                    # Static assets
    ├── css/                   # CSS files
    └── images/                # Image assets
```

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository
2. Install the required packages:

```bash
pip install -r requirements.txt
```

### Running the Application

```bash
streamlit run app/main.py
```

## Features

- Responsive modern UI
- Interactive dashboard
- Dark/light mode theme support
- Modular architecture for easy extension

## Adding New Features

To add a new feature:

1. Create a new directory under `app/features/`
2. Implement your feature components
3. Register your feature in `app/main.py`

## License

MIT 