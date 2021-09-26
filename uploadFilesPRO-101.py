import dropbox,os


class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_folder(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dir,files in os.walk(file_from):
            for file in files:
                local_path = os.path.join(root,file)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = "/"+file_to+"/"+relative_path
                print(dropbox_path)
                with open(file_from,'rb') as f:
                    dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.A5OfAVYUZ8m8uJ5BjsNTkpd508lAsQuYagDRzSivP14k6ot_RW1PKwQqma1UsmxjfPO6dq0lQl5yzCDqEjUllSMVlLymZJNyb5sOIcs0qVr7h5kv1zJyqvDEs2avIDNz6rbrZCM'
    transferdata = TransferData(access_token)

    file_from = input('Enter 1st File path: ')
    file_to = input('Enter path to upload: ')
    transferdata.upload_folder(file_from,file_to)
    print("Files uploaded successfully")

if __name__ == '__main__':
    main()