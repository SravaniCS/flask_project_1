from flask import Flask

FAI=Flask(__name__)

@FAI.route('/StringResponse')
def StringResponse(): 
    return 'This is the First View of Flask'

@FAI.route('/str_resp')
def str_resp():
    return 'Hai..!'


if __name__=='__main__':
    FAI.run(debug=True)