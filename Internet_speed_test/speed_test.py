import speedtest
import argparse
import sys
import threading
import time
import json
import os
import urllib.request
import socket

def test_speed_alternative():
  """Alternative speed test using a different approach."""
  print("Running alternative speed test...")
  print("Note: This is a basic test and may be less accurate than speedtest.net")
  
  try:
    # Test download speed by downloading a file
    print("Testing download speed...")
    
    # List of test files to try (different sources)
    test_files = [
      ("http://speedtest.ftp.otenet.gr/files/test1Mb.db", 1),  # 1MB file
      ("http://ipv4.download.thinkbroadband.com/5MB.zip", 5),  # 5MB file
      ("https://proof.ovh.net/files/1Mb.dat", 1),  # 1MB file
      ("http://mirror.internode.on.net/pub/test/1meg.test", 1),  # 1MB file
    ]
    
    download_speed = 0
    for url, size_mb in test_files:
      try:
        print(f"  Trying {url.split('//')[-1].split('/')[0]}...")
        start_time = time.time()
        
        # Create request with headers to avoid blocking
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        with urllib.request.urlopen(req, timeout=15) as response:
          data = response.read()
          end_time = time.time()
          
          actual_size_mb = len(data) / (1024 * 1024)  # Convert to MB
          duration = end_time - start_time
          download_speed = (actual_size_mb * 8) / duration  # Convert to Mbps
          
          print(f"  ✓ Downloaded {actual_size_mb:.1f} MB in {duration:.2f} seconds")
          break  # Success, exit loop
          
      except Exception as e:
        print(f"  ✗ Failed: {e}")
        continue
    
    if download_speed == 0:
      print("  All download sources failed - your network may be blocking file downloads")
    
    # Simple ping test to multiple servers
    print("Testing ping...")
    ping_targets = [
      ("8.8.8.8", "Google DNS"),
      ("1.1.1.1", "Cloudflare DNS"),
      ("208.67.222.222", "OpenDNS"),
    ]
    
    all_pings = []
    for ip, name in ping_targets:
      pings = []
      for i in range(3):
        try:
          start = time.time()
          socket.create_connection((ip, 53), timeout=3)
          ping_time = (time.time() - start) * 1000  # Convert to ms
          pings.append(ping_time)
        except:
          pass
      
      if pings:
        avg = sum(pings) / len(pings)
        all_pings.extend(pings)
        print(f"  {name}: {avg:.1f} ms")
    
    overall_ping = sum(all_pings) / len(all_pings) if all_pings else 0
    
    # Display results
    print("\n" + "="*40)
    print("ALTERNATIVE SPEED TEST RESULTS")
    print("="*40)
    if download_speed > 0:
      print(f"Download Speed: {download_speed:.2f} Mbps")
    else:
      print("Download Speed: Unable to test (blocked)")
    print("Upload Speed: Not tested (alternative method)")
    if overall_ping > 0:
      print(f"Average Ping: {overall_ping:.2f} ms")
    else:
      print("Ping: Unable to test")
    print("Note: Results may vary from speedtest.net")
    print("="*40)
    
  except Exception as e:
    print(f"Alternative test failed: {e}")

def test_speed(quick_mode=False, use_cached_server=False):
  """Test internet speed and display results."""
  print("Testing internet speed...")
  
  try:
    # Try different configurations to avoid blocking
    configs_to_try = [
      # Standard config with user agent
      lambda: speedtest.Speedtest(),
      # Try with secure=False
      lambda: speedtest.Speedtest(secure=False),
      # Try with timeout settings
      lambda: speedtest.Speedtest(timeout=10),
    ]
    
    st = None
    config_success = False
    
    for i, config_func in enumerate(configs_to_try):
      try:
        print(f"Trying configuration {i+1}...")
        st = config_func()
        st._user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        
        # Try to get config with retry logic
        for attempt in range(3):
          try:
            st.get_config()
            config_success = True
            print(f"Configuration {i+1} successful!")
            break
          except:
            if attempt < 2:
              print(f"Attempt {attempt+1} failed, retrying in 2 seconds...")
              time.sleep(2)
            else:
              raise
        
        if config_success:
          break
          
      except Exception as e:
        print(f"Configuration {i+1} failed: {e}")
        continue
    
    if not config_success:
      print("\nAll speedtest.net configurations failed.")
      print("Speedtest.net appears to be blocked or unavailable.")
      print("\nTrying alternative speed test method...")
      test_speed_alternative()
      return
    # Now proceed with the speed test
    try:
      if quick_mode:
        st.get_servers()
        st.get_best_server()
      else:
        # Check for cached server
        if use_cached_server:
          cached_server = load_cached_server()
          if cached_server:
            print("Using cached server...")
            st.get_servers([cached_server])
            st.get_best_server()
          else:
            print("Finding best server...")
            st.get_best_server()
            save_cached_server(st.best)
        else:
          print("Finding best server...")
          st.get_best_server()
      
      if quick_mode:
        # Quick test with reduced precision
        print("Running quick speed test...")
        
        # Test download speed with fewer threads
        print("Testing download speed...")
        download_speed = st.download(threads=2) / 1_000_000  # Convert to Mbps
        
        # Test upload speed with fewer threads
        print("Testing upload speed...")
        upload_speed = st.upload(threads=2) / 1_000_000  # Convert to Mbps
      else:
        # Standard test
        print("Testing download speed...")
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        
        print("Testing upload speed...")
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
      
      # Get ping
      ping = st.results.ping
      
      # Display results
      print("\n" + "="*40)
      print("INTERNET SPEED TEST RESULTS")
      print("="*40)
      print(f"Download Speed: {download_speed:.2f} Mbps")
      print(f"Upload Speed: {upload_speed:.2f} Mbps")
      print(f"Ping: {ping:.2f} ms")
      if quick_mode:
        print("(Quick test mode - reduced precision)")
      print("="*40)
      
    except Exception as e:
      print(f"Speed test failed: {e}")
      print("Falling back to alternative speed test...")
      test_speed_alternative()
      
  except Exception as e:
    print(f"Failed to initialize speedtest: {e}")
    print("Trying alternative speed test method...")
    test_speed_alternative()

def load_cached_server():
  """Load cached server information."""
  cache_file = "server_cache.json"
  if os.path.exists(cache_file):
    try:
      with open(cache_file, 'r') as f:
        cache_data = json.load(f)
        # Check if cache is less than 24 hours old
        if time.time() - cache_data['timestamp'] < 86400:  # 24 hours
          return cache_data['server_id']
    except Exception:
      pass
  return None

def save_cached_server(server_info):
  """Save server information to cache."""
  cache_file = "server_cache.json"
  try:
    cache_data = {
      'server_id': server_info['id'],
      'timestamp': time.time(),
      'server_name': server_info['name'],
      'country': server_info['country']
    }
    with open(cache_file, 'w') as f:
      json.dump(cache_data, f)
  except Exception:
    pass  # Fail silently if caching doesn't work

def ping_only_test():
  """Quick ping-only test for basic connectivity."""
  print("Running ping test...")
  try:
    st = speedtest.Speedtest()
    # Set a proper user agent to avoid blocking
    st._user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    st.get_best_server()
    ping = st.results.ping
    
    print("\n" + "="*40)
    print("PING TEST RESULTS")
    print("="*40)
    print(f"Ping: {ping:.2f} ms")
    print(f"Server: {st.best['name']} ({st.best['country']})")
    print("="*40)
    
  except speedtest.ConfigRetrievalError:
    print("Error: Unable to retrieve speedtest configuration.")
    print("This might be due to network restrictions or firewall settings.")
    sys.exit(1)
  except speedtest.NoMatchedServers:
    print("Error: No speedtest servers found.")
    print("Please check your internet connection.")
    sys.exit(1)
  except Exception as e:
    if "403" in str(e) or "Forbidden" in str(e):
      print("Error: Access forbidden by speedtest.net")
      print("This might be due to:")
      print("- Rate limiting (too many recent tests)")
      print("- Corporate firewall blocking speedtest")
      print("- VPN/proxy restrictions")
      print("Try again in a few minutes or from a different network.")
    else:
      print(f"Error testing ping: {e}")
    sys.exit(1)

def diagnose_connection():
  """Diagnose connection issues and provide troubleshooting info."""
  print("Diagnosing connection...")
  print("="*50)
  
  try:
    import urllib.request
    import socket
    
    # Test basic internet connectivity
    print("1. Testing basic internet connectivity...")
    try:
      socket.create_connection(("8.8.8.8", 53), timeout=5)
      print("   ✓ Basic internet connection: OK")
    except:
      print("   ✗ Basic internet connection: FAILED")
      print("   Check your network connection")
      return
    
    # Test speedtest.net accessibility
    print("2. Testing speedtest.net accessibility...")
    try:
      response = urllib.request.urlopen("https://www.speedtest.net", timeout=10)
      if response.getcode() == 200:
        print("   ✓ speedtest.net website: Accessible")
      else:
        print(f"   ? speedtest.net website: Response code {response.getcode()}")
    except Exception as e:
      print(f"   ✗ speedtest.net website: {e}")
      print("   This might indicate firewall or network restrictions")
    
    # Test speedtest API
    print("3. Testing speedtest configuration...")
    try:
      st = speedtest.Speedtest()
      st._user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
      st.get_config()
      print("   ✓ Speedtest configuration: OK")
      
      print("4. Testing server discovery...")
      st.get_servers()
      print(f"   ✓ Found {len(st.servers)} servers")
      
    except Exception as e:
      print(f"   ✗ Speedtest API: {e}")
      if "403" in str(e):
        print("   This indicates speedtest.net is blocking your requests")
    
    print("="*50)
    print("Diagnosis complete.")
    
  except ImportError:
    print("Unable to run full diagnosis - missing modules")
  except Exception as e:
    print(f"Diagnosis failed: {e}")

def main():
  parser = argparse.ArgumentParser(description="Test your internet connection speed")
  parser.add_argument("--simple", "-s", action="store_true", 
             help="Run simple speed test")
  parser.add_argument("--quick", "-q", action="store_true",
             help="Run quick speed test (faster but less precise)")
  parser.add_argument("--ping-only", "-p", action="store_true",
             help="Run ping test only (fastest)")
  parser.add_argument("--alternative", "-a", action="store_true",
             help="Use alternative speed test method (if speedtest.net is blocked)")
  parser.add_argument("--no-cache", action="store_true",
             help="Don't use cached server (slower but more accurate)")
  parser.add_argument("--clear-cache", action="store_true",
             help="Clear server cache and exit")
  parser.add_argument("--diagnose", "-d", action="store_true",
             help="Diagnose connection issues")
  
  args = parser.parse_args()
  
  # Clear cache if requested
  if args.clear_cache:
    cache_file = "server_cache.json"
    if os.path.exists(cache_file):
      os.remove(cache_file)
      print("Server cache cleared.")
    else:
      print("No cache file found.")
    return
  
  # Run diagnosis if requested
  if args.diagnose:
    diagnose_connection()
    return
  
  # Run alternative test if requested
  if args.alternative:
    test_speed_alternative()
    return
  
  # Choose test mode
  if args.ping_only:
    ping_only_test()
  elif args.quick:
    test_speed(quick_mode=True, use_cached_server=not args.no_cache)
  elif args.simple or len(sys.argv) == 1:
    test_speed(quick_mode=False, use_cached_server=not args.no_cache)
  else:
    parser.print_help()

if __name__ == "__main__":
  main()