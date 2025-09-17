# Internet Speed Test 🚀

A fast, robust, and optimized Python script for testing your internet connection speed with multiple fallback methods, advanced error handling, and continuous monitoring capabilities.

## Features

- **Multiple Test Modes**: Quick, standard, ping-only, and alternative tests
- **Continuous Monitoring**: Run tests at configurable intervals with data logging
- **Server Caching**: Automatic caching of best servers for faster subsequent tests
- **Optimized Performance**: Reduced test times through threading and configuration optimizations
- **Robust Fallback System**: Alternative speed test when speedtest.net is blocked
- **Advanced Error Handling**: Retry logic and multiple configuration attempts
- **Data Logging**: Save results to JSON files with timestamps and statistics
- **Detailed Results**: Download speed, upload speed, and ping measurements
- **Comprehensive Diagnostics**: Built-in connection troubleshooting
- **Command Line Interface**: Easy-to-use CLI with multiple options

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install the required package directly:

```bash
pip install speedtest-cli
```

## Usage

### Basic Commands

```bash
# Standard speed test (recommended)
python speed_test.py

# Quick test (faster, slightly less precise)
python speed_test.py --quick

# Alternative speed test (when speedtest.net is blocked)
python speed_test.py --alternative

# Ping test only (fastest)
python speed_test.py --ping-only

# Force fresh server discovery (no cache)
python speed_test.py --no-cache

# Diagnose connection issues
python speed_test.py --diagnose

# Clear server cache
python speed_test.py --clear-cache
```

### Continuous Monitoring Commands

```bash
# Run tests every 30 seconds indefinitely
python speed_test.py --continuous 30

# Run alternative tests every 10 seconds, max 20 tests
python speed_test.py --alternative --continuous 10 --max-tests 20

# Monitor with ping-only every 5 seconds, save to file
python speed_test.py --ping-only --continuous 5 --output network_log.json

# Quick tests every 60 seconds with logging
python speed_test.py --quick --continuous 60 --max-tests 100 --output hourly_monitor.json

# Full monitoring with all features
python speed_test.py --continuous 15 --max-tests 50 --output monitoring.json
```

### Command Line Options

| Option | Short | Description |
|--------|-------|-------------|
| `--simple` | `-s` | Run simple speed test |
| `--quick` | `-q` | Run quick speed test (faster but less precise) |
| `--ping-only` | `-p` | Run ping test only (fastest) |
| `--alternative` | `-a` | Use alternative speed test method (if speedtest.net is blocked) |
| `--continuous SECONDS` | `-c` | Run tests continuously every SECONDS interval |
| `--max-tests COUNT` | `-m` | Maximum number of tests to run (use with --continuous) |
| `--output FILE` | `-o` | Save results to JSON file (use with --continuous) |
| `--no-cache` | | Don't use cached server (slower but more accurate) |
| `--clear-cache` | | Clear server cache and exit |
| `--diagnose` | `-d` | Diagnose connection issues |

## Performance Comparison

| Test Mode | Typical Time | Use Case |
|-----------|-------------|----------|
| **Ping Only** | 5-10 seconds | Quick connectivity check |
| **Alternative Test** | 10-20 seconds | When speedtest.net is blocked |
| **Quick Mode** | 15-25 seconds | Fast general test |
| **Standard (cached)** | 20-35 seconds | Normal test with cached server |
| **Standard (no cache)** | 30-45 seconds | Most accurate test |
| **Continuous Monitoring** | Variable | Long-term network monitoring |

## Speed Optimizations

### 🎯 Server Caching
- Automatically saves the best server for 24 hours
- Eliminates repeated server discovery (saves 5-15 seconds)
- Cache file: `server_cache.json`

### ⚡ Quick Test Mode
- Uses fewer threads (2 instead of default 4-8)
- Reduced precision for faster results
- Maintains accuracy while improving speed

### 🏃 Ping-Only Test
- Ultra-fast connectivity check
- Only tests latency, skips bandwidth tests
- Perfect for quick network diagnostics

### � Alternative Speed Test
- Independent of speedtest.net infrastructure
- Uses multiple download sources worldwide
- Tests from various servers for better coverage
- Automatic fallback when speedtest.net is blocked

### �🔧 Optimized Threading
- Configurable thread counts based on test mode
- Quick mode uses fewer threads for faster startup
- Balanced performance vs. speed

### 🛡️ Advanced Error Handling
- Multiple configuration attempts with retry logic
- Automatic fallback to alternative methods
- Comprehensive error diagnosis and solutions

### 📊 Continuous Monitoring
- Configurable test intervals (minimum 1 second)
- Real-time test numbering and timestamps
- Automatic data logging to JSON files
- Summary statistics (min/max/average speeds and ping)
- Graceful interruption with Ctrl+C
- Optional test count limits

## Output Format

### Standard Test Results
```
========================================
INTERNET SPEED TEST RESULTS
========================================
Download Speed: 85.42 Mbps
Upload Speed: 12.34 Mbps
Ping: 15.67 ms
========================================
```

### Ping-Only Test Results
```
========================================
PING TEST RESULTS
========================================
Ping: 15.67 ms
Server: Example Server (United States)
========================================
```

### Alternative Test Results
```
========================================
ALTERNATIVE SPEED TEST RESULTS
========================================
Download Speed: 11.63 Mbps
Upload Speed: Not tested (alternative method)
Average Ping: 30.96 ms
Note: Results may vary from speedtest.net
========================================
```

## Continuous Monitoring

The script supports continuous monitoring with automatic data logging and statistics.

### Monitoring Output Example
```
Starting continuous speed testing every 10 seconds...
Will run 5 tests total
Press Ctrl+C to stop

==================================================
TEST #1 - 2025-09-17 13:19:43
==================================================
[Test results here]

Waiting 10 seconds until next test...

==================================================
TEST #2 - 2025-09-17 13:19:53
==================================================
[Test results here]

...

Completed 5 tests. Stopping.
Results saved to monitoring.json

==================================================
SUMMARY STATISTICS
==================================================
Total tests run: 5
Successful tests: 5
Download Speed - Min: 11.63 Mbps
Download Speed - Max: 15.05 Mbps
Download Speed - Avg: 13.24 Mbps
Ping - Min: 25.10 ms
Ping - Max: 38.88 ms
Ping - Avg: 31.99 ms
==================================================
```

### JSON Output Format
```json
[
  {
    "timestamp": "2025-09-17 13:19:43",
    "test_number": 1,
    "download_speed": 15.054236097308856,
    "upload_speed": null,
    "ping": 35.223192638821075,
    "test_type": "alternative"
  },
  {
    "timestamp": "2025-09-17 13:19:53",
    "test_number": 2,
    "download_speed": 12.33960612472587,
    "upload_speed": 25.67,
    "ping": 28.45,
    "test_type": "speedtest"
  }
]
```

### Monitoring Use Cases
- **Network Performance**: Track connection quality over time
- **ISP Verification**: Monitor if you're getting advertised speeds
- **Troubleshooting**: Identify patterns in connection issues
- **Peak Analysis**: See how speeds vary throughout the day
- **Gaming/Streaming**: Monitor for latency spikes during activities
- **Work From Home**: Ensure stable connection during business hours
- **Service Level Monitoring**: Automated network quality reporting

## Cache Management

The script automatically caches the best server to speed up subsequent tests:

- **Cache Duration**: 24 hours
- **Cache File**: `server_cache.json`
- **Auto-Refresh**: Cache automatically expires after 24 hours

### Manual Cache Control

```bash
# View current cache status (check if server_cache.json exists)
ls server_cache.json

# Clear cache manually
python speed_test.py --clear-cache

# Run test without using cache
python speed_test.py --no-cache
```

## Troubleshooting

### Common Issues and Solutions

#### 1. **"HTTP Error 403: Forbidden" or "ConfigRetrievalError"**
   - **Cause**: Speedtest.net is blocking your requests
   - **Solutions**:
     ```bash
     # Try alternative speed test
     python speed_test.py --alternative
     
     # Wait 10-15 minutes and try again
     python speed_test.py --quick
     
     # Run diagnostics to identify the issue
     python speed_test.py --diagnose
     ```

#### 2. **"ModuleNotFoundError: No module named 'speedtest'"**
   - **Solution**: Install the required package
     ```bash
     pip install speedtest-cli
     ```

#### 3. **Slow initial test**
   - **Cause**: First run discovers the best server (normal behavior)
   - **Solution**: Subsequent tests will be faster due to caching

#### 4. **Connection timeout errors**
   - **Solutions**:
     ```bash
     # Try ping-only test first
     python speed_test.py --ping-only
     
     # Use alternative method
     python speed_test.py --alternative
     
     # Clear cache and retry
     python speed_test.py --clear-cache
     ```

#### 5. **Inconsistent results**
   - **Solutions**:
     ```bash
     # Force fresh server discovery
     python speed_test.py --no-cache
     
     # Try multiple test methods for comparison
     python speed_test.py --quick
     python speed_test.py --alternative
     ```

#### 6. **Continuous monitoring best practices**
   - **Recommended intervals**: 
     - Ping-only: 5-10 seconds for real-time monitoring
     - Quick tests: 30-60 seconds for regular monitoring  
     - Full tests: 300+ seconds (5+ minutes) for detailed analysis
   - **Solutions**:
     ```bash
     # Light monitoring (ping-only every 10 seconds)
     python speed_test.py --ping-only --continuous 10 --max-tests 100
     
     # Regular monitoring (quick tests every minute)
     python speed_test.py --quick --continuous 60 --output hourly.json
     
     # Detailed monitoring (full tests every 5 minutes)
     python speed_test.py --continuous 300 --max-tests 50 --output detailed.json
     ```

### Diagnostic Commands

```bash
# Full diagnostic report
python speed_test.py --diagnose

# Test basic connectivity only
python speed_test.py --ping-only

# Test without speedtest.net dependency
python speed_test.py --alternative

# Monitor network continuously for troubleshooting
python speed_test.py --continuous 10 --max-tests 20 --output debug.json
```

### What the diagnostics check:
1. **Basic Internet Connectivity**: Tests connection to Google DNS
2. **Speedtest.net Accessibility**: Checks if speedtest.net website is reachable
3. **API Configuration**: Tests speedtest API access
4. **Server Discovery**: Verifies ability to find speed test servers

### Network Restrictions

If you're on a corporate network or have strict firewall settings:

1. **Use Alternative Method**: `python speed_test.py --alternative`
2. **Check with IT**: Some networks block speedtest traffic
3. **Try Different Network**: Test from mobile hotspot to compare
4. **VPN Issues**: Disable VPN temporarily if experiencing blocks

### Performance Tips

- Use `--quick` for routine monitoring
- Use `--ping-only` for basic connectivity checks
- Use `--alternative` when speedtest.net is blocked or slow
- Use `--continuous` with appropriate intervals for network monitoring
- Clear cache if you change locations: `python speed_test.py --clear-cache`
- Use `--no-cache` if you want the most accurate server selection
- Run `--diagnose` first if experiencing issues
- Use `--max-tests` to prevent runaway continuous monitoring
- Save monitoring data with `--output` for trend analysis

## Technical Details

### Dependencies
- `speedtest-cli`: Main library for speed testing
- `argparse`: Command line argument parsing (built-in)
- `sys`: System operations (built-in)
- `threading`: Thread management (built-in)
- `time`: Time operations (built-in)
- `json`: JSON handling for cache and data logging (built-in)
- `os`: Operating system interface (built-in)
- `urllib.request`: HTTP requests for alternative tests (built-in)
- `socket`: Network socket operations (built-in)
- `datetime`: Timestamp generation for monitoring (built-in)

### Speed Test Process
1. **Configuration Attempt**: Try multiple speedtest configurations with retry logic
2. **Server Discovery**: Find optimal server (cached after first run)
3. **Download Test**: Measure incoming bandwidth
4. **Upload Test**: Measure outgoing bandwidth  
5. **Results**: Display formatted results with ping information
6. **Fallback**: If speedtest.net fails, automatically use alternative method

### Alternative Speed Test Process
1. **Download Test**: Test download speed using multiple international sources
2. **Ping Test**: Test latency to multiple DNS servers (Google, Cloudflare, OpenDNS)
3. **Results**: Display basic speed and connectivity information
4. **Sources**: Uses various reliable test file servers worldwide

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this speed test tool.

## License

This project uses the speedtest.net infrastructure through the speedtest-cli library. Please respect their terms of service.