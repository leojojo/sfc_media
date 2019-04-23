# KOSMOS 資料更新
[KOSMOS](http://kosmos.lib.keio.ac.jp/) < 慶應義塾大学メディアセンター 蔵書検索 > では、その資料を予約している人がいない限りは、借りた資料の[貸出期限更新](http://www.sfc.lib.keio.ac.jp/general/libcir.html) が２回まで出来ます。
しかし、期限内にマイページで更新ボタンを押すのを忘れると、延滞金が発生してしまうので、勝手に更新してくれるようにしました。

## Install
```bash
pip install -r requirements.txt
cp .env.example .env
cp cron.conf.example cron.conf
vim .env
vim cron.conf
crontab cron.conf
```

`.env` と `cron.conf` を編集して自分の環境での設定を記入してください。
`/home/leojojo/personal/sfc_media/media.py` 部分はこのレポジトリのルートのパス (`pwd` コマンドの出力)を入れてください。

## Usage
更新結果画面のスクリーンショットが `screenshot.png` として保存されます。
更新は2回までしか出来ない上に、予約している人がいる場合は更新が出来ないので、定期的に確認してください。
