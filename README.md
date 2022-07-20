# authentication-sample
Djangoに組み込まれている認証機能を使ったシンプルなアプリ

## 使い方

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

作成したユーザーで以下のURLからログインする  
http://127.0.0.1:8000/accounts/login/  

## 機能
* ログイン / ログアウト
* パスワード変更
* パスワードリセット