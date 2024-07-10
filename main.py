from src.extract import extract
from src.transform import transform
from src.load import load

def main():
    # File and database paths
    file_path = 'data/employees.csv'
    db_path = 'data/employee_data.db'

    # Extract
    df = extract(file_path)

    # Transform
    df = transform(df)

    # Load
    load(df, db_path)

if __name__ == '__main__':
    main()
