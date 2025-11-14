# tools/airis_time.py
import argparse
from ufa_time_fetcher import UfaTimeFetcher

def main():
    parser = argparse.ArgumentParser(description='AIRIS - точное время в Уфе')
    parser.add_argument('--city', default='ufa', help='Город')
    parser.add_argument('--accurate', action='store_true', help='Точное время онлайн')
    
    args = parser.parse_args()
    
    fetcher = UfaTimeFetcher()
    time_data = fetcher.fetch_accurate_time()
    
    print(f"🏴 AIRIS Time Service")
    print(f"📍 {time_data['city']} | {time_data['timezone']}")
    print(f"🕐 {time_data['accurate_time']}")
    
if __name__ == "__main__":
    main()