# 這是一個簡單的 Python 程式範例，說明命名空間、函式定義和網路請求。

# 這個變數 n 放在模組的全域命名空間中。
# 這裡先給它初始值 0，方便後面使用。
n = 0

# 第一個 main() 函式定義，用來印出目前的命名空間資訊。
def main():
    print("這裡是main funtion的命名空間")
    # 這裡會印出全域變數 n 的值。
    print(n)

# 當這個檔案被直接執行時，以下程式碼才會執行。
# 這是一個常見的 Python idiom，用來區分「直接執行」與「被匯入」的情況。
if __name__ == '__main__':
    # 直接執行時，把全域變數 n 改成 10。
    n = 10
    main()

    # 在這裡才匯入 requests 模組，這是用來發出 HTTP 請求的第三方套件。
    import requests


# 第二個 main() 函式定義，這會覆蓋前面的第一個 main()。
# 也就是說，真正最後會執行的是這個 main()，而不是上面的那個。
def main():
    # 設定要抓取的 YouBike 資料的網址。
    url: str = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

    # 使用 requests.get() 發出 HTTP GET 請求。
    response: requests.Response = requests.get(url)
    # 印出 response 的型別，方便知道回傳的是什麼物件。
    print(type(response))

    # status_code 代表 HTTP 回應狀態碼，200 表示成功。
    if response.status_code == 200:
        # 解析 JSON 資料成為 Python 的 list 或 dict。
        data: list = response.json()
        print("下載成功")
        print(type(data))
        print(len(data))
        # 印出第一筆資料內容。
        print(data[0])
    else:
        # 若不是 200，就表示下載失敗，印出錯誤碼。
        print("下載失敗")
        print(response.status_code)

# 這裡再次檢查是否直接執行此檔案。
# 因為上面的第一個 __main__ 也會執行，實際上這裡會執行第二個 main()。
if __name__ == '__main__':
    main()