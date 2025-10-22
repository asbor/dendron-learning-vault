---
id: knowledge.setup.sql-server-connection
title: SQL Server Connection Guide
desc: "Setup and configuration guide"
updated: 1761144402000
created: 1761144402000
---


## Overview

Complete guide for establishing SQL Server connections from WSL using SQLAlchemy and pyodbc.

## Prerequisites

- WSL (Ubuntu 22.04 recommended)
- SQL Server instance (local or remote)
- Python 3.x installed
- Basic command line familiarity

## Installation Steps

### 1. Install Microsoft ODBC Driver

```bash
# Import Microsoft's GPG Key and Add Repository
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list

# Update package lists
sudo apt-get update

# Install ODBC Driver 18
sudo ACCEPT_EULA=Y apt-get install msodbcsql18
```

### 2. Verify Installation

```bash
odbcinst -q -d -n "ODBC Driver 18 for SQL Server"
```

Expected output: Driver details displayed if installation successful.

### 3. Python Environment Setup

```bash
# Create virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate

# Install required packages
pip install python-dotenv sqlalchemy pyodbc
```

## Configuration

### Environment Variables (.env file)

```dotenv
SQL_USERNAME=YourSqlUsername
SQL_PASSWORD=YourSqlPassword
SQL_SERVER=YourSqlServerAddress
```

### Connection Script Template

```python
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

username = os.getenv("SQL_USERNAME")
password = os.getenv("SQL_PASSWORD")
server   = os.getenv("SQL_SERVER")

# Create SQLAlchemy engine
engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}:1433/DATABASE_NAME?"
    "trusted_connection=no&TrustServerCertificate=yes&driver=ODBC+Driver+18+for+SQL+Server"
)

# Test connection
conn = engine.connect()
print("Connection established:", type(conn))
conn.close()
```

## Key Connection String Parameters

- `mssql+pyodbc://` - SQLAlchemy dialect for SQL Server with pyodbc
- `:1433` - Default SQL Server port
- `trusted_connection=no` - Use SQL Authentication instead of Windows Auth
- `TrustServerCertificate=yes` - Bypass SSL certificate validation
- `driver=ODBC+Driver+18+for+SQL+Server` - Specify ODBC driver version

## Usage

1. Create `.env` file with your credentials
2. Run the connection script: `python connect.py`
3. Verify successful connection output

## Common Issues & Solutions

### Driver Not Found
- **Problem**: ODBC driver not installed or incorrect version
- **Solution**: Verify installation with `odbcinst -q -d -n "ODBC Driver 18 for SQL Server"`

### SSL Certificate Error
- **Problem**: Certificate validation failures
- **Solution**: Add `TrustServerCertificate=yes` to connection string

### Authentication Issues
- **Problem**: Login failures
- **Solution**: 
  - Verify credentials in `.env` file
  - Ensure SQL Server allows SQL Authentication
  - Check server address and port accessibility

### Connection Timeout
- **Problem**: Network connectivity issues
- **Solution**:
  - Verify server is accessible from WSL
  - Check firewall settings on SQL Server
  - Confirm SQL Server is running and accepting connections

## Security Best Practices

1. **Never commit `.env` files** to version control
2. **Use strong passwords** for SQL authentication
3. **Enable SSL certificates** in production environments
4. **Restrict database user permissions** to minimum required
5. **Use connection pooling** for production applications

## Related Tools

- **SQL Server Management Studio (SSMS)** - GUI management tool
- **Azure Data Studio** - Cross-platform database tool
- **VS Code SQL Server extension** - Integrated development experience

## Example Production Connection

```python
from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool

# Production-ready engine with connection pooling
engine = create_engine(
    connection_string,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    pool_recycle=3600
)

# Execute query with proper error handling
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT @@VERSION"))
        version = result.fetchone()[0]
        print(f"SQL Server Version: {version}")
except Exception as e:
    print(f"Connection failed: {e}")
```

## Testing Connection

Quick test to verify everything works:

```bash
# Test ODBC driver
isql -v -k "DRIVER={ODBC Driver 18 for SQL Server};SERVER=your_server;UID=your_user;PWD=your_password;TrustServerCertificate=yes"

# Test Python connection
python -c "
from sqlalchemy import create_engine
engine = create_engine('your_connection_string')
conn = engine.connect()
print('Success!')
conn.close()
"
```

---
*Created from WSL SQL Server connection documentation*