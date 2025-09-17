import speedtest
import argparse
import sys

def test_speed():
  """Test internet speed and display results."""
  print("Testing internet speed...")
  
  try:
    # Create speedtest object
    st = speedtest.Speedtest()
    
    # Get best server
    print("Finding best server...")
    st.get_best_server()
    
    # Test download speed
    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    
    # Test upload speed
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
    print("="*40)
    
  except Exception as e:
    print(f"Error testing speed: {e}")
    sys.exit(1)

def main():
  parser = argparse.ArgumentParser(description="Test your internet connection speed")
  parser.add_argument("--simple", "-s", action="store_true", 
             help="Run simple speed test")
  
  args = parser.parse_args()
  
  if args.simple or len(sys.argv) == 1:
    test_speed()
  else:
    parser.print_help()

if __name__ == "__main__":
  main()