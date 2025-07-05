# JBL Chat - Real-time Messaging Application

A modern, real-time chat application built with Django, HTMX, and Bootstrap. This application allows users to send and receive messages in real-time with a beautiful, responsive interface.

## Features

- ✅ **User Authentication**: Secure login/logout functionality
- ✅ **User Management**: View all users on the platform
- ✅ **Real-time Messaging**: Send and receive messages with live updates
- ✅ **Modern UI**: Beautiful, responsive interface with Bootstrap
- ✅ **HTMX Integration**: Dynamic interactions without page reloads
- ✅ **REST API**: Full API endpoints for mobile/frontend integration
- ✅ **Docker Support**: Easy deployment with Docker
- ✅ **Auto-scroll**: Messages automatically scroll to bottom
- ✅ **Message Timestamps**: See when messages were sent
- ✅ **User Avatars**: Visual user identification with initials (first letter)

## Technology Stack

- **Backend**: Django 3.2.8
- **Frontend**: HTMX + Bootstrap 5
- **API**: Django REST Framework
- **Database**: SQLite (development)
- **Authentication**: Django Session Authentication
- **Real-time**: HTMX polling every 3 seconds

## Quick Start

### Prerequisites

- Python 3.8+
- Docker (optional)

### Option 1: Docker

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Create test users (in another terminal)**
   ```bash
   docker-compose exec web python jbl_chat/manage.py create_test_users
   ```

3. **Access the application**
   - Open http://localhost:8000
   - Login with any test user (e.g., alice/password123)
  
### Option 2: Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd jbl-chat-master
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python jbl_chat/manage.py migrate
   ```

5. **Create test users**
   ```bash
   python jbl_chat/manage.py create_test_users
   ```

6. **Start the development server**
   ```bash
   python jbl_chat/manage.py runserver
   ```

7. **Access the application**
   - Open http://localhost:8000
   - Login with any test user (e.g., alice/password123)


## Test Users

The application comes with pre-configured test users:

| Username | Password | Email |
|----------|----------|-------|
| alice    | password123 | alice@example.com |
| bob      | password123 | bob@example.com |
| charlie  | password123 | charlie@example.com |
| diana    | password123 | diana@example.com |

## API Endpoints

The application provides REST API endpoints for integration:

- `GET /api/users/` - List all users (excluding current user)
- `GET /api/chat/{user_id}/` - Get conversation messages
- `POST /api/chat/{user_id}/` - Send a new message
- `GET /api/messages/` - Get all messages for current user

### API Authentication

All API endpoints require authentication. Use session authentication by logging in through the web interface first.

## Project Structure

```
jbl_chat/
├── jbl_chat/          # Django project settings
├── chat/              # Main chat application
│   ├── models.py      # Message model
│   ├── views.py       # Web views
│   ├── api_views.py   # API views
│   ├── serializers.py # API serializers
│   ├── urls.py        # URL routing
│   └── templates/     # HTML templates
├── templates/         # Base templates
├── requirements.txt   # Python dependencies
├── docker-compose.yml # Docker configuration
└── README.md         # This file
```

## Key Features Explained

### Real-time Messaging
- Uses HTMX polling every 3 seconds to check for new messages
- Messages appear instantly without page refresh
- Auto-scroll to bottom when new messages arrive

### Modern UI/UX
- Responsive design that works on desktop and mobile
- Message bubbles with different styles for sent/received
- User avatars with initials
- Clean, modern interface with Bootstrap 5

### Security
- Session-based authentication
- CSRF protection on all forms
- Input validation and sanitization
- Secure password handling

## Future Development

### Adding New Features

1. **Models**: Add new models in `chat/models.py`
2. **Views**: Create views in `chat/views.py` or `chat/api_views.py`
3. **Templates**: Add templates in `chat/templates/chat/`
4. **URLs**: Update `chat/urls.py` with new routes

### Database Management

```bash
# Create new migration
python jbl_chat/manage.py makemigrations

# Apply migrations
python jbl_chat/manage.py migrate

# Reset database
python jbl_chat/manage.py flush
```

### Production Considerations

1. **Database**: Use PostgreSQL or MySQL instead of SQLite
2. **Static Files**: Configure static file serving
3. **Security**: Set `DEBUG=False` and configure `ALLOWED_HOSTS`
4. **HTTPS**: Use HTTPS in production
5. **Environment Variables**: Use environment variables for sensitive settings

### Environment Variables

Create a `.env` file for production:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgresql://user:pass@localhost/dbname
```

## License

This project is part of a coding assessment for Jobylon.