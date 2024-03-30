import requests


def after_scenario(context, scenario):
    resonse_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php',
                                       json={"ID": context.bookId},
                                       headers={'Content-Type': 'application/json'}, )

    assert resonse_deleteBook.status_code == 200
    resonse_deleteBook.json()
    res_json = resonse_deleteBook.json()
    print(res_json['msg'])
    assert res_json['msg'] == 'book is successfully deleted'