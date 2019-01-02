import argparse
import sys
import json

from pyvigicrues.client import VigicruesClient

def main():
    """Main function"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--stationid',
                        required=True, help='Station ID (Ex: H523102501)')
    parser.add_argument('-t', '--type',
                        required=True, help='Station ID (Ex: H for Height / Q for Speed)')
    args = parser.parse_args()

    client = VigicruesClient(args.stationid, args.type)


    try:
        print(json.dumps(client.get_data(), indent=2))
    except BaseException as exp:
        print(exp)
        return 1

if __name__ == '__main__':
    sys.exit(main())
