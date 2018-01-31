from Library.AikeVideo import CAikeVideo
import Library.TestProgressBar as tpb
import threading


def StartDownLoad(app):
    dwnFilePath = 'download\\VideoList.txt'
    with open(dwnFilePath, 'r', encoding='utf-8') as file:
        fileInfo = file.read()
    fileInfo = fileInfo.strip()
    UrlList = fileInfo.splitlines()
    for i, url in enumerate(UrlList):
        print('the %d url is %s' % (i + 1, url))
        aik = CAikeVideo(url, app)
        aik.DoDownloadLink()


def main():
    app = tpb.App()
    t = threading.Thread(target=StartDownLoad, args=(app,))
    t.start()
    app.MainLoop()


if __name__ == '__main__':
    main()
