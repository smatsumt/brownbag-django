# Generated by Django 3.0.5 on 2020-04-12 06:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'オーナー'), (1, 'ユーザー'), (-1, '---')], default=-1, verbose_name='type')),
                ('agreement', models.BooleanField(default=False, verbose_name='agreement')),
                ('mail', models.CharField(default=None, max_length=512, null=True, verbose_name='mail')),
                ('name', models.CharField(default=None, max_length=512, null=True, unique=True, verbose_name='name')),
                ('genre_sel', models.IntegerField(choices=[(0, 'その他'), (1, 'お弁当・お惣菜'), (2, '中華料理'), (3, '和食・日本料理・お寿司'), (4, 'ピザ・パスタ'), (5, '洋食・西洋料理・とんかつ'), (6, '居酒屋・ダイニングバー・焼鳥'), (7, 'アジア・エスニック・カレー'), (8, 'ステーキ・ハンバーグ・焼肉・ホルモン'), (9, '創作料理・無国籍料理'), (10, 'ラーメン'), (11, 'カフェ・喫茶店'), (12, 'バー・パブ・ラウンジ'), (13, 'パン・サンドイッチ'), (14, 'スイーツ'), (15, 'スーパーマーケット・コンビニエンスストア'), (-1, 'ジャンルなし')], default=-1, verbose_name='genre_sel')),
                ('description', models.CharField(default=None, max_length=256, null=True, verbose_name='description')),
                ('addr_sel', models.CharField(default=None, max_length=256, null=True, verbose_name='addr_sel')),
                ('addr', models.CharField(default=None, max_length=256, null=True, verbose_name='addr')),
                ('area_sel', models.IntegerField(choices=[(0, 'その他'), (1, '武蔵小杉・新丸子・元住吉'), (2, '武蔵新城・武蔵中原'), (3, '溝の口・梶ヶ谷・鷺沼'), (4, '登戸・稲田堤'), (5, '川崎・平間'), (6, '百合ヶ丘・新百合ヶ丘'), (-1, '地域の指定なし')], default=-1, verbose_name='area_sel')),
                ('takeaway_sel', models.IntegerField(choices=[(0, 'その他'), (1, '対応している'), (2, '対応してない'), (3, '準備中'), (-1, '指定なし')], default=-1, verbose_name='takeaway_sel')),
                ('takeaway_menu', models.TextField(blank=True, default='', max_length=1024, verbose_name='takeaway_menu')),
                ('takeaway_note', models.CharField(default=None, max_length=512, null=True, verbose_name='takeaway_note')),
                ('delivery_demaekan', models.BooleanField(default=False, verbose_name='delivery_demaekan')),
                ('delivery_ubereats', models.BooleanField(default=False, verbose_name='delivery_ubereats')),
                ('delivery_own', models.BooleanField(default=False, verbose_name='delivery_own')),
                ('delivery_other', models.BooleanField(default=False, verbose_name='delivery_other')),
                ('delivery_note', models.TextField(blank=True, default='', max_length=512, verbose_name='delivery_note')),
                ('phone', models.CharField(default=None, max_length=256, null=True, verbose_name='phone')),
                ('open_day', models.TextField(blank=True, default='', max_length=1024, verbose_name='open_day')),
                ('payment_cash', models.BooleanField(default=False, verbose_name='payment_cash')),
                ('payment_card', models.BooleanField(default=False, verbose_name='payment_card')),
                ('payment_qr', models.BooleanField(default=False, verbose_name='payment_qr')),
                ('payment_emoney', models.BooleanField(default=False, verbose_name='payment_emoney')),
                ('payment_note', models.TextField(blank=True, default='', max_length=512, verbose_name='payment_note')),
                ('website', models.CharField(default=None, max_length=1024, null=True, verbose_name='website')),
                ('twitter', models.CharField(default=None, max_length=256, null=True, verbose_name='twitter')),
                ('facebook', models.CharField(default=None, max_length=256, null=True, verbose_name='facebook')),
                ('instagram', models.CharField(default=None, max_length=256, null=True, verbose_name='instagram')),
                ('line', models.CharField(default=None, max_length=256, null=True, verbose_name='line')),
                ('sns_other', models.CharField(default=None, max_length=256, null=True, verbose_name='sns_other')),
                ('transportation', models.CharField(default=None, max_length=256, null=True, verbose_name='transportation')),
                ('diet_note', models.TextField(blank=True, default='', max_length=512, verbose_name='diet_note')),
                ('allergy_note', models.TextField(blank=True, default='', max_length=512, verbose_name='allergy_note')),
                ('latitude', models.FloatField(default=0.0, verbose_name='latitude')),
                ('longitude', models.FloatField(default=0.0, verbose_name='longitude')),
                ('covid19_note', models.TextField(blank=True, default='', max_length=512, verbose_name='covid19_note')),
                ('note', models.TextField(blank=True, default='', max_length=512, verbose_name='note')),
                ('expired_shop_date', models.DateTimeField(null=True)),
                ('closes_shop_date', models.DateTimeField(null=True)),
                ('soldout_takeaway_date', models.DateTimeField(null=True)),
                ('soldout_delivery_date', models.DateTimeField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('update_date', models.DateTimeField(blank=True, null=True, verbose_name='修正日')),
            ],
            options={
                'verbose_name': '店',
                'verbose_name_plural': '店',
            },
        ),
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_data', models.ImageField(blank=True, default='/static/brownbags/images/none.png', null=True, upload_to='images/', verbose_name='画像')),
                ('image_data_class', models.IntegerField(choices=[(0, 'その他'), (1, '店舗'), (2, 'テイクアウト'), (-1, '---')], default=-1, verbose_name='クラス')),
                ('order', models.IntegerField(default=0, verbose_name='順番')),
                ('expired_date', models.DateTimeField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='brownbags.Shop', verbose_name='Shop')),
            ],
            options={
                'verbose_name': '画像',
                'verbose_name_plural': '画像',
            },
        ),
    ]
