import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
            
        print('Your file has been uploaded to Dropbox')   

def main():
    access_token = 'sl.BFbL9zONG3iElnwmtmWspWNuhMuACyEnufjqXh3CFN3WDzJa6gy1sKrugKwGoJQ2yscvOzY3uJ0jm78J61aEHx0_g5sHvjJfCapBkLKFm2g8KkQcs8h3PU1tQOGksK3FjJ5koyWW-m2X'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to upload: ')
    file_to = input('Enter the full path of folder or file in dropbox: ')

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()