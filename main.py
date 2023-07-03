import mongo_crud_db

db_type = 'mongodb' # mysql postersql mongodb

def main():
    mongo_crud_db.read_data()

if __name__ == '__main__':
    main()