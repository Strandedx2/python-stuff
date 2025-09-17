# Internet Speed Test 🚀

A fast and optimized Python script for testing your internet connection speed using the speedtest.net infrastructure.

## Features

- **Multiple Test Modes**: Quick, standard, and ping-only tests
- **Server Caching**: Automatic caching of best servers for faster subsequent tests
- **Optimized Performance**: Reduced test times through threading and configuration optimizations
- **Detailed Results**: Download speed, upload speed, and ping measurements
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

# Ping test only (fastest)
python speed_test.py --ping-only

# Force fresh server discovery (no cache)
python speed_test.py --no-cache

# Clear server cache
python speed_test.py --clear-cache
```

### Command Line Options

| Option | Short | Description |
|--------|-------|-------------|
| `--simple` | `-s` | Run simple speed test |
| `--quick` | `-q` | Run quick speed test (faster but less precise) |
| `--ping-only` | `-p` | Run ping test only (fastest) |
| `--no-cache` | | Don't use cached server (slower but more accurate) |
| `--clear-cache` | | Clear server cache and exit |

## Performance Comparison

| Test Mode | Typical Time | Use Case |
|-----------|-------------|----------|
| **Ping Only** | 5-10 seconds | Quick connectivity check |
| **Quick Mode** | 15-25 seconds | Fast general test |
| **Standard (cached)** | 20-35 seconds | Normal test with cached server |
| **Standard (no cache)** | 30-45 seconds | Most accurate test |

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

### 🔧 Optimized Threading
- Configurable thread counts based on test mode
- Quick mode uses fewer threads for faster startup
- Balanced performance vs. speed

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

### Common Issues

1. **"ModuleNotFoundError: No module named 'speedtest'"**
   - Install the required package: `pip install speedtest-cli`

2. **Slow initial test**
   - First run discovers the best server (normal behavior)
   - Subsequent tests will be faster due to caching

3. **Connection errors**
   - Check your internet connection
   - Try using `--no-cache` to force fresh server discovery
   - Run ping-only test first: `python speed_test.py --ping-only`

### Performance Tips

- Use `--quick` for routine monitoring
- Use `--ping-only` for basic connectivity checks
- Clear cache if you change locations: `python speed_test.py --clear-cache`
- Use `--no-cache` if you want the most accurate server selection

## Technical Details

### Dependencies
- `speedtest-cli`: Main library for speed testing
- `argparse`: Command line argument parsing (built-in)
- `sys`: System operations (built-in)
- `threading`: Thread management (built-in)
- `time`: Time operations (built-in)
- `json`: JSON handling for cache (built-in)
- `os`: Operating system interface (built-in)

### Speed Test Process
1. **Server Discovery**: Find optimal server (cached after first run)
2. **Download Test**: Measure incoming bandwidth
3. **Upload Test**: Measure outgoing bandwidth
4. **Results**: Display formatted results with ping information

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this speed test tool.

## License

This project uses the speedtest.net infrastructure through the speedtest-cli library. Please respect their terms of service.